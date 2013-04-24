#encoding: utf-8

import zmq


 
from distark.commons.protos.proto_services_pb2 import OneRequest,RequestType, GenericRequest
from distark.commons.protos.proto_services_pb2 import OneResponse,ResponseType, GenericResponse
from distark.commons.protos.proto_services_pb2 import SimpleRequest
from distark.commons.protos.proto_services_pb2 import SimpleResponse
from distark.commons.utils.MyConfiguration import Configuration


def dothejob():

    conf=Configuration()
    context = zmq.Context.instance() 
    sock = context.socket(zmq.REQ) 
    sock.bind('tcp://*:8081') 
    #sock.send(' '.join(sys.argv[1:])) 
    #response = sock.recv()
    #print "response:",response

    sreq=SimpleRequest()
    sreq.req.servicename=u'SimpleRequest'
    sreq.req.caller=u'me_the_client'
    sreq.youpla=u'hello'

    sock.send(sreq.SerializeToString()) 
    response = sock.recv()
    sresp=SimpleResponse()
    sresp.ParseFromString(response)

    print "server response:",sresp.boum,"to",sresp.resp.req.caller

if __name__ == '__main__':
    dothejob()



