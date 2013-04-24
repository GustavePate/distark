'''
Created on 24 avr. 2013

@author: guillaume
'''

import netinfo

class NetInfo(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
    @staticmethod
    def getSystemIfs():
        return netinfo.list_active_devs()
    
    @staticmethod
    def getSystemIps():
        """ will not return the localhost one """
        IPs = []
        for interface in NetInfo.getSystemIfs():
            if not interface.startswith('lo'):
                ip = netinfo.get_ip(interface)
                IPs.append(ip)
        return IPs
    
    @staticmethod
    def getIPString():
        """ return comma delimited string of all the system IPs"""
        return ",".join(NetInfo.getSystemIps())