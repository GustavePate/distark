# encoding: utf-8
'''
Created on 24 avr. 2013

@author: guillaume
'''

from distarkcli.protos.services.simple_service_pb2 import PBSimpleRequest
from distarkcli.protos.services.simple_service_pb2 import PBSimpleResponse
from distarkcli.protos.generic_service_pb2 import SIMPLE_RESPONSE
from distarkcli.protos.generic_service_pb2 import PBOneResponse
from distarkcli.protos.generic_service_pb2 import ERROR_NONE
from distarkcli.protos.generic_service_pb2 import ERROR_REQUEST_HANDLER
from distark.majordaemon.worker.utils import error_response
import traceback


class SimpleProcessor(object):
    '''
    classdocs
    '''
    req = PBSimpleRequest()
    resp = PBSimpleResponse()

    def __init__(self, req):
        '''
        Constructor
        '''
        self.req = PBSimpleRequest()
        self.resp = PBSimpleResponse()
        self.req = req

    def process(self, simpleresp):
        simpleresp.boum = ''.join(reversed(self.req.youpla))


    # IN: PBOneRequest
    # OUT: PBOneResponse
def simple_request_handler(oreq):

    oresp = PBOneResponse()
    try:
        pbsimplereq = oreq.simplereq
        processor = SimpleProcessor(pbsimplereq)

        oresp.rtype = SIMPLE_RESPONSE
        processor.process(oresp.simpleresp)
        # a partir de la si il y a une erreur elle est fonctionnelle
        oresp.etype = ERROR_NONE

    except Exception:
        print "simple_request: ", Exception
        traceback.print_exc()
        oresp = error_response(ERROR_REQUEST_HANDLER)
    finally:
        return oresp
