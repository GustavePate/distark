from distark.commons.utils.zoo import ZooBorg
from distark.commons.utils.MyConfiguration import Configuration
import traceback
import pytest
import py


@pytest.mark.usefixtures("infraup")
class TestZoo(object):

    def stubhandler(self, data, stat):
        print "TestZoo: I handle"

    @py.test.mark.fullstack
    def test_client(self):
        ip = Configuration.getclient()['zookeeper']['ip']
        port = Configuration.getclient()['zookeeper']['port']
        zb = ZooBorg(ip, port)
        try:
            client_id = 'test_id'
            zb.register(ZooBorg.CLIENT, client_id, self.stubhandler)
            # conf must be updated

            # client id must be in client list
            cl = zb.getList(ZooBorg.CLIENT)
            assert client_id in cl
        except:
            traceback.print_exc()
            assert 0
        finally:
            zb.unregister(ZooBorg.CLIENT, 'test_client')
            zb.close()

    @pytest.mark.usefixtures("infraup")
    @py.test.mark.fullstack
    def test_worker(self):
        ip = Configuration.getworker()['zookeeper']['ip']
        port = Configuration.getworker()['zookeeper']['port']
        zb = ZooBorg(ip, port)
        try:
            worker_id = 'test_id'
            zb.register(ZooBorg.WORKER, worker_id, self.stubhandler)
            # conf must be updated

            # client id must be in client list
            cl = zb.getList(ZooBorg.WORKER)
            assert worker_id in cl
        except:
            traceback.print_exc()
            assert 0
        finally:
            zb.unregister(ZooBorg.WORKER, 'test_worker')
            zb.close()
