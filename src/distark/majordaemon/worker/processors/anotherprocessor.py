# encoding: utf-8
'''
Created on 24 avr. 2013

@author: guillaume
'''

from distark.commons.protos.services.another_service_pb2 import PBAnotherRequest
from distark.commons.protos.services.another_service_pb2 import PBAnotherResponse


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
