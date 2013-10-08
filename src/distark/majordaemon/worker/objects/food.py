# encoding: utf-8


class Food(object):

    id='0'
    name='unkown'
    pro=0.0
    lip=0.0
    glu=0.0
    cal=0.0
    qty='1'
    unit='g'

    def __init__(self, mongodata=None):
        if mongodata:
            self._initfrommongo(mongodata)

    def _initfrommongo(mongodata):
        pass

    def fillInPbSearchFood(pbsearchfood):
        pass
