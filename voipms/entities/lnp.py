# coding=utf-8
"""
The Local Number Portability (LNP) API endpoint

Documentation: https://voip.ms/m/apidocs.php
"""
from voipms.baseapi import BaseApi
from voipms.entities.lnpadd import LNPAdd
from voipms.entities.lnpget import LNPGet


class LNP(BaseApi):
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(LNP, self).__init__(*args, **kwargs)
        self.endoint = 'lnp'
        self.add = LNPAdd(self)
        self.get = LNPGet(self)
