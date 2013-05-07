import threading
from time import sleep
from distark.majordaemon.broker.mdbroker import main as bmain
from distark.majordaemon.worker.mdworker import main as wmain


class WorkerThread(threading.Thread):
    _worker = None

    def __init__(self):
        threading.Thread.__init__(self)
        print "init worker"

    def stop(self):
        self._worker.stop()

    def run(self):
        print "running worker"
        self._worker = wmain()
        self._worker.work()
        print "stopping worker"


class BrokerThread(threading.Thread):
    _broker = None

    def __init__(self):
        threading.Thread.__init__(self)
        print "init broker"

    def stop(self):
        self._broker.stop()

    def run(self):
        print "running broker"
        self._broker = bmain()
        self._broker.mediate()  # run forever
        print "stopping broker"


class InfraLauncher(object):

    brokerlist = []
    workerlist = []

    @staticmethod
    def launch(nbworker):
        print "Launch infra !!!!!!"
        if len(InfraLauncher.brokerlist) == 0:
            # launch broker
            InfraLauncher.brokerlist.append(BrokerThread())
            for _ in range(nbworker):
                # launch worker
                InfraLauncher.workerlist.append(WorkerThread())

            for b in InfraLauncher.brokerlist:
                b.start()

            for w in InfraLauncher.workerlist:
                w.start()

    @staticmethod
    def stop():
        print "Stop infra !!!!!!"
        for b in InfraLauncher.brokerlist:
            b.stop()

        for w in InfraLauncher.workerlist:
            w.stop()
