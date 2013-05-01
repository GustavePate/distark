#encoding: utf-8

import argparse
import traceback

from kazoo.client import KazooClient
from distark.commons.utils.MyConfiguration import Configuration

from kazoo.client import KazooState
from kazoo.client import KeeperState


from kazoo.client import KazooState


class ZooBorg(object):
    '''
    distark
    distark/client/
    distark/client/conf
    distark/client/list/client_uniq_id (ephemeral?

    
    '''
    zk=KazooClient()
    ip=''
    port=''
    initialized=False
    __shared_state = {} # variable de classe contenant l'état à partage
        
    @staticmethod
    def _my_listener(state):
        if state == KazooState.LOST:
            # Register somewhere that the session was lost
            print 'Zookeeper session LOST'
        elif state == KazooState.SUSPENDED:        
            # Handle being disconnected from Zookeeper
            print 'Zookeeper session SUSPENDED'
        else:
            print 'Zookeeper session (RE)CONNECTED'
            # Handle being connected/reconnected to Zookeeper

    def __init__(self):
        # copie de l'état lors de l'initialisation d'une nouvelle instance
        self.__dict__ = self.__shared_state     
        if not(self.initialized):
            conf=Configuration()
            self.ip=Configuration.get()['client']['zookeeper']['ip']
            self.port=Configuration.get()['client']['zookeeper']['port']
            self.connect()
            # Ensure a path, create if necessary
            self.zk.ensure_path("/distark/client/conf")
            self.initialized=True
            
            @self.zk.add_listener
            def watch_for_ro(state):
                if state == KazooState.CONNECTED:
                    if zk.client_state == KeeperState.CONNECTED_RO:
                        print("Read only mode!")
                    else:
                        print("Read/Write mode!")


    def connect(self):
        self.zk = KazooClient(hosts=''.join([self.ip,':',self.port]))
        self.zk.start()
        self.zk.add_listener(self._my_listener)


    def close(self):
        print "zoo connection closed"
        self.zk.stop()
        self.zk.close()

    def registerclient(self,client_id):
        '''
        client_id must be a string
        automagically update conf with zookeeper content
        '''
        # Create a node with data
        #TODO: add system properties in data (ip, os) 
        #TODO: add uniq client id
        self.zk.ensure_path("/distark/client/list")
        path=''.join(['/distark/client/list/',client_id])
        data=b'ip̂,os'
        if not(self.zk.exists(path)):
            self.zk.create(path,data)
        else:
            self.zk.delete(path,recursive=True)
            self.zk.create(path, data)
        #reload conf if change in zoo
        self._setHandleOnClientConf(self._clientconfwatcher)

    def unregisterclient(self,client_id):
        '''
        client_id must be a string
        '''
        self.zk.ensure_path("/distark/client/list")
        path=''.join(['/distark/client/list/',client_id])
        if self.zk.exists(path):
            self.zk.delete(path,recursive=True)

    def getClientList(self):
        return self.zk.get_children('/distark/client/list')

    def _setHandleOnClientConf(self,callable):
        self.zk.DataWatch('/distark/client/conf/conf_reload_trigger',callable)

    def _dumbdatawatcher(self,data,stat):
        print 'dumbwatcher'
        print 'data:',data
        print 'stat:',stat
    
    def _dumbchildrenwatcher(self,children):
        print 'dumbwatcher'
        print 'children:',children

    def _clientconfwatcher(self,data,stat):
        self.getClientConf()

    def getClientConf(self):
        '''
        return dic
        '''
        print 'Load zookeeper client conf'
        zooconf={'broker':{'connectionstr':None}}
        zooconf['broker']['connectionstr'],stat=self.zk.get('/distark/client/conf/broker/connectionstr')
        Configuration.settings.update(zooconf)
        print Configuration.settings
        return zooconf

    def getWorkerConf(self):
        pass

    def getBrokerConf(self):
        pass


def _initclientconf(zb):
    print "initclientconf"
    zb=ZooBorg()
    print "initclientconf: delete client root"
    if zb.zk.exists("/distark/client"):
        zb.zk.delete("/distark/client",recursive=True)
    print "initclientconf: create distark/client/list"
    zb.zk.ensure_path("/distark/client/list")
    print "initclientconf: create distark/client/conf"
    zb.zk.ensure_path("/distark/client/conf")
    print "initclientconf: create distark/client/broker/connectionstr"
    zb.zk.ensure_path("/distark/client/conf/broker/connectionstr")
    print "initclientconf: set data distark/client/broker/connectionstr"
    zb.zk.set("/distark/client/conf/broker/connectionstr",b"tcp://localhost:5555")
    zb.zk.ensure_path("/distark/client/conf/conf_reload_trigger")
    print "initclientconf: create distark/client/conf/conf_reload_trigger"



if __name__ == '__main__':
    ##############################################
    #     ARGUMENTS PARSING
    ##############################################
    parser = argparse.ArgumentParser(description='Send requests')
    parser.add_argument('do', help='test initclientconf initworkerconf initbrokerconf initall', type=str)
    
    parser.set_defaults(do='test')
    args= parser.parse_args()
    print "Program Launched with args:"+str(args)
    print "Do:"+str(args.do)    
    
    zb=None
    zb=ZooBorg()
    try:
        if args.do == 'initclientconf':
            _initclientconf(zb)

        elif args.do == 'initall':
            _initclientconf(zb)
        else:
            print 'do nothing !!!'

    except:
        traceback.print_exc()

    finally:
        zb.unregisterclient('test_client')
        zb.close()

