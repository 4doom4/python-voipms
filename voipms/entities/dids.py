# coding=utf-8
"""
The Dids API endpoint

Documentation: https://voip.ms/m/apidocs.php
"""
from voipms.baseapi import BaseApi
from voipms.entities.didsback_order import DidsBackOrder
from voipms.entities.didscancel import DidsCancel
from voipms.entities.didsconnect import DidsConnect
from voipms.entities.didsdelete import DidsDelete
from voipms.entities.didsget import DidsGet
from voipms.entities.didsorder import DidsOrder
from voipms.entities.didssearch import DidsSearch
from voipms.entities.didssend import DidsSend
from voipms.entities.didsset import DidsSet
from voipms.entities.didsunconnect import DidsUnconnect


class Dids(BaseApi):
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(Dids, self).__init__(*args, **kwargs)
        self.endoint = 'dids'
        self.back_order = DidsBackOrder(self)
        self.cancel = DidsCancel(self)
        self.connect = DidsConnect(self)
        self.delete = DidsDelete(self)
        self.get = DidsGet(self)
        self.order = DidsOrder(self)
        self.search = DidsSearch(self)
        self.send = DidsSend(self)
        self.set = DidsSet(self)
        self.unconnect = DidsUnconnect(self)
