'''
Created on 24 avr. 2013

@author: guillaume
'''

from distark.commons.protos.proto_services_pb2 import SimpleRequest, SimpleResponse

class SimpleProcessor(object):
    '''
    classdocs
    '''
    req=SimpleRequest()
    resq=SimpleResponse()

    def __init__(self,req):
        '''
        Constructor
        '''
        self.req=req
        
    def process(self):
        self.resp.boum=''.join(reversed(self.req.youpla))
        return self.resp
        
        
        