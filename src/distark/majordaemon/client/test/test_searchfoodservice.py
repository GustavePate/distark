from distark.majordaemon.client.services.searchfoodservice import SearchFoodService
from distark.majordaemon.client.services.searchfoodservice import SearchFoodRequest
import py
import pytest


@pytest.mark.usefixtures("infraup")
class TestSearchFoodService(object):

    @py.test.mark.fullstack
    def test_searchfoodservice(self):
        self.callsearchfoodservice("ananas")

    def callsearchfoodservice(self, txtreq="unkown"):
        request = SearchFoodRequest()
        request.setReq(txtreq)
        ss = SearchFoodService(request)
        # blocking call
        response = ss.getResponse()

        if response[0] == ss.pbresptype:
            assert len(response[1].getFoods()) > 0
        else:
            assert False
            # fail
