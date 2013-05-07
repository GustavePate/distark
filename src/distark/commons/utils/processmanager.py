import subprocess
import signal
import os
from time import sleep


class ProcessManager(object):

    @staticmethod
    def killall(processnameregex):

        proc = subprocess.Popen(["pgrep", processnameregex], stdout=subprocess.PIPE)
        # Kill process.
        pidlist = []
        for pid in proc.stdout:
            pidlist.append(pid)
            print "licencetokill:", pid
            os.kill(int(pid), signal.SIGINT)
            # Check if the process that we killed is alive.
            if ProcessManager.pidexists([pid]):
                try:
                    print "killagain"
                    os.kill(int(pid), signal.SIGKILL)
                except Exception:
                    print "killagain:", Exception
                    # wasn't able to kill the process: don't exists anymore
                    pass
        return pidlist

    @staticmethod
    def pidexists(pidstrlist):
        res = True
        for pid in pidstrlist:
            if not(os.path.exists("/proc/" + pid)):
                res = False
        return res

    @staticmethod
    def exists(processnameregex):
        res = False
        sleep(0.4)

        proc = subprocess.Popen(["pgrep", processnameregex], stdout=subprocess.PIPE)
        for pid in proc.stdout:
            print "exists:", pid
            res = True
        return res

    @staticmethod
    def fireandforget(listcmd):
        subprocess.Popen(listcmd)
