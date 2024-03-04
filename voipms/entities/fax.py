# coding=utf-8
"""
The Fax API endpoint

Documentation: https://voip.ms/m/apidocs.php
"""
from voipms.baseapi import BaseApi
from voipms.entities.faxcancel import FaxCancel
from voipms.entities.faxconnect import FaxConnect
from voipms.entities.faxdelete import FaxDelete
from voipms.entities.faxget import FaxGet
from voipms.entities.faxmail import FaxMail
from voipms.entities.faxmove import FaxMove
from voipms.entities.faxorder import FaxOrder
from voipms.entities.faxsearch import FaxSearch
from voipms.entities.faxsend import FaxSend
from voipms.entities.faxset import FaxSet
from voipms.entities.faxunconnect import FaxUnconnect


class Fax(BaseApi):
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(Fax, self).__init__(*args, **kwargs)
        self.endoint = 'fax'
        self.cancel = FaxCancel(self)
        self.connect = FaxConnect(self)
        self.delete = FaxDelete(self)
        self.get = FaxGet(self)
        self.mail = FaxMail(self)
        self.move = FaxMove(self)
        self.order = FaxOrder(self)
        self.search = FaxSearch(self)
        self.send = FaxSend(self)
        self.set = FaxSet(self)
        self.unconnect = FaxUnconnect(self)
