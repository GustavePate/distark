import zmq
from generic_request_pb2 import SimpleRequest
from generic_request_pb2 import SimpleResponse


def handle_message(message):
    print "message:", message
    return "ack"


def handle_message_protobuf(message):

    sreq = SimpleRequest()
    sreq.ParseFromString(message)
    print "request received:", sreq.youpla

    sresp = SimpleResponse()
    sresp.resp.req.servicename = sreq.req.servicename
    sresp.resp.req.caller = sreq.req.caller
    sresp.resp.computetime = 1
    sresp.boum = u'world!'
    res = sresp.SerializeToString()
    return res


context = zmq.Context.instance()
sock = context.socket(zmq.REP)
sock.connect('tcp://localhost:8081')

while True:
    msg = sock.recv()
    print msg
    response = handle_message_protobuf(msg)
    sock.send(response)
