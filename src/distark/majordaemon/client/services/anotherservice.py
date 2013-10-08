#encoding: utf-8
'''
Created on 25 avr. 2013

@author: guillaume
'''
from distark.commons.protos.generic_service_pb2 import ANOTHER_REQUEST
from generic_service_pb2 import ANOTHER_RESPONSE
from distark.majordaemon.client.transport.distarkcli import Distarkcli


class AnotherRequest():

    __requeststr=''

    def getRequestStr(self):
        return self.__requeststr

    def setRequestStr(self, value):
        self.__requeststr= value

    #IN: OneRequest
    def fillinPBOneRequest(self, pbonereq):
        pbonereq.rtype=ANOTHER_REQUEST
        pbonereq.anotherreq.request_str =self.__requeststr


class AnotherResponse():

    __responsestr=''

    #IN: OneResponse
    def __init__(self, pboneresponse=None):
        if pboneresponse:
            if pboneresponse.rtype == ANOTHER_RESPONSE:
                self.__responsestr=pboneresponse.anotherresp.response_str
            else:
                raise Exception('Wrong response Type received !')

    def getResponseStr(self):
        return self.__responsestr

    def setResponseStr(self, value):
        self.__responsestr = value


class AnotherService(Distarkcli):
    '''
    Objectif: faire la requete à la construction
    la classe vit sa vie
    getReply renvoie la reponse si elle est arrivée
    '''

    pbresptype=ANOTHER_RESPONSE
    serviceName='AnotherService'
    pbrespHandler=AnotherResponse

    def __init__(self, anotherrequest):
        self.objreq=anotherrequest
        self.send()
