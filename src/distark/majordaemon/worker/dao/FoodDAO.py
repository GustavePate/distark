import abc
import argparse
from distarkcli.utils.MyConfiguration import Configuration
from distark.majordaemon.worker.db.mongopool import MongoPool

#TODO pass argument to implementation (kwargs...)
def FoodDAOFactory(*args):
    factory = {}
    factory['REAL'] = FoodDAOMongo
    factory['MOCK'] = FoodDAOMock
    workerdaomockmode = Configuration.getworker()['dbdaoimpl']
    return factory[workerdaomockmode](*args)


class FoodDAO:
    __metaclass__ = abc.ABCMeta

    id = '0'
    name_fr = 'unkown'
    pro = 0.0
    lip = 0.0
    glu = 0.0
    cal = 0.0
    qty = '1'
    unit = 'g'

    def __init__(self, id=None, name_fr=None, pro=None, lip=None, glu=None, cal=None, qty=None, unit=None):
        if id:
            self.id = id
        if name_fr:
            self.name_fr = name_fr
        if pro:
            self.pro = pro
        if lip:
            self.lip = lip
        if glu:
            self.glu = glu
        if qty:
            self.qty = qty
        if unit:
            self.unit = unit

    @staticmethod
    @abc.abstractmethod
    def get(self, id):
        pass

    @abc.abstractmethod
    def save(self):
        pass

    def __str__(self):
        str = ''.join([self.id, ' ', self.name_fr])
        return str


class FoodDAOMongo(FoodDAO):

    def __init__(self, id=None, name_fr='mongo_unknown', pro=0.0, lip=0.0, glu=0.0, cal=0.0, qty=1, unit='g'):
        super(FoodDAOMongo,self).__init__(id, name_fr, pro, lip, glu, cal, qty, unit)

    @staticmethod
    def get(id):
        if id:
            return FoodDAOMock(id, 'a random food')
        else:
            raise(Exception("id not supplied"))

    def save(self):
        pass


class FoodDAOMock(FoodDAO):

    def __init__(self, id=None, name_fr='mock_unknown', pro=0.0, lip=0.0, glu=0.0, cal=0.0, qty=1, unit='g'):
        super(FoodDAOMock,self).__init__(id, name_fr, pro, lip, glu, cal, qty, unit)

    @staticmethod
    def get(id):
        if id:
            return FoodDAOMock(id, 'a random food')
        else:
            raise(Exception("id not supplied"))

    def save(self):
        pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Test objects')
    parser.add_argument('-c', '--conf', help='conf to load', type=str)
    args = parser.parse_args()

    conf = Configuration(args.conf)

    impl = FoodDAOFactory('youpi', 'label')
    print impl
    print type(impl)
    print FoodDAOFactory().get('myid')
