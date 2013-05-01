'''
Created on 27 avr. 2013

@author: guillaume
'''

from distark.commons.protos.generic_service_pb2 import PBOneRequest, PBOneResponse

from distark.commons.utils.NetInfo import NetInfo 


from distark.majordaemon.client.transport.transportpool import StubSimpleRequestConnectionPool
from distark.majordaemon.client.transport.transportpool import NaiveConnectionPool
from distark.majordaemon.client.transport.transportpool import ConnectionPoolBorg
from time import sleep    


class Distarkcli(object):
    
    serviceName=''
    pbrespHandler=None
    pbresptype=None
    #__requestType=None
    objreq=None
    __pboreq=None
    
    __pboresp=None
    __connection=None
        
        
        
    #OUT: PBOnResponse
    def getResponse(self):
        while True:
            msg=self.__connection.recv()
            if isinstance(msg,list):
                if len(msg)==1:
                    msg=msg[0]
                else:
                    #multipart response whe can't handle
                    raise Exception('Distarkcli: multipart response received')
                    
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

        
        self.objreq.fillinPBOneRequest(self.__pboreq)
        #serialize
        msg=self.__pboreq.SerializeToString()
        #pool=StubSimpleRequestConnectionPool()
        #pool=NaiveConnectionPool()
        
        pool=ConnectionPoolBorg()
        self.__connection=pool.getConnection()
        #TODO: Fix this "echo" for appropriate service discovery 
        self.__connection.send("echo",msg)      
