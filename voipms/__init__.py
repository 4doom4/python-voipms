# coding=utf-8
"""
voip.ms v1 REST API SDK

Documentation at https://voip.ms/m/apidocs.php
"""
# API Client
from voipms.voipmsclient import VoipMsClient
# General
from voipms.entities.general import General
# Accounts
from voipms.entities.accounts import Accounts
# Call Detail Records
from voipms.entities.calls import Calls
# Clients
from voipms.entities.clients import Clients
# DIDs
from voipms.entities.dids import Dids


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
        self.general = General(self)
        self.accounts = Accounts(self)
        self.calls = Calls(self)
        self.clients = Clients(self)
        self.dids = Dids(self)
