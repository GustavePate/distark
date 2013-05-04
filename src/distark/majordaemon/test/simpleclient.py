# encoding: utf-8

'''
Created on 25 avr. 2013

@author: guillaume
'''

import zmq
import sys


from distark.commons.protos.proto_services_pb2 import SimpleRequest
from distark.commons.protos.proto_services_pb2 import SimpleResponse


def text_version(sock):
    print "==>text_version"
    sock.send(' '.join(sys.argv[1:]))
    response = sock.recv()
    print "response:", response


def protobuf_simple_version(sock):

    print "==>protobuf_simple_version"
    sreq = SimpleRequest()
    sreq.youpla = u'hello'

    sock.send(sreq.SerializeToString())
    response = sock.recv()
    sresp = SimpleResponse()
    sresp.ParseFromString(response)

    print "server response:", sresp.boum


if __name__ == '__main__':
    context = zmq.Context.instance()
    sock = context.socket(zmq.REQ)
    sock.bind('tcp://*:8081')

    #### proto buf version
    protobuf_simple_version(sock)


    #### text version
    # text_version(sock)
