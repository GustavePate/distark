'''
Created on 6 mai 2013

@author: guillaume
'''

from distark.commons.protos.generic_service_pb2 import PBOneResponse
from distark.commons.protos.generic_service_pb2 import TECHNICAL_ERROR_RESPONSE
from distarkcli.utils.NetInfo import NetInfo


def error_response(etype):
    oresp = PBOneResponse()
    oresp.rtype = TECHNICAL_ERROR_RESPONSE
    oresp.etype = type
    oresp.gresp.req.servicename = 'idontknow'
    oresp.gresp.req.caller = 'idontknow'
    oresp.gresp.computetime = -1.0
    oresp.gresp.server_ipadress = NetInfo.getIPString()
    res = oresp.SerializeToString()
    return res
