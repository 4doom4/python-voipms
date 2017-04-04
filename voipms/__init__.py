# coding=utf-8
"""
voip.ms v1 REST API SDK

Documentation at https://voip.ms/m/apidocs.php
"""
# API Client
from voipms.voipmsclient import VoipMsClient
# General
from voipms.entities.general import General
from voipms.entities.generalget import GeneralGet
# Accounts
from voipms.entities.accounts import Accounts
from voipms.entities.accountscreate import AccountsCreate
from voipms.entities.accountsdelete import AccountsDelete
from voipms.entities.accountsget import AccountsGet
from voipms.entities.accountsset import AccountsSet
# Call Detail Records
from voipms.entities.calls import Calls
from voipms.entities.callsget import CallsGet
# Clients
from voipms.entities.clients import Clients
from voipms.entities.clientsadd import ClientsAdd
from voipms.entities.clientsget import ClientsGet
from voipms.entities.clientsset import ClientsSet
# DIDs
from voipms.entities.dids import Dids
# Fax
from voipms.entities.fax import Fax
# Voicemail
from voipms.entities.voicemail import Voicemail


class VoipMs(VoipMsClient):
    """
    VoipMS class to communicate with the v1 REST API
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the class with your voip_user and voip_api_password and attach all
        of the endpoints
        """
        super(VoipMs, self).__init__(*args, **kwargs)
        # General
        self.general = General(self)
        self.general.get = GeneralGet(self)
        # Accounts
        self.accounts = Accounts(self)
        self.accounts.create = AccountsCreate(self)
        self.accounts.delete = AccountsDelete(self)
        self.accounts.get = AccountsGet(self)
        self.accounts.set = AccountsSet(self)
        # Calls
        self.calls = Calls(self)
        self.calls.get = CallsGet(self)
        # Clients
        self.clients = Clients(self)
        self.clients.add = ClientsAdd(self)
        self.clients.get = ClientsGet(self)
        self.clients.set = ClientsSet(self)
        # Dids
        self.dids = Dids(self)
        self.fax = Fax(self)
        self.voicemail = Voicemail(self)
