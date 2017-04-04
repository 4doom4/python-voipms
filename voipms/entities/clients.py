# coding=utf-8
"""
The Clients API endpoint

Documentation: https://voip.ms/m/apidocs.php
"""
from voipms.baseapi import BaseApi
from voipms.entities.clientsadd import ClientsAdd
from voipms.entities.clientsget import ClientsGet
from voipms.entities.clientsset import ClientsSet


class Clients(BaseApi):
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(Clients, self).__init__(*args, **kwargs)
        self.endoint = 'clients'
        self.add = ClientsAdd(self)
        self.get = ClientsGet(self)
        self.set = ClientsSet(self)
