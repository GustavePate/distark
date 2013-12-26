from distark.commons.utils.MyConfiguration import Configuration
import py
import pytest


@pytest.mark.usefixtures("infraup")
class TestConfiguration(object):

    @py.test.mark.fullstack
    def test_conf_client(self):
        assert Configuration.getclient() is not None
        assert Configuration.initialized is True
        assert Configuration.client_initialized is True
        assert len(Configuration.getclient()['zookeeper']['ip'])>0

    @py.test.mark.fullstack
    def test_conf_worker(self):
        assert Configuration.getworker() is not None
        assert Configuration.initialized is True
        assert Configuration.worker_initialized is True
        assert len(Configuration.getworker()['zookeeper']['ip'])>0
