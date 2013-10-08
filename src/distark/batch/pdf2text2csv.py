# encoding: utf-8
import sh
import sys
import os
import re

from sh import wc
from sh import cat
from sh import mv
from distark.commons.utils.db.mongopool import MongoPool
from distark.commons.utils.MyConfiguration import Configuration

MODE_DESC='description'
MODE_POINT='points'
MODE_PROPERTIES='prop'
MODE_QTE="qte"
MODE_NOTHING='nothing'

MAX_CONN = 1
host = Configuration.getworker()['mongo']['host']
port = Configuration.getworker()['mongo']['port']
db = Configuration.getworker()['mongo']['db']
mp = MongoPool(host, port, db, MAX_CONN)
dbcon = mp.getConnection()
refloat = re.compile('^\d+(\.\d+)*$')


def is_mode_qte(line):
    res=False
    qte = ['100 g', '1 part', '1 pot', u'1 unité', '1 tranche',
           '1 portion', '100 ml', '1 canette', 'c.c.']
    if line in qte:
        res = True

    return res


def store_data(lst_desc, lst_qte, lst_cal, lst_prot, lst_glu, lst_lip):

    data = []
    # output as json
    i=0
    for _ in lst_desc:
        rec = {}
        rec['name']=lst_desc[i]
        rec['qty']=lst_qte[i]
        rec['cal']=float(lst_cal[i])
        rec['pro']=float(lst_prot[i])
        rec['glu']=float(lst_glu[i])
        rec['lip']=float(lst_lip[i])
        data.append(rec)
        i+=1

    print "store:", len(data)
    #store in db
    dbcon.alim.insert(data)


#returns if the current line must be recorded
def define_mode(line, mode):
    #print line
    store_line = True
    if line != '':
        mode_changed = False

        if line == 'quantite':
            mode = MODE_DESC
            print "mode desc"
            store_line = False
            mode_changed = True
        elif line in ['points', u'10 gr ou unité', u'100 gr ou unité']:
            mode = MODE_POINT
            print "mode points"
            store_line = False
            mode_changed = True
        elif line in ['calories', 'lipides',
                      'glucides', 'proteines', 'proteines glucides']:
            mode = MODE_PROPERTIES
            print "mode properties"
            store_line = False
            mode_changed = True

        if not(mode_changed):
            if (mode in [MODE_DESC, MODE_QTE, MODE_POINT]):
                if is_mode_qte(line):
                    mode = MODE_QTE
                    store_line = True
                # si ça match un nombre (points)
                elif refloat.match(line):
                    store_line = False
                else:
                    mode = MODE_DESC
                    store_line = True
    else:
        store_line = False
    return mode, store_line


def readfile(input_file):

    txtoutput = "out.tmp"

    sh.rm(txtoutput)

    res = sh.pdf2txt(input_file, _out=txtoutput)
    print "nb lines in pdf2txt", res

    res = wc("-l", txtoutput)
    print "nb lines in ", txtoutput, ":", res
    #print cat(txtoutput)

    lst_desc = []
    lst_qte = []
    lst_cal = []
    lst_prot = []
    lst_glu = []
    lst_lip = []

    mode = MODE_NOTHING
    previous = 'lip'

    for line in cat(txtoutput, _iter=True):
        line = line.lower().strip()
        mode, store_line = define_mode(line, mode)
        if store_line:
            if (mode == MODE_DESC):
                lst_desc.append(line)
            elif (mode == MODE_QTE):
                lst_qte.append(line)
            elif (mode == MODE_PROPERTIES):
                if previous == 'lip':
                    lst_cal.append(line)
                    previous = 'cal'
                elif previous == 'cal':
                    lst_prot.append(line)
                    previous = 'prot'
                elif previous == 'prot':
                    lst_glu.append(line)
                    previous = 'glu'
                elif previous == 'glu':
                    lst_lip.append(line)
                    previous = 'lip'

    d = len(lst_desc)
    q = len(lst_qte)
    c = len(lst_cal)
    p = len(lst_prot)
    g = len(lst_glu)
    l = len(lst_lip)

    print "desc:", d
    print "qte:", q
    print "cal:", c
    print "prot:", p
    print "glu:", g
    print "lip:", l
    #for l in lst_cal:
    #    print l

    data_check = True
    if not((d != 0) and (d == q) and (q == c) and (c == p)):
        data_check = False
    if not((p == g) and (g == l)):
        data_check = False

    if data_check:
        print "data check: OK"
        try:
            store_data(lst_desc, lst_qte, lst_cal, lst_prot, lst_glu, lst_lip)
        except:
            pass
        else:
            # move file if no errror
            input_filename = input_file.split('/')
            target_dir = "/home/guillaume/git/distark/data/ok/"
            target = os.path.join(target_dir, input_filename[-1])
            print "mv", input_file, target
            mv(input_file, target)
    else:
        print "data check: KO"

if __name__ == "__main__":

    to_process = []
    dir_path = sys.argv[1]

    if os.path.isdir(dir_path):

        dir = os.listdir(dir_path)
        for f in dir:
            f = os.path.join(dir_path, f)
            if os.path.isfile(f):
                print f
                if 'pdf' in f:
                    to_process.append(f)
    else:
        to_process.append(dir_path)

    for f in to_process:
        readfile(f)
