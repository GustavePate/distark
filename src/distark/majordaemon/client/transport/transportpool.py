'''
Created on 27 avr. 2013

@author: guillaume
'''

from distark.commons.protos.generic_service_pb2 import PBOneRequest, PBOneResponse
from distark.commons.protos.generic_service_pb2 import SIMPLE_RESPONSE
from distark.commons.protos.generic_service_pb2 import ERROR_NONE
from distark.majordaemon.commons.PBUtils import PBUtils

class TransportPool():
    
    def __init__(self):
        pass
    
    def get(self):
        pass


class SimpleRequestTransportStubPool():
    
    __oreq=None
    __oresp=None
    
    def get(self):
        return self
    
    def __init__(self):
        pass
    
    def send(self,msg):
        if msg:
            self.__oreq=PBOneRequest()
            self.__oreq.ParseFromString(msg)
            PBUtils.dumpOneRequest(self.__oreq)
    
    def recv(self):
        self.__oresp=None
        if self.__oreq:
            self.__oresp=PBOneResponse()
            self.__oresp.rtype=SIMPLE_RESPONSE
            self.__oresp.etype=ERROR_NONE
            self.__oresp.gresp.computetime=1.0
            self.__oresp.gresp.req.servicename=self.__oreq.greq.servicename
            self.__oresp.gresp.req.caller=self.__oreq.greq.caller
            self.__oresp.gresp.req.ipadress=self.__oreq.greq.ipadress
            
            self.__oresp.simpleresp.boum=''.join(reversed(self.__oreq.simplereq.youpla))
            PBUtils.dumpOneResponse(self.__oresp)
            res=self.__oresp.SerializeToString()
            return res