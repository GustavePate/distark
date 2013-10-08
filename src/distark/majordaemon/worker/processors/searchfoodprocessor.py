# encoding: utf-8
'''
Created on 24 avr. 2013

@author: guillaume
'''

from distark.commons.protos.services.search_food_service_pb2 import PBSearchFoodRequest
from distark.commons.protos.services.search_food_service_pb2 import PBSearchFoodResponse
from distark.commons.protos.generic_service_pb2 import SEARCH_FOOD_RESPONSE
from distark.commons.protos.generic_service_pb2 import PBOneResponse
from distark.commons.protos.generic_service_pb2 import ERROR_NONE
from distark.commons.protos.generic_service_pb2 import ERROR_REQUEST_HANDLER
from distark.majordaemon.worker.utils import error_response
from distark.majordaemon.worker.objects.food import Food
from distark.commons.utils.db.mongopool import MongoPool
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
        self.req = PBSearchFoodRequest()
        self.resp = PBSearchFoodResponse()
        self.req = req

    def process(self, pbsearchfoodresp):
        mp = MongoPool()
        con = mp.getConnection()
        qryres = con.alim.find({'name':
                                {'$regex': '.*' + self.req.request_food_str
                                 + '.*',
                                 '$options': 'i'}
                                })
        nbres = qryres.count()
        if nbres > self.MAX_RESULTS:
            #add a warning in response
            pass

        if qryres.count() > 0:
            #build response of at more MAX_RESULT rec
            cpt = 1
            for r in qryres:
                #add rec to pbresponse
                f=Food(mongo=r)
                f.fillInPbSearchFood(pbsearchfoodresp)
                if cpt >= self.MAX_RESULTS:
                    break
                cpt+=1
        else:
            #return functional error ERROR_NO_RESULT
            #TODO: hashmap in protoc ?
            pass


# IN: PBOneRequest
# OUT: PBOneResponse
def search_food_request_handler(oreq):
    oresp = PBOneResponse()
    try:
        pbrealreq = oreq.searchfoodreq
        processor = SearchFoodProcessor(pbrealreq)

        oresp.rtype = SEARCH_FOOD_RESPONSE
        oresp.etype = ERROR_NONE
        # a partir de la si il y a une erreur elle est fonctionnelle
        processor.process(oresp.searchfoodresp)

    except Exception:
        print "SearchFood_request: ", Exception
        traceback.print_exc()
        oresp = error_response(ERROR_REQUEST_HANDLER)
    finally:
        return oresp
