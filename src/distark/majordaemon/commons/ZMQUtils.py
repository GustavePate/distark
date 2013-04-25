'''
Created on 25 avr. 2013

@author: guillaume
'''

class ZMQUtils(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    @staticmethod
    def is_valid_envelop(request):
        res=False
        if isinstance(request,list):
            #we don't handle multipart request !
            if len(request)==1:
                res=True
        return res
