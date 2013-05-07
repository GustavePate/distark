from distark.commons.utils.processmanager import ProcessManager


class TestProcessManager(object):

    def test_fire_exists_kill(self):
        ProcessManager.fireandforget(['sleep', '160'])
        assert ProcessManager.exists('dghijgfjkgdgdghccccxcc') is False
        assert ProcessManager.exists('sleep') is True
        pids = ProcessManager.killall('sleep')
        assert ProcessManager.pidexists(pids) is False
        assert ProcessManager.exists('sleep') is False
