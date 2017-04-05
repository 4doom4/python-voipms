# coding=utf-8
"""
The Dids API endpoint back_order

Documentation: https://voip.ms/m/apidocs.php
"""
from voipms.baseapi import BaseApi
from voipms.helpers import order


class DidsBackOrder(BaseApi):
    """
    BackOrder for the Dids endpoint.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(DidsBackOrder, self).__init__(*args, **kwargs)
        self.endpoint = 'dids'

    def back_order_did_can(self, quantity, province, ratecenter, routing, pop, dialtime, cnam, billing_type, **kwargs):
        """
        Backorder DID (USA) from a specific ratecenter and state

        :param quantity: [Required] Number of DIDs to be Ordered (Example: 3)
        :type quantity: :py:class:`int`
        :param province: [Required] Canadian Province  (values from dids.get_provinces)
        :type province: :py:class:`str`
        :param ratecenter: [Required] Canadian Ratecenter (Values from dids.get_rate_centers_can)
        :type ratecenter: :py:class:`str`
        :param routing: [Required] Main Routing for the DID
        :type routing: :py:class:`str`
        :param pop: [Required] Point of Presence for the DID (Example: 5)
        :type pop: :py:class:`int`
        :param dialtime: [Required] Dial Time Out for the DID (Example: 60 -> in seconds)
        :type dialtime: :py:class:`int`
        :param cnam: [Required] CNAM for the DID (Boolean: True/False)
        :type cnam: :py:class:`bool`
        :param billing_type: [Required] Billing type for the DID (1 = Per Minute, 2 = Flat)
        :type billing_type: :py:class:`int`
        :param **kwargs: All optional parameters
        :type **kwargs: :py:class:`dict`

        :param failover_busy: Busy Routing for the DID
        :type failover_busy: :py:class:`str`
        :param failover_unreachable: Unreachable Routing for the DID
        :type failover_unreachable: :py:class:`str`
        :param failover_noanswer: NoAnswer Routing for the DID
        :type failover_noanswer: :py:class:`str`
        :param voicemail: Voicemail for the DID (Example: 101)
        :type voicemail: :py:class:`int`
        :param callerid_prefix: Caller ID Prefix for the DID
        :type callerid_prefix: :py:class:`str`
        :param note: Note for the DID
        :type note: :py:class:`str`
        :param test: Set to True if testing how Orders work
                        - Orders can not be undone
                        - When testing, no Orders are made
        :type test: :py:class:`bool`

        :returns: :py:class:`dict`

        routing, failover_busy, failover_unreachable and failover_noanswer
        can receive values in the following format => header:record_id
        Where header could be: account, fwd, vm, sip, grp, ivr, sys, recording, queue, cb, tc, disa, none.
        Examples:

            account     Used for routing calls to Sub Accounts
                        You can get all sub accounts using the accounts.get_sub_accounts function

            fwd         Used for routing calls to Forwarding entries.
                        You can get the ID right after creating a Forwarding with setForwarding
                        or by requesting all forwardings entries with getForwardings.

            vm          Used for routing calls to a Voicemail.
                        You can get all voicemails and their IDs using the voicemail.get_voicemails function

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
        method = "backOrderDIDCAN"

        kwargs.update({
            "method": method,
            "quantity": quantity,
            "province": province,
            "ratecenter": ratecenter,
            "routing": routing,
            "pop": pop,
            "dialtime": dialtime,
            "cnam": cnam,
            "billing_type": billing_type,
        })

        return self._voipms_client._get(order(**kwargs))

    def back_order_did_usa(self, quantity, state, ratecenter, routing, pop, dialtime, cnam, billing_type, **kwargs):
        """
        Backorder DID (USA) from a specific ratecenter and state

        :param quantity: [Required] Number of DIDs to be Ordered (Example: 3)
        :type quantity: :py:class:`int`
        :param state: [Required] USA State (values from dids.get_states)
        :type state: :py:class:`str`
        :param ratecenter: [Required] USA Ratecenter (Values from dids.get_rate_centers_usa)
        :type ratecenter: :py:class:`str`
        :param routing: [Required] Main Routing for the DID
        :type routing: :py:class:`str`
        :param pop: [Required] Point of Presence for the DID (Example: 5)
        :type pop: :py:class:`int`
        :param dialtime: [Required] Dial Time Out for the DID (Example: 60 -> in seconds)
        :type dialtime: :py:class:`int`
        :param cnam: [Required] CNAM for the DID (Boolean: True/False)
        :type cnam: :py:class:`bool`
        :param billing_type: [Required] Billing type for the DID (1 = Per Minute, 2 = Flat)
        :type billing_type: :py:class:`int`
        :param **kwargs: All optional parameters
        :type **kwargs: :py:class:`dict`

        :param failover_busy: Busy Routing for the DID
        :type failover_busy: :py:class:`str`
        :param failover_unreachable: Unreachable Routing for the DID
        :type failover_unreachable: :py:class:`str`
        :param failover_noanswer: NoAnswer Routing for the DID
        :type failover_noanswer: :py:class:`str`
        :param voicemail: Voicemail for the DID (Example: 101)
        :type voicemail: :py:class:`int`
        :param callerid_prefix: Caller ID Prefix for the DID
        :type callerid_prefix: :py:class:`str`
        :param note: Note for the DID
        :type note: :py:class:`str`
        :param test: Set to True if testing how Orders work
                        - Orders can not be undone
                        - When testing, no Orders are made
        :type test: :py:class:`bool`

        :returns: :py:class:`dict`

        routing, failover_busy, failover_unreachable and failover_noanswer
        can receive values in the following format => header:record_id
        Where header could be: account, fwd, vm, sip, grp, ivr, sys, recording, queue, cb, tc, disa, none.
        Examples:

            account     Used for routing calls to Sub Accounts
                        You can get all sub accounts using the accounts.get_sub_accounts function

            fwd         Used for routing calls to Forwarding entries.
                        You can get the ID right after creating a Forwarding with setForwarding
                        or by requesting all forwardings entries with getForwardings.

            vm          Used for routing calls to a Voicemail.
                        You can get all voicemails and their IDs using the voicemail.get_voicemails function

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
        method = "backOrderDIDUSA"

        kwargs.update({
            "method": method,
            "quantity": quantity,
            "state": state,
            "ratecenter": ratecenter,
            "routing": routing,
            "pop": pop,
            "dialtime": dialtime,
            "cnam": cnam,
            "billing_type": billing_type,
        })

        return self._voipms_client._get(order(**kwargs))
