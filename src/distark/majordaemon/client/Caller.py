'''
Created on 27 avr. 2013

@author: guillaume
'''

from distark.majordaemon.client.services.simpleservice import  SimpleService,SimpleRequest,SimpleResponse

class Caller(object):
    
    def __init__(self):
        pass
    
    def main(self):
        print 'caller: prepare request'
        request=SimpleRequest()
        request.setYoupla('youpla?')
        ss=SimpleService(request)
        #blocking call
        response=ss.getResponse()
        
        if response[0] == ss.associated_pb_response:
            print 'caller: handler',response[1].getBoum()
            func_error=False
            if func_error:
                print 'functional error handling ...'
        else:
            #TODO: add helper here
            print 'caller: technical error handling...'
        
if __name__ == '__main__':
    caller=Caller()
    caller.main()