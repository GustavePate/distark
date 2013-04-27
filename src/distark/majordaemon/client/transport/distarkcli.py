'''
Created on 27 avr. 2013

@author: guillaume
'''

from distark.commons.protos.generic_service_pb2 import PBOneRequest, PBOneResponse

from distark.commons.utils.NetInfo import NetInfo 


from distark.majordaemon.client.transport.transportpool import SimpleRequestTransportStubPool
from distark.majordaemon.client.transport.transportpool import TransportPool
from time import sleep    


class Distarkcli(object):
    
    serviceName=''
    pbrespHandler=None
    pbresptype=None
    #__requestType=None
    objreq=None
    __pboreq=None
    
    __pboresp=None
    __transport=SimpleRequestTransportStubPool().get()    
        
#     #IN: a non list serialized pbmessage 
#     def __pbresponsehandler(self,pbmessage):
#         #deserialize
#         pbresponse=self.__responsetype().ParseFromString(pbmessage)
#         #set reply
#         self.__reply=self.__responsetype(pbresponse)
            
        
    #OUT: PBOnResponse
    def getResponse(self):
        while True:
            msg=self.__transport.recv()
            if msg:
                self.__pboresp=PBOneResponse()
                self.__pboresp.ParseFromString(msg)
                #soit une reponse au service, soit une erreur
                if (self.__pboresp.rtype == self.pbresptype):
                    return [self.__pboresp.rtype,self.pbrespHandler(self.__pboresp)]
                else:
                    return [self.__pboresp.rtype,self.__pboresp]
                    
            #sleep 1 ms
            sleep(0.001)  
            
    def fillinGenericRequest(self):
        self.__pboreq.greq.servicename=self.serviceName
        self.__pboreq.greq.caller='Distarkcli'
        self.__pboreq.greq.ipadress=NetInfo.getIPString() 
            
    def send(self):
        
        #prepare OneRequest
        self.__pboreq=PBOneRequest() 
        self.fillinGenericRequest()
        print self.objreq
        self.objreq.fillinPBOneRequest(self.__pboreq)
        #serialize
        msg=self.__pboreq.SerializeToString()
        self.__transport.send(msg)      
    