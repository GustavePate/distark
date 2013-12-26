'''
Created on 27 avr. 2013

@author: guillaume
'''
from distarkcli.services.anotherservice import AnotherService
from distarkcli.services.anotherservice import AnotherRequest
import py
import pytest


@pytest.mark.usefixtures("infraup")
class TestAnotherService(object):

    @py.test.mark.fullstack
    def test_anotherservice(self):
            self.callanotherservice()

    def callanotherservice(self, txtreq='anotherworld'):

        request = AnotherRequest()
        request.setRequestStr(txtreq)
        ss = AnotherService(request)
        # blocking call
        response = ss.getResponse()

        if response[0] == ss.pbresptype:
            assert response[1].getResponseStr() == ''.join([txtreq, txtreq])
        else:
            # fail
            assert 0
