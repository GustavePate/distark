import py
import pytest
from distark.commons.utils.db.mongopool import MongoPool
from distark.commons.utils.MyConfiguration import Configuration


@pytest.mark.usefixtures("infraup")
class TestMongoPool(object):
    mp = None
    MAX_CONNECTION = 3

    def getConnection(self):
        self.mp = MongoPool()
        #print mp
        return self.mp.getConnection()

    #useless: overide by infra setup
    def initConnection(self):
        host = Configuration.getworker()['mongo']['host']
        port = Configuration.getworker()['mongo']['port']
        db = Configuration.getworker()['mongo']['db']
        self.mp = MongoPool(host, port, db, self.MAX_CONNECTION)
        #print mp
        return self.mp.getConnection()

    @py.test.mark.fullstack
    def test_mongopool(self):

        copool = []

        self.mp = MongoPool()
        nbmax = self.mp.availableconnection

        # init
        co1 = self.initConnection()
        assert co1 is not None
        copool.append(co1)

        # get connections
        for _ in range(2, nbmax + 1):
            co = self.getConnection()
            assert co is not None
            copool.append(co)

        # should error pool explosed
        co = None
        try:
            co = self.getConnection()
        except Exception:
            assert co is None
        else:
            assert False, 'pool should be full'

        mp = MongoPool()
        assert mp.availableconnection == 0

        # Release cnnection
        for co in copool:
            mp.returnToPool(co)

        assert mp.availableconnection == nbmax
