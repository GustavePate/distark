# encoding: utf-8

"""Majordomo Protocol worker example.

Uses the mdwrk API to hide all MDP aspects

Author: Min RK <benjaminrk@gmail.com>
"""

import datetime
import traceback
import argparse

from distark.majordaemon.worker.mdwrkapi import MajorDomoWorker
from distarkcli.utils.NetInfo import NetInfo
from distarkcli.utils.MyConfiguration import Configuration
from distarkcli.utils.zoo import ZooConst, ZooBorgFactory
from distark.majordaemon.worker.db.mongopool import MongoPool
from distarkcli.utils.uniq import Uniq
from distark.majordaemon.commons.ZMQUtils import ZMQUtils

from distarkcli.protos.generic_service_pb2 import PBOneRequest
from distarkcli.protos.generic_service_pb2 import PBOneResponse

from distarkcli.protos.generic_service_pb2 import ERROR_UNKNOWN_SERVICE
from distarkcli.protos.generic_service_pb2 import ERROR_PARSING_EXCEPTION
from distarkcli.protos.generic_service_pb2 import ERROR_INVALID_ENVELOP
from distarkcli.protos.generic_service_pb2 import _PBREQUESTTYPE as PBRequestType


from distark.majordaemon.worker.processors.anotherprocessor import another_request_handler
from distarkcli.protos.generic_service_pb2 import ANOTHER_REQUEST

from distark.majordaemon.worker.processors.SimpleProcessor import simple_request_handler
from distarkcli.protos.generic_service_pb2 import SIMPLE_REQUEST

from distark.majordaemon.worker.processors.searchfoodprocessor import search_food_request_handler
from distarkcli.protos.generic_service_pb2 import SEARCH_FOOD_REQUEST

from distark.majordaemon.worker.utils import error_response


# a = threading.Thread(None, affiche, None, (200,), {'nom':'thread a'})
# b = threading.Thread(None, affiche, None, (200,), {'nom':'thread b'})
# a.start()


# IN: OneReponse, OneRequest
# OUT: nothing
def fillOneResponseGenericFields(oresp, oreq):
    oresp.gresp.req.servicename = oreq.greq.servicename
    oresp.gresp.req.caller = oreq.greq.caller
    oresp.gresp.req.ipadress = oreq.greq.ipadress
    oresp.gresp.server_ipadress = NetInfo.getIPString()


class Worker(object):

    start_working = 0
    end_working = 0
    verbose = False
    services = []
    _terminated = False
    uniqid = ''
    _isup = False

    existing_services = {
        SIMPLE_REQUEST: simple_request_handler,
        ANOTHER_REQUEST: another_request_handler,
        SEARCH_FOOD_REQUEST: search_food_request_handler,
    }

    # IN: PBOneRequest
    # OUT: PBOneResponse
    def handle_request(self, oreq):

        # prepare response
        oresp = PBOneResponse()
        if self.verbose:
            print "handle:", PBRequestType.values_by_number[oreq.rtype].name

        # if exists
        if oreq.rtype in self.existing_services.keys():
            # do the job
            oresp = self.existing_services[oreq.rtype](oreq)
        else:
            oresp = error_response(ERROR_UNKNOWN_SERVICE)
            print "dispatch: Unknown service:", oreq.rtype

        # Fill in Generic Response
        fillOneResponseGenericFields(oresp, oreq)

        return oresp

    # IN: ZMQEnvelop
    # OUT: string
    # if deserialize a success: handle
    # else reply protobuf OneResponse error
    def deserialize_and_reply(self, request):

        start_working = datetime.datetime.now()

        if not ZMQUtils.is_valid_envelop(request):
            print 'Invalid Request:', TypeError
            res = error_response(ERROR_INVALID_ENVELOP)
        else:
            if self.verbose:
                print "raw_request", request
            pboreq = PBOneRequest()
            res = ''
            try:
                pboreq = PBOneRequest()
                pboreq.ParseFromString(request[0])
                pboresp = self.handle_request(pboreq)
                end_working = datetime.datetime.now()
                delta = end_working - start_working
                pboresp.gresp.computetime = delta.total_seconds()
                res = pboresp.SerializeToString()
            except TypeError:
                print 'Exception:', TypeError
                traceback.print_exc()
                res = error_response(ERROR_PARSING_EXCEPTION)
            except Exception:
                print 'General Exception:', Exception
                traceback.print_exc()
                res = error_response(ERROR_PARSING_EXCEPTION)
            finally:
                if self.verbose:
                    print 'raw_reply:', res
                return [res]

    def work(self, verbose=False):
        reply = None
        while True:
            if not(self._terminated):
                self._isup = True
                request = self.worker.recv(reply)
            else:
                request = None
            if request is None:
                print "Have to quit, bye !"
                break  # Worker was interrupted

            ### Reply Must be in a list !!!!!!
            reply = self.deserialize_and_reply(request)

    def stop(self):
        self.worker.stop()
        self._terminated = True

    def zoo_conf_changed(self, data, stat):
        print 'worker conf has changed !!!'
        pass

    def isup(self):
        if not(self._terminated):
            return self._isup
        else:
            return False

    def __init__(self, verbose=False):
        # TODO: add uniq id
        self.verbose = verbose
        uniq = Uniq()
        self.uniqid = uniq.getid(uniq.WORKER)

        #zookeeper connection
        zb = ZooBorgFactory(Configuration.getworker()['zookeeper']['mockmode'],
                     Configuration.getworker()['zookeeper']['ip'],
                     Configuration.getworker()['zookeeper']['port'])
        addconf = zb.getConf(ZooConst.WORKER)
        con_str = addconf['broker']['connectionstr']
        zb.register(ZooConst.WORKER, self.uniqid, self.zoo_conf_changed)
        self.worker = MajorDomoWorker(con_str, "echo", self.verbose)

        #init mongodb pool
        self.mp = MongoPool(Configuration.getworker()['mongo']['host'],
                            Configuration.getworker()['mongo']['port'],
                            Configuration.getworker()['mongo']['db'],
                            Configuration.getworker()['mongo']['maxcon'])


def main(conf, verbose=False):
    conf = Configuration(conf)
    w = Worker(verbose)
    return w

if __name__ == '__main__':

    ##############################################
    #     ARGUMENTS PARSING
    ##############################################
    parser = argparse.ArgumentParser(prog = 'Worker', description='Send requests')
    parser.add_argument('-c', '--conf',
                        help='conf filepath',
                        type=str)
    parser.add_argument(
            '-v', '--verbose', help='verbose output', action='store_true')
    args = parser.parse_args()
    print "Program Launched with args:" + str(args)

    #init conf
    conf = Configuration(args.conf)

    #work
    w = main()
    w.work(args.verbose)
