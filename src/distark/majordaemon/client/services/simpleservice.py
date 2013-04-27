#encoding: utf-8
'''
Created on 25 avr. 2013

@author: guillaume
'''


from distark.commons.protos.generic_service_pb2 import SIMPLE_REQUEST
from distark.commons.protos.generic_service_pb2 import SIMPLE_RESPONSE
from distark.majordaemon.client.transport.distarkcli import Distarkcli

class SimpleRequest():

    __youpla=''

    def getYoupla(self):
        return self.__youpla


    def setYoupla(self, value):
        self.__youpla = value
        
    #IN: OneRequest
    def fillinPBOneRequest(self,pbonereq):
        pbonereq.rtype=SIMPLE_REQUEST
        pbonereq.simplereq.youpla=self.__youpla

    youpla = property(getYoupla, setYoupla, None, None)
    

class SimpleResponse():

    __boum=''

    #IN: OneResponse
    def __init__(self,pboneresponse=None):
        #TODO: test rtype
        
        if pboneresponse:
            if pboneresponse.rtype == SIMPLE_RESPONSE:
                self.__boum=pboneresponse.simpleresp.boum
            else:
                raise Exception('Wrong response Type received !')

    def getBoum(self):
        return self.__boum


    def setBoum(self, value):
        self.__boum = value

    boum = property(getBoum, setBoum, None, None)

class SimpleService(Distarkcli):
    '''
    Objectif: faire la requete à la construction
    la classe vit sa vie
    getReply renvoie la reponse si elle est arrivée
    '''

    associated_pb_response=SIMPLE_RESPONSE
    
    def __init__(self,simplerequest):
        self.objreq=simplerequest
        self.pbresptype=self.associated_pb_response
        self.pbrespHandler=SimpleResponse
        self.serviceName='SimpleService'
        self.send()        
  
    

    




        

    


        