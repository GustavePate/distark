#encoding: utf-8
"""
Majordomo Protocol client example. Uses the mdcli API to hide all MDP aspects

Author : Min RK <benjaminrk@gmail.com>

"""
import datetime
import sys
import argparse

from distark.majordaemon.client.transport.majordomoclient import MajorDomoClient 
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


from distark.commons.utils.NetInfo import NetInfo 



my_ip=NetInfo.getIPString()
NB_REQUEST=100000

#TODO: create a handler in separate file for each request/reply pair 
#TODO: the handler should take care of transport and serialisation/deserialisation to be used as an API

#OUT: PBOneRequest
def simple_request(youpla): 

    #instanciate a SimpleRequest
    oreq=PBOneRequest()
    oreq.simplereq.youpla=youpla
    
    oreq.rtype=SIMPLE_REQUEST
    oreq.greq.servicename='SIMPLE_REQUEST'
    oreq.greq.caller='me_the_client'
    oreq.greq.ipadress=my_ip
    oreq.greq.priority=PRIORITY_STD
    res=oreq.SerializeToString()
    return [res]


def simple_response(oresp):
    print "received: ",oresp.simpleresp.boum
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


#IN: OneResponse
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

    ##############################################
    #     ARGUMENTS PARSING
    ##############################################

    parser = argparse.ArgumentParser(description='Send requests')
    parser.add_argument('numreq', help='number of request to send', type=int)
    parser.add_argument('-c', '--content', help='content data to send to simple request', type=str)
    parser.add_argument('-v', '--verbose', help='increase output verbosity',action='store_true')
    parser.add_argument('-a', '--asynchronous', help='send/receive asynchronous',action='store_true')
    
    parser.set_defaults(numreq=10)
    parser.set_defaults(content='youpi')
    args= parser.parse_args()
    print "Program Launched with args:"+str(args)
    print "Number of requests:"+str(args.numreq)
    print "Verbose:"+str(args.verbose)
    print "Content:"+str(args.content)

    data = args.content
    verbose = args.verbose
    NB_REQUEST=args.numreq
    
    start_launcher=datetime.datetime.now()
        
    client = MajorDomoClient("tcp://localhost:5555", verbose)
    requests = NB_REQUEST
    
    
    
    count = 0
    
    if args.asynchronous:
        for _ in xrange(requests):
            try:
                request=simple_request(data)
                client.send("echo", request)
                if verbose:
                    print 'request sended:',request
            except KeyboardInterrupt:
                print "send interrupted, aborting"
                return
    
        
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
    else:
        for _ in xrange(requests):
            try:
                request=simple_request(data)
                client.send("echo", request)
                if verbose:
                    print 'request sended:',request
                reply = client.recv()
                if reply is None:
                    print 'None reply'
                else:
                    #check if my reponse is a list of one
                    if ZMQUtils.is_valid_envelop(reply):
                        #then
                        sresp=PBOneResponse()
                        sresp.ParseFromString(reply[0])    
                        handle_response(sresp)
                    else:
                        print "received invalid response envelop"            
            except KeyboardInterrupt:
                print "send interrupted, aborting"
                return
            count += 1
        
    print "%i requests/replies processed" % count
    
    end_launcher=datetime.datetime.now()

    delta=end_launcher-start_launcher
    print 'Launcher ALL JOBS DONE  in ',str(delta),' !!!!'    
    print 'Avergage round-trip:', str(delta/requests)   

if __name__ == '__main__':
    main()
