# coding=utf-8
"""
The Dids API endpoint cancel

Documentation: https://voip.ms/m/apidocs.php
"""
from voipms.baseapi import BaseApi
from voipms.helpers import convert_bool


class DidsCancel(BaseApi):
    """
    Cancel for the Dids endpoint.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(DidsCancel, self).__init__(*args, **kwargs)
        self.endpoint = 'dids'

    def did(self, did, **kwargs):
        """
        Deletes a specific DID from your Account

        :param did: [Required] DID to be canceled and deleted (Example: 5551234567)
        :type did: :py:class:`str` or `int`
        :param **kwargs: All optional parameters
        :type **kwargs: :py:class:`dict`

        :param cancelcomment: Comment for DID cancellation
        :type cancelcomment: :py:class:`str`
        :param portout: Set to True if the DID is being ported out
        :type portout: :py:class:`bool`
        :param test: Set to True if testing how cancellation works
                                - Cancellation can not be undone
                                - When testing, no changes are made
        :type test: :py:class:`bool`

        :returns: :py:class:`dict`

        routing, failover_busy, failover_unreachable and failover_noanswer
        can receive values in the following format => header:record_id
        Where header could be: account, fwd, vm, sip, grp, ivr, sys, recording, queue, cb, tc, disa, none.
        Examples:

            account     Used for routing calls to Sub Accounts
                        You can get all sub accounts using the accounts.get.sub_accounts function

            fwd         Used for routing calls to Forwarding entries.
                        You can get the ID right after creating a Forwarding with dids.set.forwarding
                        or by requesting all forwardings entries with getForwardings.

            vm          Used for routing calls to a Voicemail.
                        You can get all voicemails and their IDs using the voicemail.get.voicemails function

            sys         System Options:
                        hangup       = Hangup the Call
                        busy         = Busy tone
                        noservice    = System Recording: Number not in service
                        disconnected = System Recording: Number has been disconnected
                        dtmf         = DTMF Test
                        echo         = ECHO Test


            none        Used to route calls to no action

        Examples:
            'account:100001_VoIP'
            'fwd:1026'
            'vm:101'
            'none:'
            'sys:echo'
        """
        method = "cancelDID"

        if isinstance(did, str):
            did = did.replace('.', '')
            try:
                did = int(did)
            except:
                raise ValueError("DID to be canceled and deleted needs to be an int or str of numbers (Example: 555.123.4567 or 5551234567)")
        if not isinstance(did, int):
            raise ValueError("DID to be canceled and deleted needs to be an int (Example: 5551234567)")
        parameters = {
            "did": did
        }

        if "portout" in kwargs:
            if not isinstance(kwargs["portout"], bool):
                raise ValueError("Set to True if the DID is being ported out")
            parameters["portout"] = convert_bool(kwargs.pop("portout"))

        if "test" in kwargs:
            if not isinstance(kwargs["test"], bool):
                raise ValueError("Set to True if testing how cancellation works")
            parameters["test"] = convert_bool(kwargs.pop("test"))

        if len(kwargs) > 0:
            not_allowed_parameters = ""
            for key, value in kwargs.items():
                not_allowed_parameters += key + " "
            raise ValueError("Parameters not allowed: {}".format(not_allowed_parameters))

        return self._voipms_client._get(method, parameters)
