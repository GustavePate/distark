'''
Created on 26 mars 2013

@author: guillaume
'''

import gc
import urllib2
import os
import urllib
import subprocess
import logging

class Utils(object):
    '''
    classdocs
    '''


    def wgetreporthook(self,a,b,c): 
        #print "% 3.1f%% of %d bytes\r" % (min(100, float(a * b) / c * 100), c),
        pass

    def wget(self,url,label):
        i = url.rfind('/')
        filename = label+url[i+1:]
        print 'Download ',url, ' to ', filename
        urllib.urlretrieve(url, str(filename), self.wgetreporthook)
        return filename
    
    def sort(self,inputfile,outputfile):
        return subprocess.check_call('sort '+inputfile+' > '+outputfile,shell=True)
    
    def grep(self,inputfile,outputfile,pattern):
        cmd="grep '"+pattern+"' "+inputfile+" > "+outputfile
        #print cmd
        return subprocess.check_call(cmd,shell=True)
    
    
    def downloadexample(self,filename):
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
            if len(s) > 80: s = s[:80]
            print type(x),"\n  ", s
            
    def loggers(self):
        ##############################################
        #     INIT LOGGERS
        ##############################################
        
        logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                        datefmt='%m-%d %H:%M',
                        filename='monitorParser.log',
                        filemode='w')
    
        # define a Handler which writes INFO messages or higher to the sys.stderr
        console = logging.StreamHandler()
        console.setLevel(logging.DEBUG)
    
        # set a format which is simpler for console use
        formatter = logging.Formatter('%(levelname)-2s %(message)s')
        # tell the handler to use this format
        console.setFormatter(formatter)
        # add the handler to the root logger
        logging.getLogger('').addHandler(console)
        logging.info("Mon message info")
        