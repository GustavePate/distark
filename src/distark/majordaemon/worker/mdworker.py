#encoding: utf-8

"""Majordomo Protocol worker example.

Uses the mdwrk API to hide all MDP aspects

Author: Min RK <benjaminrk@gmail.com>
"""

import sys
import datetime
import traceback
from distark.majordaemon.worker.mdwrkapi import MajorDomoWorker
from distark.commons.protos.generic_service_pb2 import PBOneRequest, PBOneResponse
from distark.commons.protos.generic_service_pb2 import SIMPLE_REQUEST
from distark.commons.protos.generic_service_pb2 import SIMPLE_RESPONSE
from distark.commons.protos.generic_service_pb2 import TECHNICAL_ERROR_RESPONSE 
from distark.commons.protos.generic_service_pb2 import ERROR_UNKNOWN_SERVICE
from distark.commons.protos.generic_service_pb2 import ERROR_PARSING_EXCEPTION 
from distark.commons.protos.generic_service_pb2 import ERROR_INVALID_ENVELOP
from distark.commons.protos.generic_service_pb2 import ERROR_NONE
from distark.commons.protos.generic_service_pb2 import PBGenericRequest, PBGenericResponse
from distark.commons.protos.services.simple_service_pb2 import PBSimpleRequest, PBSimpleResponse

from distark.majordaemon.commons.ZMQUtils import ZMQUtils
from distark.majordaemon.worker.processors.SimpleProcessor import SimpleProcessor

from distark.commons.utils.NetInfo import NetInfo


my_ip=''
start_working=0
end_working=0
verbose=False
services=[]

#IN: PBOneRequest
#OUT: PBOneResponse

def simple_request(oreq):
    if verbose:
        print "Work on: Simple Request"
        
    try:
        pbsimplereq=oreq.simplereq
        processor=SimpleProcessor(pbsimplereq)
        oresp=PBOneResponse()
        oresp.rtype=SIMPLE_RESPONSE
        processor.process2(oresp.simpleresp)
        return oresp

    except Exception:
        print "simple_request: ",Exception
        traceback.print_exc()

#IN: OneReponse, OneRequest
#OUT: nothing
def fillOneResponseGenericFields(oresp,oreq):
    oresp.gresp.req.servicename=oreq.greq.servicename
    oresp.gresp.req.caller=oreq.greq.caller
    oresp.gresp.req.ipadress=oreq.greq.ipadress
    oresp.gresp.server_ipadress=my_ip

    
    
    

#IN: PBOneRequest
#OUT: PBOneResponse
def handle_request(oreq):
    
    
    existing_services = {
                         SIMPLE_REQUEST: simple_request,
                         }
    #prepare response
    oresp=PBOneResponse()
    
    #do the job
    if oreq.rtype in existing_services.keys():
        #TODO: switch case pattern doesn't work
        #oresp=existing_services[oreq.rtype](oreq)
        oresp=simple_request(oreq)
        oresp.etype=ERROR_NONE
    else:
        oresp=error_response(ERROR_UNKNOWN_SERVICE)
        print "dispatch: Unknown service:", oreq.rtype
        
    #Fill in Generic Response
    fillOneResponseGenericFields(oresp,oreq)
    
    return oresp
    
    
def error_response(type):
    oresp=PBOneResponse() 
    oresp.rtype=TECHNICAL_ERROR_RESPONSE
    oresp.etype=type
    oresp.gresp.req.servicename='idontknow'
    oresp.gresp.req.caller='idontknow'
    oresp.gresp.computetime=-1.0
    oresp.gresp.server_ipadress=my_ip
    res=oresp.SerializeToString()  
    return res  

#IN: ZMQEnvelop
#OUT: string
# if deserialize a success: handle
# else reply protobuf OneResponse error
def deserialize_and_reply(request,verbose):

    start_working=datetime.datetime.now()
    
    if not ZMQUtils.is_valid_envelop(request):
        print 'Invalid Request:', TypeError 
        res=error_response(ERROR_INVALID_ENVELOP)
    else:
        if verbose:
            print "raw_request",request
        pboreq=PBOneRequest()
        res=''
        try:
            pboreq = PBOneRequest()
            pboreq.ParseFromString(request[0])
            pboresp=handle_request(pboreq)
            end_working=datetime.datetime.now()
            delta=end_working-start_working   
            pboresp.gresp.computetime=delta.total_seconds()
            res=pboresp.SerializeToString()
        except TypeError:
            print 'Exception:', TypeError 
            traceback.print_exc()
            res=error_response(ERROR_PARSING_EXCEPTION)
        except Exception:
            print 'General Exception:',  Exception
            traceback.print_exc()
            res=error_response(ERROR_PARSING_EXCEPTION)
        finally:
            if verbose:
                print 'raw_reply:',res
            return [res]





def main():
    verbose = '-v' in sys.argv
    
    my_ip=NetInfo.getIPString()
    
    worker = MajorDomoWorker("tcp://localhost:5555", "echo", verbose)
    reply = None
    while True:
        request = worker.recv(reply)
        if request is None:
            print "Have to quit, bye !"
            break # Worker was interrupted
        
        ### Reply Must be in a list !!!!!!
        reply = deserialize_and_reply(request,verbose) # Echo is complex... :-)
        
        


if __name__ == '__main__':
    main()
