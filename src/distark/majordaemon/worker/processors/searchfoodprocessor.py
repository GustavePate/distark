# encoding: utf-8
'''
Created on 24 avr. 2013

@author: guillaume
'''

from distarkcli.protos.services.search_food_service_pb2 import PBSearchFoodRequest
from distarkcli.protos.services.search_food_service_pb2 import PBSearchFoodResponse
from distarkcli.protos.services.search_food_service_pb2 import ERROR_NONE as PBSFOOD_ERROR_NONE
from distarkcli.protos.services.search_food_service_pb2 import ERROR_NO_RESULT as PBSFOOD_ERROR_NO_RESULT
from distarkcli.protos.services.search_food_service_pb2 import ERROR_OTHER as PBSFOOD_ERROR_OTHER
from distarkcli.protos.generic_service_pb2 import SEARCH_FOOD_RESPONSE
from distarkcli.protos.generic_service_pb2 import PBOneResponse
from distarkcli.protos.generic_service_pb2 import ERROR_NONE
from distarkcli.protos.generic_service_pb2 import ERROR_REQUEST_HANDLER
from distark.majordaemon.worker.utils import error_response
from distark.majordaemon.worker.objects.food import Food
from distark.majordaemon.worker.dao.FoodDAO import FoodDAOFactory, FoodDAO
import traceback


class SearchFoodProcessor(object):
    '''
    classdocs
    '''
    req = PBSearchFoodRequest()
    resp = PBSearchFoodResponse()
    MAX_RESULTS = 8

    def __init__(self, req):
        '''
        Constructor
        '''
        self.resp = PBSearchFoodResponse()
        self.req = req

    def analyseinput(self):
        #Throw BADINPUTPARAMETERS Exception
        if self.req.request_food_str == '' or not(self.req.request_food_str):
            raise(Exception("SearchFoodResponse: bad parameters"))

    def process(self, pbsearchfoodresp):
        try:

            #fooddao = FoodDAO()  # completion
            fooddao = FoodDAOFactory()
            fooddaolist = fooddao.searchFoodByPattern(self.req.request_food_str)
            cpt = 0
            pbsearchfoodresp.func_error_code = PBSFOOD_ERROR_NONE

            if len(fooddaolist) == 0:
                pbsearchfoodresp.func_error_code = PBSFOOD_ERROR_NO_RESULT

            for fdao in fooddaolist:
                f = Food(fdao)
                f.fillInPbSearchFoodResponse(pbsearchfoodresp)
                if cpt >= self.MAX_RESULTS:
                    pbsearchfoodresp.func_error_code = PBSFOOD_ERROR_OTHER
                    #return functional error ERROR_TOO_MUCH_RESULT
                    #TODO: hashmap in protoc ?
                    break
                cpt += 1

        except:
            print traceback.format_exc()
            pbsearchfoodresp.func_error_code = PBSFOOD_ERROR_OTHER
            raise Exception("SearchFood: Unexpected exception")


# IN: PBOneRequest
# OUT: PBOneResponse
def search_food_request_handler(oreq):
    oresp = PBOneResponse()
    try:
        pbrealreq = oreq.searchfoodreq
        processor = SearchFoodProcessor(pbrealreq)

        oresp.etype = ERROR_NONE
        oresp.rtype = SEARCH_FOOD_RESPONSE
        # a partir de la si il y a une erreur elle est fonctionnelle
        processor.process(oresp.searchfoodresp)

    except:
        traceback.print_exc()
        oresp = error_response(ERROR_REQUEST_HANDLER)
    finally:
        return oresp
