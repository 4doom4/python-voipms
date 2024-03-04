# coding=utf-8
"""
voip.ms v1 REST API SDK

Documentation at https://voip.ms/m/apidocs.php
"""

# META
__version__ = "0.2.6"
__title__ = "voipms"
__description__ = "Complete REST API for the voip.ms service"
__uri__ = "https://github.com/4doom4/python-voipms"
__doc__ = __description__ + " <" + __uri__ + ">"

__author__ = "Maximilian Ebert and Andrew Langemann"
__email__ = "max.ebert@me.com"

__license__ = "MIT"
__copyright__ = "Copyright (c) 2022"


# API Client
from voipms.voipmsclient import VoipMsClient
# General
from voipms.entities.general import General
from voipms.entities.generalget import GeneralGet
# Accounts
from voipms.entities.accounts import Accounts
from voipms.entities.accountsadd import AccountsAdd
from voipms.entities.accountscreate import AccountsCreate
from voipms.entities.accountsdelete import AccountsDelete
from voipms.entities.accountsget import AccountsGet
from voipms.entities.accountsset import AccountsSet
# Call Detail Records
from voipms.entities.calls import Calls
from voipms.entities.callsdelete import CallsDelete
from voipms.entities.callsget import CallsGet
from voipms.entities.callssend import CallsSend
from voipms.entities.callsset import CallsSet
# Clients
from voipms.entities.clients import Clients
from voipms.entities.clientsadd import ClientsAdd
from voipms.entities.clientsassign import ClientsAssign
from voipms.entities.clientsget import ClientsGet
from voipms.entities.clientsset import ClientsSet
# DIDs
from voipms.entities.dids import Dids
from voipms.entities.didsback_order import DidsBackOrder
from voipms.entities.didscancel import DidsCancel
from voipms.entities.didsconnect import DidsConnect
from voipms.entities.didsdelete import DidsDelete
from voipms.entities.didsget import DidsGet
from voipms.entities.didsorder import DidsOrder
from voipms.entities.didsremove import DidsRemove
from voipms.entities.didssearch import DidsSearch
from voipms.entities.didssend import DidsSend
from voipms.entities.didsset import DidsSet
from voipms.entities.didsunconnect import DidsUnconnect
# E911
from voipms.entities.e911 import E911
# Fax
from voipms.entities.fax import Fax
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
# Local Number Portability (LNP)
from voipms.entities.lnp import LNP
from voipms.entities.lnpadd import LNPAdd
from voipms.entities.lnpget import LNPGet
# Voicemail
from voipms.entities.voicemail import Voicemail
from voipms.entities.voicemailcreate import VoicemailCreate
from voipms.entities.voicemaildelete import VoicemailDelete
from voipms.entities.voicemailget import VoicemailGet
from voipms.entities.voicemailmark import VoicemailMark
from voipms.entities.voicemailmove import VoicemailMove
from voipms.entities.voicemailsend import VoicemailSend
from voipms.entities.voicemailset import VoicemailSet


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
        self.accounts.add = AccountsAdd(self)
        self.accounts.create = AccountsCreate(self)
        self.accounts.delete = AccountsDelete(self)
        self.accounts.get = AccountsGet(self)
        self.accounts.set = AccountsSet(self)
        # Calls
        self.calls = Calls(self)
        self.calls.delete = CallsDelete(self)
        self.calls.get = CallsGet(self)
        self.calls.send = CallsSend(self)
        self.calls.set = CallsSet(self)
        # Clients
        self.clients = Clients(self)
        self.clients.add = ClientsAdd(self)
        self.clients.assign = ClientsAssign(self)
        self.clients.get = ClientsGet(self)
        self.clients.set = ClientsSet(self)
        # E911
        self.e911 = E911(self)
        # Dids
        self.dids = Dids(self)
        self.dids.back_order = DidsBackOrder(self)
        self.dids.cancel = DidsCancel(self)
        self.dids.connect = DidsConnect(self)
        self.dids.delete = DidsDelete(self)
        self.dids.get = DidsGet(self)
        self.dids.order = DidsOrder(self)
        self.dids.remove = DidsRemove(self)
        self.dids.search = DidsSearch(self)
        self.dids.send = DidsSend(self)
        self.dids.set = DidsSet(self)
        self.dids.unconnect = DidsUnconnect(self)
        # Fax
        self.fax = Fax(self)
        self.fax.cancel = FaxCancel(self)
        self.fax.connect = FaxConnect(self)
        self.fax.delete = FaxDelete(self)
        self.fax.get = FaxGet(self)
        self.fax.mail = FaxMail(self)
        self.fax.move = FaxMove(self)
        self.fax.order = FaxOrder(self)
        self.fax.search = FaxSearch(self)
        self.fax.send = FaxSend(self)
        self.fax.set = FaxSet(self)
        self.fax.unconnect = FaxUnconnect(self)
        # Local Number Portability (LNP)
        self.lnp = LNP(self)
        self.lnp.add = LNPAdd(self)
        self.lnp.get = LNPGet(self)
        # Voicemail
        self.voicemail = Voicemail(self)
        self.voicemail.create = VoicemailCreate(self)
        self.voicemail.delete = VoicemailDelete(self)
        self.voicemail.get = VoicemailGet(self)
        self.voicemail.mark = VoicemailMark(self)
        self.voicemail.move = VoicemailMove(self)
        self.voicemail.send = VoicemailSend(self)
        self.voicemail.set = VoicemailSet(self)
