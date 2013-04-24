#encoding: utf-8
"""
Majordomo Protocol client example. Uses the mdcli API to hide all MDP aspects

Author : Min RK <benjaminrk@gmail.com>

"""
import datetime
import sys
from distark.majordaemon.client.mdcliapi import MajorDomoClient
from distark.commons.protos.proto_services_pb2 import OneRequest, OneResponse
from distark.commons.protos.proto_services_pb2 import SIMPLE_REQUEST
from distark.commons.protos.proto_services_pb2 import SIMPLE_RESPONSE
from distark.commons.protos.proto_services_pb2 import UNKNOWN_SERVICE
from distark.commons.protos.proto_services_pb2 import UNSUPPORTED_SERVICE
from distark.commons.protos.proto_services_pb2 import PRIORITY_STD
from distark.commons.protos.proto_services_pb2 import GenericRequest, GenericResponse
from distark.commons.protos.proto_services_pb2 import SimpleRequest, SimpleResponse

from distark.commons.utils.NetInfo import NetInfo

my_ip=NetInfo.getIPString()
NB_REQUEST=10

def simplerequest(youpla): 
    
    #instanciate a SimpleRequest
    req=OneRequest()
    req.type=SIMPLE_REQUEST
    req.simplereq.youpla=youpla
    req.greq.servicename='SIMPLE_REQUEST'
    req.greq.caller='me_the_client'
    req.greq.ipadress=my_ip
    req.greq.priority=PRIORITY_STD
    return req.SerializeToString()
    

def simple_response(oresp):
    print "received: ",oresp.simpleresp.boum
    pass

def retryNtimes(oresp):
    #TODO: implement
    print 'Unknow or Unsupported service received: TODO retry Nx'


def handle_response(oresp):
    
    existing_response = {
                         SIMPLE_RESPONSE: simple_response,
                         UNKNOWN_SERVICE : retryNtimes,
                         UNSUPPORTED_SERVICE: retryNtimes,
                         }

    
    #do the job
    if oresp.type in existing_response.keys():
        oresp=existing_response[oresp.type](oresp)
    else:
        oresp.type=UNKNOWN_SERVICE
        print "Unknown response type", oresp.type
    


def main():
    
    start_launcher=datetime.datetime.now()
    
    verbose = '-v' in sys.argv
    client = MajorDomoClient("tcp://localhost:5555", verbose)
    requests = NB_REQUEST
    for i in xrange(requests):
        request = "Hello world"
        try:
            #client.send("echo", simplerequest('youpi'))
            client.send("echo",request)
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
#            else:
#                sresp=OneResponse()
#                sresp.ParseFromString(reply)    
#                handle_response(sresp)
            
        count += 1
    print "%i requests/replies processed" % count
    
    end_launcher=datetime.datetime.now()

    delta=end_launcher-start_launcher
    print('Launcher ALL JOBS DONE  in '+str(delta)+' !!!!')    
    

if __name__ == '__main__':
    main()
