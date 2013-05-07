# encoding: utf-8
'''
Created on 24 avr. 2013

@author: guillaume
'''

from distark.commons.protos.services.another_service_pb2 import PBAnotherRequest
from distark.commons.protos.services.another_service_pb2 import PBAnotherResponse
from distark.commons.protos.generic_service_pb2 import ANOTHER_RESPONSE
from distark.commons.protos.generic_service_pb2 import PBOneResponse
from distark.commons.protos.generic_service_pb2 import ERROR_NONE
from distark.commons.protos.generic_service_pb2 import ERROR_REQUEST_HANDLER
from distark.majordaemon.worker.utils import error_response
import traceback


class AnotherProcessor(object):
    '''
    classdocs
    '''
    req = PBAnotherRequest()
    resp = PBAnotherResponse()

    def __init__(self, req):
        '''
        Constructor
        '''
        self.req = PBAnotherRequest()
        self.resp = PBAnotherResponse()
        self.req = req

    def process(self, pbanotherresp):
        pbanotherresp.response_str = ''.join([self.req.request_str, self.req.request_str])


# IN: PBOneRequest
# OUT: PBOneResponse
def another_request_handler(oreq):
    oresp = PBOneResponse()
    try:
        pbrealreq = oreq.anotherreq
        processor = AnotherProcessor(pbrealreq)

        oresp.rtype = ANOTHER_RESPONSE
        processor.process(oresp.anotherresp)
        # a partir de la si il y a une erreur elle est fonctionnelle
        oresp.etype = ERROR_NONE

    except Exception:
        print "another_request: ", Exception
        traceback.print_exc()
        oresp = error_response(ERROR_REQUEST_HANDLER)
    finally:
        return oresp
