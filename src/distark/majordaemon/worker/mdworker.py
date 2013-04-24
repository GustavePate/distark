#encoding: utf-8

"""Majordomo Protocol worker example.

Uses the mdwrk API to hide all MDP aspects

Author: Min RK <benjaminrk@gmail.com>
"""

import sys
import datetime
from mdwrkapi import MajorDomoWorker
from distark.commons.protos.proto_services_pb2 import OneRequest, OneResponse
from distark.commons.protos.proto_services_pb2 import FOO
from distark.commons.protos.proto_services_pb2 import SIMPLE_REQUEST
from distark.commons.protos.proto_services_pb2 import SIMPLE_RESPONSE
from distark.commons.protos.proto_services_pb2 import ERROR_UNKNOWN_SERVICE 
from distark.commons.protos.proto_services_pb2 import ERROR_PARSING_EXCEPTION 
from distark.commons.protos.proto_services_pb2 import GenericRequest, GenericResponse
from distark.commons.protos.proto_services_pb2 import SimpleRequest, SimpleResponse
from distark.majordaemon.worker.processors.SimpleProcessor import SimpleProcessor

from distark.commons.utils.NetInfo import NetInfo


my_ip=''
start_working=0
end_working=0
verbose=False
services=[]

def simple_request(oreq):
    if verbose:
        print "Work on: Simple Request"
    req=oreq.simplereq
    processor=SimpleProcessor(req)
    oresp=OneResponse()
    oresp.type=SIMPLE_RESPONSE
    oresp.simpleresp=processor.process()
    return oresp

def foo(oreq):
    if verbose:    
        print "Work on: Foo"


def dispatch(oreq):
    
    
    existing_services = {
                         SIMPLE_REQUEST: simple_request,
                         FOO : foo,
                         }
    #prepare response
    oresp=OneResponse()
    
    #do the job
    if oreq.type in existing_services.keys():
        oresp=existing_services[oreq.type](oreq)
    else:
        oresp.type=ERROR_UNKNOWN_SERVICE
        print "Unknown service:", oreq.type
        
    #Fill in Generic Response
    oresp.gresp.req=oreq
    oresp.gresp.server_ipadress=my_ip
    
    end_working=datetime.datetime.now()
    delta=end_working-start_working   
    oresp.gresp.computetime=delta.total_seconds()
    
    return oresp
    
    
 

def handle_request(message,verbose):

    
    start_working=datetime.datetime.now()
    
    oreq=OneRequest()
    try:
        oreq.ParseFromString(message)
        print "request received:",oreq.type
        res=dispatch(oreq).SerializeToString()
    except:
        oresp=OneResponse()
        oresp.type=ERROR_PARSING_EXCEPTION
        oresp.gresp.req=message
        oresp.gresp.computetime=-1.0
        oresp.gresp.server_ipadress=my_ip
        res=oresp.SerializeToString()
    finally:
        return res




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
        
        reply = request
        #reply = handle_request(request,verbose) # Echo is complex... :-)


if __name__ == '__main__':
    main()
