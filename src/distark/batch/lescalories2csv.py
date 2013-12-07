# -*- coding: utf-8 -*-
import urllib2
import argparse
import traceback
from bs4 import BeautifulSoup
import codecs

items = []


############# RETRIEVE #################
def tags2csv(tags):

    for t in tags:
        item = {}
        item["name"] = unicode(t.contents[1].span.a.string)
        #item["name"] = type(t.contents[1].span.a.string)
        item["cal"] = unicode(t.contents[3].span.string)
        item["prot"] = unicode(t.contents[5].span.string)
        item["glu"] = unicode(t.contents[7].span.string)
        item["lip"] = unicode(t.contents[9].span.string)
        item["qty"] = unicode(t.contents[11].span.string)

        if ";" in item["name"]:
            item["name"] = item["name"].replace(u";", ",")

        items.append(item)


def dumpcsv(file):
    if file:
        f = codecs.open(file, "w", "utf-8")
        for i in items:
            res = i["name"] + ";" + i["cal"] + ";" + i["prot"] + ";" + i["glu"] + ";" + i["lip"] + ";" + i["qty"]
            f.write(res + "\n")
            print res
        f.close()
    else:
        for i in items:
            res = i["name"] + ";" + i["cal"] + ";" + i["prot"] + ";" + i["glu"] + ";" + i["lip"] + ";" + i["qty"]
            print res



def main(file, url, output):

    if file:
        page = open(file)
    elif url:
        page = urllib2.urlopen(url)

    soup = BeautifulSoup(page)
    #x = soup.body.tr
    tags = soup.select('tr[bgcolor="#96C56F"]')
    tags2csv(tags)
    tags = soup.select('tr[bgcolor="#999999"]')
    tags2csv(tags)
    dumpcsv(output)
    #x = soup.body.find('div', attrs={'class': 'container'}).text




if __name__ == '__main__':
    ##############################################
    #     ARGUMENTS PARSING
    ##############################################
    try:
        parser = argparse.ArgumentParser(description='Parse html and generate csv')
        parser.add_argument(
            '-f', '--file', help='page to parse', type=str)
        parser.add_argument(
            '-u', '--url', help='url to parse', type=str)
        parser.add_argument(
            '-o', '--output', help='csv file name', type=str)
        args = parser.parse_args()
        print "Program Launched with args:" + str(args)

        if args.file:
            main(args.file, None, args.output)
        elif args.url:
            main(None, args.url, args.output)
        else:
            print 'do nothing !!!'

    except:
        traceback.print_exc()

    finally:
        print "Done !"
