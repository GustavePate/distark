'''
Created on 25 avr. 2013

@author: guillaume
'''

import zmq
from distark.commons.protos.proto_services_pb2 import SimpleRequest
from distark.commons.protos.proto_services_pb2 import SimpleResponse

#### text versions


def handle_message_text(message):
    print "==>handle_message"
    print "message:", message
    return "ack"


#### protofbuf versions
def handle_message_simple_protobuf(message):

    print "==>handle_message_simple_protobuf"
    sreq = SimpleRequest()
    sreq.ParseFromString(message)
    print "request received:", sreq.youpla

    sresp = SimpleResponse()
#     sresp.resp.req.servicename=sreq.req.servicename
#     sresp.resp.req.caller=sreq.req.caller
#     sresp.resp.computetime=1
    sresp.boum = u'world!'
    res = sresp.SerializeToString()
    return res


if __name__ == '__main__':
    context = zmq.Context.instance()
    sock = context.socket(zmq.REP)
    sock.connect('tcp://localhost:8081')

    while True:
        msg = sock.recv()
        print "received:", msg
        response = handle_message_simple_protobuf(msg)
        # response = handle_message_text(msg)
        sock.send(response)
        print "sended:", response
