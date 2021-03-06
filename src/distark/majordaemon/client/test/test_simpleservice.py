from distarkcli.services.simpleservice import SimpleService
from distarkcli.services.simpleservice import SimpleRequest
import py
import pytest


@pytest.mark.usefixtures("infraup")
class TestSimpleService(object):

    @py.test.mark.fullstack
    def test_simpleservice(self):
        self.callsimpleservice()

    def callsimpleservice(self, txtreq='anotherworld'):
        request = SimpleRequest()
        request.setYoupla(txtreq)
        ss = SimpleService(request)
        # blocking call
        response = ss.getResponse()
        if response[0] == ss.pbresptype:
            assert response[1].getBoum() == ''.join(reversed(txtreq))
        else:
            assert 0
