# coding=utf-8
"""
The Accounts API endpoint

Documentation: https://voip.ms/m/apidocs.php
"""
from voipms.baseapi import BaseApi
from voipms.entities.accountscreate import AccountsCreate
from voipms.entities.accountsdelete import AccountsDelete
from voipms.entities.accountsget import AccountsGet
from voipms.entities.accountsset import AccountsSet


class Accounts(BaseApi):
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(Accounts, self).__init__(*args, **kwargs)
        self.endoint = 'accounts'
        self.create = AccountsCreate(self)
        self.delete = AccountsDelete(self)
        self.get = AccountsGet(self)
        self.set = AccountsSet(self)
