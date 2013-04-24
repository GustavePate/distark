#encoding: utf-8
'''
Created on 11 oct. 2012

@author: guillaume
'''

from yaml import load, Loader
import os

class Configuration(object):

    
    logger=''
    initialized=False
    settings={}
    

    def __init__(self,confpath=None):
        '''
        Constructor
        '''
        f=None
        if confpath != None:
            try:
                print "Configuration Loaded from:",confpath
                f=open(confpath,'r')
                Configuration.settings=load(f, Loader=Loader)
                Configuration.initialized=True
            finally:
                if f!=None:
                    f.close()
        else: 
            try:
                confpath=Configuration.getConfigPath(__file__)
                print "Configuration Loaded from:",confpath
                f=open(confpath,'r')
                Configuration.settings=load(f, Loader=Loader)
                Configuration.initialized=True
            finally:
                if f!=None:
                    f.close()


        self.initialized=True
        self.settings = Configuration.settings
            
                
                
    def get(self):
        return self.settings
        
    @staticmethod
    def getInit():
        return Configuration.initialized
    
    @staticmethod
    def getLogger():
        return Configuration.logger

    @staticmethod
    def getConfigPath(underscored_file):
        pathelements=underscored_file.split("/")
        index=pathelements.index("src")
        basepath=pathelements[:index]
        res="/"
        for e in basepath:
            res=os.path.join(res,e)
        confpath=os.path.join(res,'ressources/common/conf/configuration.yaml')
        return confpath
