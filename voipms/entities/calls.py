# coding=utf-8
"""
The Calls API endpoint

Documentation: https://voip.ms/m/apidocs.php
"""
from voipms.baseapi import BaseApi
from voipms.entities.callsdelete import CallsDelete
from voipms.entities.callsget import CallsGet
from voipms.entities.callssend import CallsSend
from voipms.entities.callsset import CallsSet


class Calls(BaseApi):
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(Calls, self).__init__(*args, **kwargs)
        self.endoint = 'calls'
        self.delete = CallsDelete(self)
        self.get = CallsGet(self)
        self.send = CallsSend(self)
        self.set = CallsSet(self)
