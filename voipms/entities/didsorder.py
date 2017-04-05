# coding=utf-8
"""
The Dids API endpoint order

Documentation: https://voip.ms/m/apidocs.php
"""
from voipms.baseapi import BaseApi
from voipms.helpers import order


class DidsOrder(BaseApi):
    """
    ORder for the Dids endpoint.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(DidsOrder, self).__init__(*args, **kwargs)
        self.endpoint = 'dids'

    def order_did(self, did, routing, pop, dialtime, cnam, billing_type, **kwargs):
        """
        Orders and Adds a new DID Number to the Account

        :param did: [Required] DID to be Ordered (Example: 5552223333)
        :type did: :py:class:`int`
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
        :param account: Reseller Sub Account (Example: '100001_VoIP')
        :type account: :py:class:`str`
        :param monthly: Montly Fee for Reseller Client (Example: 3.50)
        :type monthly: :py:class:`float`
        :param setup: Setup Fee for Reseller Client (Example: 1.99)
        :type setup: :py:class:`float`
        :param minute: Minute Rate for Reseller Client (Example: 0.03)
        :type minute: :py:class:`float`
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
        method = "orderDID"

        kwargs.update({
            "method": method,
            "did": did,
            "routing": routing,
            "pop": pop,
            "dialtime": dialtime,
            "cnam": cnam,
            "billing_type": billing_type,
        })

        return self._voipms_client._get(order(**kwargs))

    def order_did_international_geographic(self, location_id, quantity, routing, pop, dialtime, cnam, billing_type, **kwargs):
        """
        Orders and Adds new International Geographic DID Numbers to the Account

        :param location_id: [Required] ID for a specific International Location (Values from dids.get_dids_international_geographic)
        :type location_id: :py:class:`int`
        :param quantity: [Required] Number of dids to be purchased (Example: 2)
        :type quantity: :py:class:`int`
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
        :param account: Reseller Sub Account (Example: '100001_VoIP')
        :type account: :py:class:`str`
        :param monthly: Montly Fee for Reseller Client (Example: 3.50)
        :type monthly: :py:class:`float`
        :param setup: Setup Fee for Reseller Client (Example: 1.99)
        :type setup: :py:class:`float`
        :param minute: Minute Rate for Reseller Client (Example: 0.03)
        :type minute: :py:class:`float`
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
        method = "orderDIDInternationalGeographic"

        kwargs.update({
            "method": method,
            "location_id": location_id,
            "quantity": quantity,
            "routing": routing,
            "pop": pop,
            "dialtime": dialtime,
            "cnam": cnam,
            "billing_type": billing_type,
        })

        return self._voipms_client._get(order(**kwargs))

    def order_did_international_national(self, location_id, quantity, routing, pop, dialtime, cnam, billing_type, **kwargs):
        """
        Orders and Adds new International National DID Numbers to the Account

        :param location_id: [Required] ID for a specific International Location (Values from dids.get_dids_international_geographic)
        :type location_id: :py:class:`int`
        :param quantity: [Required] Number of dids to be purchased (Example: 2)
        :type quantity: :py:class:`int`
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
        :param account: Reseller Sub Account (Example: '100001_VoIP')
        :type account: :py:class:`str`
        :param monthly: Montly Fee for Reseller Client (Example: 3.50)
        :type monthly: :py:class:`float`
        :param setup: Setup Fee for Reseller Client (Example: 1.99)
        :type setup: :py:class:`float`
        :param minute: Minute Rate for Reseller Client (Example: 0.03)
        :type minute: :py:class:`float`
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
        method = "orderDIDInternationalNational"

        kwargs.update({
            "method": method,
            "location_id": location_id,
            "quantity": quantity,
            "routing": routing,
            "pop": pop,
            "dialtime": dialtime,
            "cnam": cnam,
            "billing_type": billing_type,
        })

        return self._voipms_client._get(order(**kwargs))

    def order_did_international_toll_free(self, location_id, quantity, routing, pop, dialtime, cnam, billing_type, **kwargs):
        """
        Orders and Adds new International TollFree DID Numbers to the Account

        :param location_id: [Required] ID for a specific International Location (Values from dids.get_dids_international_geographic)
        :type location_id: :py:class:`int`
        :param quantity: [Required] Number of dids to be purchased (Example: 2)
        :type quantity: :py:class:`int`
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
        :param account: Reseller Sub Account (Example: '100001_VoIP')
        :type account: :py:class:`str`
        :param monthly: Montly Fee for Reseller Client (Example: 3.50)
        :type monthly: :py:class:`float`
        :param setup: Setup Fee for Reseller Client (Example: 1.99)
        :type setup: :py:class:`float`
        :param minute: Minute Rate for Reseller Client (Example: 0.03)
        :type minute: :py:class:`float`
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
        method = "orderDIDInternationalTollFree"

        kwargs.update({
            "method": method,
            "location_id": location_id,
            "quantity": quantity,
            "routing": routing,
            "pop": pop,
            "dialtime": dialtime,
            "cnam": cnam,
            "billing_type": billing_type,
        })

        return self._voipms_client._get(order(**kwargs))

    def order_did_virtual(self, digits, routing, pop, dialtime, cnam, billing_type, **kwargs):
        """
        Orders and Adds a new Virtual DID Number to the Account

        :param digits: [Required] Three Digits for the new Virtual DID (Example: 001)
        :type digits: :py:class:`int`
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
        :param account: Reseller Sub Account (Example: '100001_VoIP')
        :type account: :py:class:`str`
        :param monthly: Montly Fee for Reseller Client (Example: 3.50)
        :type monthly: :py:class:`float`
        :param setup: Setup Fee for Reseller Client (Example: 1.99)
        :type setup: :py:class:`float`
        :param minute: Minute Rate for Reseller Client (Example: 0.03)
        :type minute: :py:class:`float`
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
        method = "orderDIDVirtual"

        kwargs.update({
            "method": method,
            "digits": digits,
            "routing": routing,
            "pop": pop,
            "dialtime": dialtime,
            "cnam": cnam,
            "billing_type": billing_type,
        })

        return self._voipms_client._get(order(**kwargs))

    def order_toll_free(self, did, routing, pop, dialtime, cnam, billing_type, **kwargs):
        """
        Orders and Adds a new Toll Free Number to the Account

        :param did: [Required] DID to be Ordered (Example: 8772223333)
        :type did: :py:class:`int`
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
        :param account: Reseller Sub Account (Example: '100001_VoIP')
        :type account: :py:class:`str`
        :param monthly: Montly Fee for Reseller Client (Example: 3.50)
        :type monthly: :py:class:`float`
        :param setup: Setup Fee for Reseller Client (Example: 1.99)
        :type setup: :py:class:`float`
        :param minute: Minute Rate for Reseller Client (Example: 0.03)
        :type minute: :py:class:`float`
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
        method = "orderTollFree"

        kwargs.update({
            "method": method,
            "did": did,
            "routing": routing,
            "pop": pop,
            "dialtime": dialtime,
            "cnam": cnam,
            "billing_type": billing_type,
        })

        return self._voipms_client._get(order(**kwargs))

    def order_vanity(self, did, routing, pop, dialtime, cnam, billing_type, carrier, **kwargs):
        """
        Orders and Adds a new Vanity Toll Free Number to the Account

        :param did: [Required] DID to be Ordered (Example: 8772223333)
        :type did: :py:class:`int`
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
        :param carrier: [Required] Carrier for the DID (Values from dids.get_carriers)
        :type carrier: :py:class:`int`
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
        :param account: Reseller Sub Account (Example: '100001_VoIP')
        :type account: :py:class:`str`
        :param monthly: Montly Fee for Reseller Client (Example: 3.50)
        :type monthly: :py:class:`float`
        :param setup: Setup Fee for Reseller Client (Example: 1.99)
        :type setup: :py:class:`float`
        :param minute: Minute Rate for Reseller Client (Example: 0.03)
        :type minute: :py:class:`float`
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
        method = "orderVanity"

        kwargs.update({
            "method": method,
            "did": did,
            "routing": routing,
            "pop": pop,
            "dialtime": dialtime,
            "cnam": cnam,
            "billing_type": billing_type,
            "carrier": carrier,
        })

        return self._voipms_client._get(order(**kwargs))
