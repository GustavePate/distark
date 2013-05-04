# encoding: utf-8
'''
Created on 24 avr. 2013

@author: guillaume
'''

from distark.commons.protos.services.simple_service_pb2 import PBSimpleRequest
from distark.commons.protos.services.simple_service_pb2 import PBSimpleResponse


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

    def process2(self, simpleresp):
        simpleresp.boum = ''.join(reversed(self.req.youpla))

    def process(self):
        self.resp.boum = ''.join(reversed(self.req.youpla))
        return self.resp
