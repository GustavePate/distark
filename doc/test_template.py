#encoding: utf-8
import os
import pytest
import py
from time import sleep

#fixtures = powerfull setup / teardown


@pytest.fixture()
def i_will_execute_before_each_method():
    #possible to define before each test of the suite
    # in pytest.ini
    #print '\nhello i m here'
    pass


@pytest.mark.usefixtures("i_will_execute_before_each_method")
class TestTemplate(object):

    class_variable=''

    def test_template_func(self):
        assert True is True

    #TMPDIRµ***************************************
    #create a tmpdir
    def test_needatmpdir(self, tmpdir):
        #print tmpdir
        assert os.path.exists(str(tmpdir))

    #TESTING EXCEPTIONµ***************************************
    #raise exception
    def f(self):
        raise SystemExit(1)

    def test_myexception(self):
        with pytest.raises(SystemExit):
            self.f()

    #MARKµ***************************************
    @py.test.mark.slow
    def test_marked_as_slow(self):
        assert 'slow' == 'slow'
        sleep(0.1)

    @py.test.mark.fullstack
    def test_marked_as_fullstack(self):
        assert 'slow' == 'slow'

    #FIXTURESµ***************************************
    #simple fixture
    # scope="module" evalyated only once for the module
    # scope="session" evalyated only once for the whole test session
    # scope="function"
    @pytest.fixture(scope="module")
    def un_truc(self, request):
        #print 'un truc'
        TestTemplate.class_variable=''.join(
            ['truc', TestTemplate.class_variable])

        def run_only_at_module_end():
            #print "\nfinalizing un truc"
            pass
        request.addfinalizer(run_only_at_module_end)
        return TestTemplate.class_variable

    def test_montruc(self, un_truc):
        assert len(un_truc) == 4

    def test_montruc2(self, un_truc):
        assert len(un_truc) == 4

    #PARAMETERSµ***************************************

    @pytest.fixture(scope="module", params=['un', 'deux'])
    def fixparam(self, request):
        return request.param

    #will be called twice because fixture parameters
    def test_parameter(self, fixparam):
        #print fixparam
        assert fixparam in ['un', 'deux']

    #MONKEYPATCHINGµ***************************************
    def test_monkey(self, monkeypatch):
        def mockpath():
            return 'mockpath'
        monkeypatch.setattr(os, 'nice', mockpath)
        assert os.nice() == 'mockpath'
        #cleanup
        monkeypatch.undo()
        os.nice(1)
