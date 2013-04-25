#encoding: utf-8

import zmq 
from generic_request_pb2 import SimpleRequest;
from generic_request_pb2 import SimpleResponse;


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

#print "response:",response

