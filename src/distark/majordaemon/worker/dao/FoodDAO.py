# encoding: utf-8
import abc
import argparse
import traceback
from distarkcli.utils.MyConfiguration import Configuration
from distark.majordaemon.worker.db.mongopool import MongoPool

from distark.commons.protos.objects.food_pb2 import UNIT_GR

#TODO pass argument to implementation (kwargs...)
def FoodDAOFactory(id=None, name_fr=None, pro=None, lip=None, glu=None, cal=None, qty=None, unit=None):
    factory = {}
    factory['REAL'] = FoodDAOMongo
    factory['MOCK'] = FoodDAOMock
    workerdaomockmode = Configuration.getworker()['dbdaoimpl']
    return factory[workerdaomockmode](id, name_fr, pro, lip, glu, cal, qty, unit)


class FoodDAO:
    __metaclass__ = abc.ABCMeta
    MAX_SEARCH_RESULTS = 100
    more_results = False

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

    @abc.abstractmethod
    def get(self, id):
        pass

    @abc.abstractmethod
    def save(self):
        pass

    @staticmethod
    @abc.abstractmethod
    def searchFoodByPattern():
        try:
            pass
        except:
            print 'abstarct'

    def __str__(self):
        str = ''.join([self.id, ' ', self.name_fr])
        return str

    def fillInPBFood(self, pbf):
        pbf.id = self.id
        pbf.name = self.name_fr
        pbf.cal = self.cal
        pbf.pro = self.pro
        pbf.glu = self.glu
        pbf.lip = self.lip
        pbf.qty = self.qty
        pbf.qty_unit = UNIT_GR

    def fillInPbSearchFoodResponse(self, pbsearchfoodresponse):
        pbfood = pbsearchfoodresponse.foods.add()
        self.fillInPBFood(pbfood)


class FoodDAOMongo(FoodDAO):

    def __init__(self, id=None, name_fr='mongo_unknown', pro=0.0, lip=0.0, glu=0.0, cal=0.0, qty=1, unit='g'):
        super(FoodDAOMongo, self).__init__(id, name_fr, pro, lip, glu, cal, qty, unit)

    @staticmethod
    def get(id):
        if id:
            return FoodDAOMock(id, 'a random food')
        else:
            raise(Exception("id not supplied"))

    @staticmethod
    def searchFoodByPattern(pattern):
        res = []
        try:
            mp = MongoPool()
            qryres = mp.find("food.fooddb", {'name_fr':
                                            {'$regex': '.*' + pattern
                                                + '.*',
                                                '$options': 'i'}
                                             })
            print 'allo3'
            if qryres:
                print 'allo', qryres.count()
            else:
                print 'None'
            if qryres.count() > 0:
                #build response of at more MAX_RESULT rec
                cpt = 1
                for r in qryres:
                    f = FoodDAOMongo()
                    f._initfrommongo(r)
                    res.append(f)

                    if cpt >= FoodDAO.MAX_SEARCH_RESULTS:
                        FoodDAO.more_results = True
                        break
                    cpt += 1
        except:
            traceback.print_exc()
            raise
        finally:
            return res

    def _initfrommongo(self, mongodata):
        self.id = str(mongodata[u'_id'])
        self.name_fr = mongodata[u'name_fr']
        self.pro = mongodata[u'pro']
        self.lip = mongodata[u'lip']
        self.glu = mongodata[u'glu']
        self.qty = mongodata[u'qty']

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

    @staticmethod
    def searchFoodByPattern(pattern):
        list = []
        list.append(FoodDAOMock('1', 'random food 1' + pattern))
        list.append(FoodDAOMock('2', 'random food 2' + pattern))
        list.append(FoodDAOMock('3', 'random food 3' + pattern))
        list.append(FoodDAOMock('4', 'random food 4' + pattern))
        return list

    def save(self):
        pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Test objects')
    parser.add_argument('-c', '--conf', help='conf to load', type=str)
    args = parser.parse_args()

    #init conf
    conf = Configuration(args.conf)
    #init mongo pool
    mp = MongoPool(Configuration.getworker()['mongo']['host'],
                   Configuration.getworker()['mongo']['port'],
                   Configuration.getworker()['mongo']['db'])

    impl = FoodDAOFactory('youpi', 'label')
    print impl
    print type(impl)
    print FoodDAOFactory().get('myid')
    fdao = FoodDAOFactory()

    try:
        res = fdao.searchFoodByPattern('an')
    except:
        print 'we got an error'
    finally:
        print res
