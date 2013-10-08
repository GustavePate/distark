from distark.commons.utils.zoo import ZooBorg
from distark.commons.utils.MyConfiguration import Configuration
import traceback
import pytest
import py


@pytest.mark.usefixtures("infraup")
class TestZoo(object):

    def stubhandler(self, data, stat):
        #print "TestZoo: I handle"
        pass

    @py.test.mark.fullstack
    def test_client(self):
        ip = Configuration.getclient()['zookeeper']['ip']
        port = Configuration.getclient()['zookeeper']['port']
        zb = ZooBorg(ip, port)
        try:
            client_id = 'client_test_id'
            zb.register(ZooBorg.CLIENT, client_id, self.stubhandler)
            # conf must be updated

            # client id must be in client list
            cl = zb.getList(ZooBorg.CLIENT)
            assert client_id in cl
            #just the one created here (connection pools are dead here)
            #print "clientlist:",cl
            assert len(cl) == 1
        except:
            traceback.print_exc()
            assert 0
        finally:
            zb.unregister(ZooBorg.CLIENT, client_id)
            #zb.close()

    @py.test.mark.fullstack
    def test_broker(self):
        ip = Configuration.getbroker()['zookeeper']['ip']
        port = Configuration.getbroker()['zookeeper']['port']
        zb = ZooBorg(ip, port)
        try:
            broker_id = 'broker_test_id'
            zb.register(ZooBorg.BROKER, broker_id, self.stubhandler)
            # conf must be updated

            # broker id must be in broker list
            cl = zb.getList(ZooBorg.BROKER)
            #print "brokerlist:",cl
            assert broker_id in cl
            #the one created here + infra broker(s)
            assert len(cl) > 1
        except:
            traceback.print_exc()
            assert 0
        finally:
            zb.unregister(ZooBorg.BROKER, broker_id)

    @py.test.mark.fullstack
    def test_worker(self):
        ip = Configuration.getworker()['zookeeper']['ip']
        port = Configuration.getworker()['zookeeper']['port']
        zb = ZooBorg(ip, port)
        worker_id = 'test_worket_id'
        try:
            zb.register(ZooBorg.WORKER, worker_id, self.stubhandler)
            # client id must be in client list
            cl = zb.getList(ZooBorg.WORKER)
            #print "workerlist:",cl
            assert worker_id in cl
            #just created + test infra worker
            assert len(cl) >= 2
        except:
            traceback.print_exc()
            assert 0
        finally:
            zb.unregister(ZooBorg.WORKER, worker_id)
            #zb.close()
