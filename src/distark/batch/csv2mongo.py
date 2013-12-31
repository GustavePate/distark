# encoding: utf-8
import argparse
import traceback

import codecs
import re

from distark.majordaemon.worker.db.mongopool import MongoPool
from distarkcli.utils.MyConfiguration import Configuration


#TODO: pass the configuration by command line
MAX_CONN = 1
host = Configuration.getworker()['mongo']['host']
port = Configuration.getworker()['mongo']['port']
db = Configuration.getworker()['mongo']['db']
mp = MongoPool(host, port, db, MAX_CONN)
refloat = re.compile('^\d+(\.\d+)*$')


def is_valid_qte(line):
    res = False
    qte = [u'100 g', u'1 part', u'1 pot', u'1 unité', u'1 tranche',
           u'1 portion', u'100 ml', u'1 canette', u'c.c.']
    if line in qte:
        res = True

    return res


def store_data(datadic):

    #store in db
    mp.insert("food.fooddb", datadic)


def analyse_line(line):

    valid = False

    #cut line
    rec = {}
    data = line.split(";")

    if len(data) != 6:
        valid = False
    else:
        rec['name_fr'] = data[0].strip()
        rec['cal'] = data[1].strip()
        rec['pro'] = data[2].strip()
        rec['glu'] = data[3].strip()
        rec['lip'] = data[4].strip()
        rec['qty'] = data[5].strip()
        valid = True

    #no ; in name
    # check invalid characters in name
    if valid:
        if ';' in rec["name_fr"]:
            valid = False

    #glu, pro, lip, cal are numbers
    if valid:
        try:
            rec['cal'] = float(rec['cal'])
            rec['pro'] = float(rec['pro'])
            rec['glu'] = float(rec['glu'])
            rec['lip'] = float(rec['lip'])
        except:
            valid = False

    #qty is in accepted domain
    if valid:
        valid = is_valid_qte(rec['qty'])

    if valid:
        return rec
    else:
        return None


def reject(file, line):
    if file:
        f = codecs.open(file, "a", "utf-8")
        print "Rejected: " + line
        f.write(line)
        f.close
    else:
        print "Rejected: " + line


#csv format
# nam;cal;prot;glu;lip;qty
def main(input, rejectfile):

    #open data file
    f = codecs.open(input, "r", "utf-8")
    for l in f:
        to_store = analyse_line(l)
        if to_store:
            store_data(to_store)
        else:
            reject(rejectfile, l)
    f.close()

if __name__ == '__main__':
    ##############################################
    #     ARGUMENTS PARSING
    ##############################################
    try:
        parser = argparse.ArgumentParser(description='Load csv into mongo')
        parser.add_argument(
            '-f', '--file', help='data to load', type=str)
        parser.add_argument(
            '-r', '--reject', help='rejected data filename', type=str)
        args = parser.parse_args()
        print "Program Launched with args:" + str(args)

        if args.file:
            main(args.file, args.reject)
        else:
            print 'do nothing !!!'

    except:
        traceback.print_exc()

    finally:
        print "Done !"
