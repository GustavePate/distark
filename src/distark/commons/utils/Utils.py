#encoding: utf-8

'''
Created on 26 mars 2013

@author: guillaume
'''
import urllib
import gc
import urllib2
import os
import subprocess
import logging


class Singleton1():

    #### begin: make it a singeton
    instance = None

    def __new__(cls, *args, **kargs):
        if not cls._instance:
            cls.instance = object.__new__(cls, *args, **kargs)
        return cls.instance
    #### end: make it a singeton

    def __init__(self, maxconnection=10):
        print "INIT SINGLETON1"


class Singleton2(object):
    instance = None  # Attribut statique de classe

    def __new__(laClasse):
        "méthode de construction standard en Python"
        if laClasse.instance is None:
            laClasse.instance = object.__new__(laClasse)
        return laClasse.instance

    def __init__(self, maxconnection=10):
        print "INIT SINGLETON2"


# Singleton/ClassVariableSingleton.py
class SingleTone(object):
    __instance = None

    def __new__(cls, val):
        if SingleTone.__instance is None:
            SingleTone.__instance = object.__new__(cls)
        SingleTone.__instance.val = val
        return SingleTone.__instance


class Borg:
    __shared_state = {}  # variable de classe contenant l'état à partage

    def __init__(self):
        # copie de l'état lors de l'initialisation d'une nouvelle instance
        self.__dict__ = self.__shared_state
    _i=0

    def inc(self):
        self._i+=1

    def __str__(self):
        return str(self._i)

if __name__ == '__main__':
    sing1=Singleton1()
    sing2=Singleton1()
    print 'sing1', sing1
    print 'sing2', sing2
    # Utilisation
    sing1 = Singleton2()
    sing2 = Singleton2()

    print 'sing1', sing1
    print 'sing2', sing2
    # monSingleton1 et monSingleton2 renvoient à la même instance
    assert sing1 is sing2

    b1=Borg()
    b1.inc()
    print 'b1', b1
    b2=Borg()
    print 'b2', b2
    b2.inc()
    b2.inc()
    b2.inc()
    b2.inc()
    print 'b1', b1
    assert str(b1) == str(b2)

    # Utilisation
    sing1 = SingleTone(1)
    sing2 = SingleTone(2)
    print 'sing1', sing1
    print 'sing2', sing2
    # monSingleton1 et monSingleton2 renvoient à la même instance
    assert sing1 is sing2


def singleton(cls):
    instances = {}

    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]

    return getinstance


@singleton
class Singleton4(object):
    i=0

    def inc(self):
        self.i+=1

sing1=Singleton4()
sing2=Singleton4()
sing1.inc()
print sing1
print sing2


class Utils(object):
    '''
    classdocs
    '''

    def wgetreporthook(self, a, b, c):
        #print "% 3.1f%% of %d bytes\r" % (min(100, float(a * b) / c * 100), c)
        pass

    def wget(self, url, label):
        i = url.rfind('/')
        filename = label + url[i + 1:]
        print 'Download ', url, ' to ', filename
        urllib.urlretrieve(url, str(filename), self.wgetreporthook)
        return filename

    def sort(self, inputfile, outputfile):
        return subprocess.check_call('sort ' + inputfile + ' > ' + outputfile,
                                     shell=True)

    def grep(self, inputfile, outputfile, pattern):
        cmd="grep '" + pattern + "' " + inputfile + " > " + outputfile
        #print cmd
        return subprocess.check_call(cmd, shell=True)

    def downloadexample(self, filename):
        """ Get a python logo image for this example """
        if not os.path.exists(filename):
            response = urllib2.urlopen(
                'http://www.python.org/community/logos/python-logo.png')
            f = open(filename, 'w')
            f.write(response.read())
            f.close()

    def __init__(self):
        '''
        Constructor
        '''
    def dump_garbage(self):
        """
        show us what's the garbage about
        """
        # force collection
        print "GARBAGE:"
        gc.collect()
        print "GARBAGE OBJECTS:"
        for x in gc.garbage:
            s = str(x)
            if len(s) > 80:
                s = s[:80]
            print type(x), "\n  ", s

    def loggers(self):
        ##############################################
        #     INIT LOGGERS
        ##############################################

        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                            datefmt='%m-%d %H:%M',
                            filename='monitorParser.log',
                            filemode='w')

        # define a Handler which writes INFO messages
        #or higher to the sys.stderr
        console = logging.StreamHandler()
        console.setLevel(logging.DEBUG)

        # set a format which is simpler for console use
        formatter = logging.Formatter('%(levelname)-2s %(message)s')
        # tell the handler to use this format
        console.setFormatter(formatter)
        # add the handler to the root logger
        logging.getLogger('').addHandler(console)
        logging.info("Mon message info")
