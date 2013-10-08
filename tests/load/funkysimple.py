import unittest
import py
from random import randrange
from distark.majordaemon.client.test.test_anotherservice import TestAnotherService
from distark.majordaemon.client.test.test_simpleservice import TestSimpleService
from distark.majordaemon.client.test.test_searchfoodservice import TestSearchFoodService
from distark.majordaemon.infralauncher import InfraLauncher
from funkload.FunkLoadTestCase import FunkLoadTestCase


class FunkySimple(FunkLoadTestCase):
    """This test use a configuration file Simple.conf."""

    @py.test.mark.fullstack
    def setUp(self):
        if not(self.in_bench_mode):
            InfraLauncher.launch(2)

    @py.test.mark.fullstack
    def tearDown(self):
        if not(self.in_bench_mode):
            InfraLauncher.stop()

    def setUpCycle(self):
        pass

    def tearDownCycle(self):
        pass

    @py.test.mark.fullstack
    def setUpBench(self):
        """Setting up test."""
        self.label="testing different services" + "\n"
        self.mode='bench'
        # self.server_url = self.conf_get('main', 'url')
        InfraLauncher.launch(2)

    @py.test.mark.fullstack
    def tearDownBench(self):
        InfraLauncher.stop()
        self.logd("teardown\n")

    @py.test.mark.fullstack
    def test_simple(self):
        # The description should be set in the
        # configuration file
        # server_url = self.server_url
        # begin of test
        # ---------------------------------------------
        nb_time = self.conf_getInt('test_simple', 'nb_time')
        another=TestAnotherService()
        self.another_inc=0
        simple=TestSimpleService()
        self.simple_inc=0
        searchfood = TestSearchFoodService()
        self.searchfood_inc = 0
        for i in range(nb_time):
            coin=randrange(1, 100)
            if coin<=30:
                another.callanotherservice()
                self.another_inc = self.another_inc + 1
            elif coin <= 60:
                simple.callsimpleservice()
                self.simple_inc = self.simple_inc + 1
            else:
                searchfood.callsearchfoodservice()
                self.searchfood_inc += 1

            # self.get(server_url, description='Get url')
        # end
        # of
        # test
        # -----------------------------------------------
        pass


if __name__ in ('main', '__main__'):
    unittest.main()
