#encoding: utf-8
"""
Majordomo Protocol client example. Uses the mdcli API to hide all MDP aspects

Author : Min RK <benjaminrk@gmail.com>

"""
import datetime
import sys
from distark.majordaemon.client.mdcliapi import MajorDomoClient 
from distark.majordaemon.commons.ZMQUtils import ZMQUtils

from distark.commons.protos.generic_service_pb2 import PBOneRequest, PBOneResponse
from distark.commons.protos.generic_service_pb2 import SIMPLE_REQUEST
from distark.commons.protos.generic_service_pb2 import SIMPLE_RESPONSE
from distark.commons.protos.generic_service_pb2 import ERROR_NONE
from distark.commons.protos.generic_service_pb2 import ERROR_PARSING_EXCEPTION
from distark.commons.protos.generic_service_pb2 import ERROR_INVALID_ENVELOP 
from distark.commons.protos.generic_service_pb2 import ERROR_UNKNOWN_SERVICE
from distark.commons.protos.generic_service_pb2 import ERROR_UNSUPPORTED_SERVICE
from distark.commons.protos.generic_service_pb2 import TECHNICAL_ERROR_RESPONSE
from distark.commons.protos.generic_service_pb2 import PRIORITY_STD
from distark.commons.protos.generic_service_pb2 import PBGenericRequest, PBGenericResponse
from distark.commons.protos.services.simple_service_pb2 import PBSimpleRequest, PBSimpleResponse

from distark.commons.utils.NetInfo import NetInfo 

my_ip=NetInfo.getIPString()
NB_REQUEST=10

#TODO: create a handler in separate file for each request/reply pair 
#TODO: the handler should take care of transport and serialisation/deserialisation to be used as an API


def simple_request(youpla): 
    
    #instanciate a SimpleRequest
    oreq=PBOneRequest()
    oreq.rtype=SIMPLE_REQUEST
    oreq.simplereq.youpla=youpla
    oreq.greq.servicename='SIMPLE_REQUEST'
    oreq.greq.caller='me_the_client'
    oreq.greq.ipadress=my_ip
    oreq.greq.priority=PRIORITY_STD
    res=oreq.SerializeToString()
    return [res]
    

def simple_response(oresp):
    print "received: ",oresp.simpleresp.boum
    pass


def super_simple_request(youpla): 
    
    #instanciate a SimpleRequest
    oreq=PBSimpleRequest()
    oreq.youpla=youpla
    res=oreq.SerializeToString()
    return [res]
    

def super_simple_response(oresp):
    print "received: ",oresp.boum
    pass


def retryNtimes(oresp):
    #TODO: implement    
    if oresp.rtype == TECHNICAL_ERROR_RESPONSE:
    
        if oresp.etype == ERROR_NONE:
            print "None error /ResponseType:",oresp.rtype," ErroType:",oresp.etype
        elif oresp.etype == ERROR_PARSING_EXCEPTION:
            print "Parsing error /ResponseType:",oresp.rtype," ErroType:",oresp.etype
        elif oresp.etype == ERROR_INVALID_ENVELOP:
            print "Invalid Envelop error /ResponseType:",oresp.rtype," ErroType:",oresp.etype
        elif oresp.etype == ERROR_UNKNOWN_SERVICE:
            print "Unknown service error /ResponseType:",oresp.rtype," ErroType:",oresp.etype
        elif oresp.etype == ERROR_UNSUPPORTED_SERVICE:
            print "Unsupported error /ResponseType:",oresp.rtype," ErroType:",oresp.etype
        else:
            print "Unknown error /ResponseType:",oresp.rtype," ErroType:",oresp.etype
    else:
        raise Exception("should be a technical error here")

def handle_response(oresp):
    
    existing_response = {
                         SIMPLE_RESPONSE: simple_response,
                         TECHNICAL_ERROR_RESPONSE: retryNtimes,
                         }

    
    #do the job
    if oresp.rtype in existing_response.keys():
        oresp=existing_response[oresp.rtype](oresp)
    else:
        
        
        
        
        oresp.type=ERROR_UNKNOWN_SERVICE
        print "Unknown response type", oresp.rtype
        
def deserialize():
    pass


def main():
    
    start_launcher=datetime.datetime.now()
    
    verbose = '-v' in sys.argv
    client = MajorDomoClient("tcp://localhost:5555", verbose)
    requests = NB_REQUEST
    for _ in xrange(requests):
        request = "Hello world"
        try:
            #request=super_simple_request('youpi')
            request=simple_request('youpi')
            client.send("echo", request)
            if verbose:
                print 'request sended:',request
        except KeyboardInterrupt:
            print "send interrupted, aborting"
            return

    count = 0
    while count < requests:
        try:
            reply = client.recv()
        except KeyboardInterrupt:
            break
        else:
            # also break on failure to reply:
            if reply is None:
                break
            else:
                #check if my reponse is a list of one
                if ZMQUtils.is_valid_envelop(reply):
                    #then
                    sresp=PBOneResponse()
                    sresp.ParseFromString(reply[0])    
                    handle_response(sresp)
                else:
                    print "received invalid response envelop"
            
            
        count += 1
    print "%i requests/replies processed" % count
    
    end_launcher=datetime.datetime.now()

    delta=end_launcher-start_launcher
    print('Launcher ALL JOBS DONE  in '+str(delta)+' !!!!')    
    

if __name__ == '__main__':
    main()
