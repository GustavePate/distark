# encoding: utf-8

""" this is a borg """

from pymongo import MongoClient


class MongoPool(object):

    initialized = False
    __availableconnection = []
    __busyconnection = []
    __shared_state = {}  # variable de classe contenant l'état à partage
    __maxconnection = 0

    def __init__(self, host='', port='', db='', maxconnection=10):
        # copie de l'état lors de l'initialisation d'une nouvelle instance
        self.__dict__ = self.__shared_state
        if not(self.initialized):
            if (host == '' or port == '' or db == ''):
                # raise exception
                raise Exception('MongoPool init error: missing host or port')
            else:
                self.__maxconnection = maxconnection
                for _ in range(1, maxconnection + 1):
                    client = MongoClient(host, port)
                    conn = client[db]
                    self.__availableconnection.append(conn)
                self.initialized = True

    def __str__(self):
        return 'MongoPool> avail:{0} busy:{1}'.format(
            len(self.__availableconnection),
            len(self.__busyconnection))

    def getConnection(self):
        #print self
        if len(self.__availableconnection) > 0:
            conn = self.__availableconnection.pop()
            self.__busyconnection.append(conn)
            return conn
        else:
            raise Exception('MongoPool: No more connection available')

    def insert(self, table, data):
        con = self.getConnection()
        table = eval("con."+table)
        table.insert(data)
        self.returnToPool(con)

    def find(self, table, query):
        con = self.getConnection()
        table = eval("con."+table)
        qryres = table.find(query)
        self.returnToPool(con)
        return qryres

    def returnToPool(self, conn):
        #print self
        #make connection available
        if conn in self.__busyconnection:
            self.__availableconnection.append(conn)
            self.__busyconnection.remove(conn)
        else:
            raise Exception('MongoPool: ReturnToPool a non busy connection')

    @property
    def availableconnection(self):
        return len(self.__availableconnection)

    @property
    def maxconnection(self):
        return self.__maxconnection

    @maxconnection.setter
    def maxconnection(self, value):
        self.__maxconnection = value
