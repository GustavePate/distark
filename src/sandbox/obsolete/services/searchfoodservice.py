#encoding: utf-8
'''
Created on 25 avr. 2013

@author: guillaume
'''
from distark.commons.protos.generic_service_pb2 import SEARCH_FOOD_REQUEST
from distark.commons.protos.generic_service_pb2 import SEARCH_FOOD_RESPONSE
from distark.majordaemon.client.transport.distarkcli import Distarkcli


class SearchFoodRequest():

    __req_str=''

    def getReq(self):
        return self.__req_str

    def setReq(self, value):
        self.__req_str = value

    #IN: OneRequest
    def fillinPBOneRequest(self, pbonereq):
        pbonereq.rtype=SEARCH_FOOD_REQUEST
        pbonereq.searchfoodreq.request_food_str=self.__req_str


class SearchFoodResponse():

    __foods=''

    #IN: OneResponse
    def __init__(self, pboneresponse=None):
        if pboneresponse:
            if pboneresponse.rtype == SEARCH_FOOD_RESPONSE:
                self.__foods=pboneresponse.searchfoodresp.foods
            else:
                raise Exception('Wrong response Type received !')

    def getFoods(self):
        return self.__foods

    def setFoods(self, value):
        self.__foods = value


class SearchFoodService(Distarkcli):
    '''
    Objectif: faire la requete à la construction
    la classe vit sa vie
    getReply renvoie la reponse si elle est arrivée
    '''

    pbresptype=SEARCH_FOOD_RESPONSE
    serviceName='SearchFoodService'
    pbrespHandler=SearchFoodResponse

    def __init__(self, searchfoodrequest):
        self.objreq=searchfoodrequest
        self.send()
