# coding=utf-8
"""
The Calls API endpoint

Documentation: https://voip.ms/m/apidocs.php
"""
from voipms.baseapi import BaseApi
from voipms.entities.callsget import CallsGet


class Calls(BaseApi):
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(Calls, self).__init__(*args, **kwargs)
        self.endoint = 'calls'
        self.get = CallsGet(self)
