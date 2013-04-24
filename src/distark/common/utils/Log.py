'''
Created on 26 mars 2013

@author: guillaume
'''

from logging import Logger

class Log(object):
    '''
    classdocs
    '''

    logger=Logger()
    
    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def setLogger(self,logger):
        self.logger=logger
        
    def info(self,text):
        print text
        self.logger.info(text)
        