import pytest
import py


confpath = ""

def pytest_addoption(parser):
    parser.addoption("--confpath", action="append", default=[],
                     help="configuration full path")

@py.test.mark.fullstack
@pytest.fixture(scope="session")
def infraup(request):

    from distark.majordaemon.infralauncher import InfraLauncher

    def run_only_at_session_end():
        print "\nfinalizing session"
        InfraLauncher.stop()

    if pytest.config.getoption('confpath') is not None:
        if len(pytest.config.getoption('confpath')) > 0:
            confpath = pytest.config.getoption('confpath')[0]
    print "Launch Infra with conf:", confpath

    InfraLauncher.launch(confpath, 2)
    request.addfinalizer(run_only_at_session_end)
