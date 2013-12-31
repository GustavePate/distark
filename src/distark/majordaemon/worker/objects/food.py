# encoding: utf-8
from distark.commons.protos.objects.food_pb2 import UNIT_GR


class Food(object):

    id = '0'
    name_fr = 'unkown'
    pro = 0.0
    lip = 0.0
    glu = 0.0
    cal = 0.0
    qty = '1'
    unit = 'g'

    def __init__(self, foodDAO=None):
        if foodDAO:
            self._initfromDAO(foodDAO)

    def _initfromDAO(self, foodDAO):



        pass



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
