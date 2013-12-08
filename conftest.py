import pytest
import py


@py.test.mark.fullstack
@pytest.fixture(scope="session")
def infraup(request):

    from distark.majordaemon.infralauncher import InfraLauncher

    def run_only_at_session_end():
        print "\nfinalizing session"
        InfraLauncher.stop()

    InfraLauncher.launch(2)
    request.addfinalizer(run_only_at_session_end)
