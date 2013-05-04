'''
Created on 27 avr. 2013

@author: guillaume
'''
import datetime
import argparse
from distark.commons.utils.MyConfiguration import Configuration
from distark.majordaemon.client.services.simpleservice import SimpleService, SimpleRequest


class Caller(object):

    verbose = False

    def __init__(self, verbose=False):

        self.verbose = verbose
        pass

    def main(self, txtreq='youpla?'):

        request = SimpleRequest()
        request.setYoupla(txtreq)
        ss = SimpleService(request)
        # blocking call
        response = ss.getResponse()

        if response[0] == ss.associated_pb_response:
            print response[1].getBoum()
            func_error = False
            if func_error:
                print 'functional error handling ...'
            assert response[1].getBoum() == ''.join(reversed(txtreq))
        else:
            # TODO: add helper here
            print 'caller: technical error handling...'

if __name__ == '__main__':

    ##############################################
    #     ARGUMENTS PARSING
    ##############################################
    parser = argparse.ArgumentParser(description='Send requests')
    parser.add_argument('numreq', help='number of request to send', type=int)
    parser.add_argument(
        '-c', '--content', help='content data to send to simple request', type=str)
    parser.add_argument('-v', '--verbose',
                        help='increase output verbosity', action='store_true')
    # parser.add_argument('-a', '--asynchronous', help='send/receive
    # asynchronous',action='store_true')

    parser.set_defaults(numreq=10)
    parser.set_defaults(content='youpi')
    args = parser.parse_args()
    print "Program Launched with args:" + str(args)
    print "Number of requests:" + str(args.numreq)
    print "Verbose:" + str(args.verbose)
    print "Content:" + str(args.content)

    content = args.content
    verbose = args.verbose
    NB_REQUEST = args.numreq

    # init conf
    print Configuration.get()

    start_launcher = datetime.datetime.now()

    for _ in xrange(NB_REQUEST):

        caller = Caller(verbose)
        caller.main(content)

    end_launcher = datetime.datetime.now()

    delta = end_launcher - start_launcher
    print 'Launcher ALL JOBS DONE  in ', str(delta), ' !!!!'
    print 'Avergage round-trip:', str(delta / NB_REQUEST)
