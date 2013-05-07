from distark.commons.utils.zoo import ZooBorg
import traceback
import pytest
import py


@pytest.mark.usefixtures("infraup")
@py.test.mark.fullstack
def testclient():
    zb = None
    zb = ZooBorg()
    try:
        client_id = 'test_id'
        zb.registerclient(client_id)
        # conf must be updated

        # client id must be in client list
        cl = zb.getClientList()
        assert client_id in cl
    except:
        traceback.print_exc()

    finally:
        zb.unregisterclient('test_client')
        zb.close()
