# coding=utf-8
"""
The General API endpoint

Documentation: https://voip.ms/m/apidocs.php
"""
from voipms.baseapi import BaseApi
from voipms.entities.generalget import GeneralGet


class General(BaseApi):
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(General, self).__init__(*args, **kwargs)
        self.endoint = 'general'
        self.get = GeneralGet(self)
