from voipms.baseapi import BaseApi

from voipms.helpers import convert_bool, validate_email, validate_date


class Dids(BaseApi):
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(Dids, self).__init__(*args, **kwargs)
        self.endoint = 'dids'

    def _back_order(self, method, quantity, state, ratecenter, routing, pop, dialtime, cnam, billing_type, **kwargs):
        if not isinstance(quantity, int):
            raise ValueError("Number of DIDs to be Ordered needs to be an int (Example: 3)")

        if not isinstance(state, str):
            if method == "backOrderDIDUSA":
                raise ValueError("USA State needs to be a str (values from dids.get_states)")
            else:
                raise ValueError("Canadian Province needs to be a str (values from dids.get_provinces)")

        if not isinstance(ratecenter, str):
            raise ValueError("USA Ratecenter needs to be a str (Values from dids.get_rate_centers_usa)")

        if not isinstance(routing, int):
            raise ValueError("Main Routing for the DID needs to be an int (Values from accounts.get_routes)")

        if not isinstance(pop, int):
            raise ValueError("Point of Presence for the DID needs to be an int (Example: 5)")

        if not isinstance(dialtime, int):
            raise ValueError("Dial Time Out for the DID needs to be an int (Example: 60 -> in seconds)")

        if not isinstance(cnam, bool):
            raise ValueError("CNAM for the DID needs to be a bool (Boolean: True/False)")

        if not isinstance(billing_type, int):
            raise ValueError("Billing type for the DID needs to be an int (1 = Per Minute, 2 = Flat)")

        parameters = {
            "quantity": quantity,
            "ratecenter": ratecenter,
            "routing": routing,
            "pop": pop,
            "dialtime": dialtime,
            "cnam": convert_bool(cnam),
            "billing_type": billing_type,
        }

        if method == "backOrderDIDUSA":
            parameters["state"] = state
        else:
            parameters["province"] = state

        if "failover_busy" in kwargs:
            if not isinstance(kwargs["failover_busy"], str):
                raise ValueError("Busy Routing for the DID needs to be a str")
            parameters["failover_busy"] = kwargs.pop("failover_busy")

        if "failover_unreachable" in kwargs:
            if not isinstance(kwargs["failover_unreachable"], str):
                raise ValueError("Unreachable Routing for the DID needs to be a str")
            parameters["failover_unreachable"] = kwargs.pop("failover_unreachable")

        if "failover_noanswer" in kwargs:
            if not isinstance(kwargs["failover_noanswer"], str):
                raise ValueError("NoAnswer Routing for the DID")
            parameters["failover_noanswer"] = kwargs.pop("failover_noanswer")

        if "voicemail" in kwargs:
            if not isinstance(kwargs["voicemail"], int):
                raise ValueError("Voicemail for the DID needs to be an int (Example: 101)")
            parameters["voicemail"] = kwargs.pop("voicemail")

        if "country" in kwargs:
            if not isinstance(kwargs["country"], str):
                raise ValueError("Client's Country needs to be a str (Values from general.get_countries)")
            parameters["country"] = kwargs.pop("country")

        if "callerid_prefix" in kwargs:
            if not isinstance(kwargs["callerid_prefix"], str):
                raise ValueError("Caller ID Prefix for the DID needs to be a str")
            parameters["callerid_prefix"] = kwargs.pop("callerid_prefix")

        if "note" in kwargs:
            if not isinstance(kwargs["note"], str):
                raise ValueError("Note for the DID needs to be a str")
            parameters["note"] = kwargs.pop("note")

        if "test" in kwargs:
            if not isinstance(kwargs["test"], bool):
                raise ValueError("Test needs to be a bool (True/False)")
            parameters["test"] = convert_bool(kwargs.pop("test"))

        if len(kwargs) > 0:
            not_allowed_parameters = ""
            for key, value in kwargs.items():
                not_allowed_parameters += key + " "
            raise ValueError("Parameters not allowed: {}".format(not_allowed_parameters))

        return self._voipms_client._get(method, parameters)

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
        """
        method = "backOrderDIDCAN"

        return self._back_order(method, quantity, province, ratecenter, routing, pop, dialtime, cnam, billing_type, **kwargs)

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
        """
        method = "backOrderDIDUSA"

        return self._back_order(method, quantity, state, ratecenter, routing, pop, dialtime, cnam, billing_type, **kwargs)

    def cancel_did(self, did, **kwargs):
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
        """
        method = "cancelDID"

        parameters = {}
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

    def connect_did(self, did, account, monthly, setup, minute, **kwargs):
        """
        Connects a specific DID to a specific Reseller Client Sub Account

        :param did: [Required] DID to be canceled and deleted (Example: 5551234567)
        :type did: :py:class:`str` or `int`
        :param account: [Required] Reseller Sub Account (Example: '100001_VoIP')
        :type account: :py:class:`str`
        :param monthly: [Required] Montly Fee for Reseller Client (Example: 3.50)
        :type monthly: :py:class:`float`
        :param setup: [Required] Setup Fee for Reseller Client (Example: 1.99)
        :type setup: :py:class:`float`
        :param minute: [Required] Minute Rate for Reseller Client (Example: 0.03)
        :type minute: :py:class:`float`
        :param **kwargs: All optional parameters
        :type **kwargs: :py:class:`dict`

        :param next_billing: Next billing date (Example: '2014-03-30')
        :type next_billing: :py:class:`str`
        :param dont_charge_setup: If set to true, the setup value will not be charged after Connect
        :type dont_charge_setup: :py:class:`bool`
        :param dont_charge_monthly: If set to true, the monthly value will not be charged after Connect
        :type dont_charge_monthly: :py:class:`bool`

        :returns: :py:class:`dict`
        """
        method = "connectDID"

        parameters = {}
        if isinstance(did, str):
            did = did.replace('.', '')
            try:
                did = int(did)
            except:
                raise ValueError("DID to be canceled and deleted needs to be an int or str of numbers (Example: 555.123.4567 or 5551234567)")
        if not isinstance(did, int):
            raise ValueError("DID to be canceled and deleted needs to be an int (Example: 5551234567)")

        if not isinstance(account, str):
            raise ValueError("Reseller Sub Account needs to be a str (Example: '100001_VoIP')")

        if not isinstance(monthly, float):
            raise ValueError("Montly Fee for Reseller Client needs to be a float (Example: 3.50)")

        if not isinstance(setup, float):
            raise ValueError("Setup Fee for Reseller Client needs to be a float (Example: 1.99)")

        if not isinstance(minute, float):
            raise ValueError("Minute Rate for Reseller Client needs to be a float (Example: 0.03)")

        parameters = {
            "did": did,
            "account": account,
            "monthly": monthly,
            "setup": setup,
            "minute": minute,
        }

        if "next_billing" in kwargs:
            next_billing = kwargs.pop("next_billing")
            if not isinstance(next_billing, str):
                raise ValueError("Next billing date needs to be a str (Example: '2014-03-30')")
            validate_date(next_billing)
            parameters["next_billing"] = next_billing

        if "dont_charge_setup" in kwargs:
            if not isinstance(kwargs["dont_charge_setup"], bool):
                raise ValueError("If set to True, the setup value will not be charged after Connect (needs to be bool)")
            parameters["dont_charge_setup"] = convert_bool(kwargs.pop("dont_charge_setup"))

        if "dont_charge_monthly" in kwargs:
            if not isinstance(kwargs["dont_charge_monthly"], bool):
                raise ValueError("If set to True, the monthly value will not be charged after Connect (needs to be bool)")
            parameters["dont_charge_monthly"] = convert_bool(kwargs.pop("dont_charge_monthly"))

        if len(kwargs) > 0:
            not_allowed_parameters = ""
            for key, value in kwargs.items():
                not_allowed_parameters += key + " "
            raise ValueError("Parameters not allowed: {}".format(not_allowed_parameters))

        return self._voipms_client._get(method, parameters)

    def del_callback(self, callback):
        """
        Deletes a specific Callback from your Account

        :param callback: [Required] ID for a specific Callback (Example: 19183)
        :type callback: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "delCallback"

        parameters = {}
        if not isinstance(callback, int):
            raise ValueError("ID for a specific Callback needs to be an int (Example: 19183)")
        parameters = {
            "callback": callback
        }

        return self._voipms_client._get(method, parameters)

    def del_caller_id_filtering(self, filtering):
        """
        Deletes a specific CallerID Filtering from your Account

        :param filtering: [Required] ID for a specific CallerID Filtering (Example: 19183)
        :type filtering: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "delCallerIDFiltering"

        parameters = {}
        if not isinstance(filtering, str):
            raise ValueError("ID for a specific CallerID Filtering needs to be an int (Example: 19183)")
        parameters = {
            "filtering": filtering
        }

        return self._voipms_client._get(method, parameters)

    def del_client(self, client):
        """
        Deletes a specific reseller client from your Account

        :param client: [Required] ID for a specific Reseller Client (Example: 1998)
        :type client: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "delClient"

        parameters = {}
        if not isinstance(client, int):
            raise ValueError("ID for a specific Reseller Client needs to be an int (Example: 1998)")
        parameters = {
            "client": client
        }

        return self._voipms_client._get(method, parameters)

    def del_disa(self, disa):
        """
        Deletes a specific DISA from your Account

        :param disa: [Required] ID for a specific DISA (Example: 19183)
        :type disa: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "delDISA"

        parameters = {}
        if not isinstance(disa, int):
            raise ValueError("ID for a specific DISA needs to be an int (Example: 19183)")
        parameters = {
            "disa": disa
        }

        return self._voipms_client._get(method, parameters)

    def delete_sms(self, sms_id):
        """
        Deletes a specific SMS from your Account

        :param sms_id: [Required] ID for a specific SMS (Example: 1918)
        :type sms_id: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "deleteSMS"

        parameters = {}
        if not isinstance(sms_id, int):
            raise ValueError("ID for a specific SMS needs to be an int (Example: 1918)")
        parameters = {
            "id": sms_id
        }

        return self._voipms_client._get(method, parameters)

    def del_forwarding(self, forwarding):
        """
        Deletes a specific Forwarding from your Account

        :param forwarding: [Required] ID for a specific Forwarding (Example: 19183)
        :type forwarding: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "delForwarding"

        parameters = {}
        if not isinstance(forwarding, int):
            raise ValueError("ID for a specific Forwarding needs to be an int (Example: 19183)")
        parameters = {
            "forwarding": forwarding
        }

        return self._voipms_client._get(method, parameters)

    def del_ivr(self, ivr):
        """
        Deletes a specific IVR from your Account

        :param ivr: [Required] ID for a specific IVR (Example: 19183)
        :type ivr: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "delIVR"

        parameters = {}
        if not isinstance(ivr, int):
            raise ValueError("ID for a specific IVR needs to be an int (Example: 19183)")
        parameters = {
            "ivr": ivr
        }

        return self._voipms_client._get(method, parameters)

    def del_phonebook(self, phonebook):
        """
        Deletes a specific Phonebook from your Account

        :param phonebook: [Required] ID for a specific Phonebook (Example: 19183)
        :type phonebook: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "delPhonebook"

        parameters = {}
        if not isinstance(phonebook, int):
            raise ValueError("ID for a specific Phonebook needs to be an int (Example: 19183)")
        parameters = {
            "phonebook": phonebook
        }

        return self._voipms_client._get(method, parameters)

    def del_queue(self, queue):
        """
        Deletes a specific Queue from your Account

        :param queue: [Required] ID for a specific Queue (Example: 13183)
        :type queue: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "delQueue"

        parameters = {}
        if not isinstance(queue, int):
            raise ValueError("ID for a specific Queue needs to be an int (Example: 13183)")
        parameters = {
            "queue": queue
        }

        return self._voipms_client._get(method, parameters)

    def del_recording(self, recording):
        """
        Deletes a specific Recording from your Account

        :param recording: [Required] ID for a specific Recording (Example: 19183)
        :type recording: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "delRecording"

        parameters = {}
        if not isinstance(recording, int):
            raise ValueError("ID for a specific Recording needs to be an int (Example: 19183)")
        parameters = {
            "recording": recording
        }

        return self._voipms_client._get(method, parameters)

    def get_dids_can(self, province, ratecenter=None):
        """
        Retrives a list of Canadian DIDs by Province and Ratecenter

        :param province: [Required] Canadian Province (Values from dids.get_provinces)
        :type province: :py:class:`str`

        :param ratecenter: Canadian Ratecenter (Values from dids.get_rate_centers_can)
        :type ratecenter: :py:class:`str`

        :returns: :py:class:`dict`
        """
        method = "getDIDsCAN"

        parameters = {}
        if not isinstance(province, str):
            raise ValueError("Canadian Province needs to be a str (Values from dids.get_provinces)")
        parameters = {
            "province": province
        }

        if ratecenter:
            if not isinstance(ratecenter, str):
                raise ValueError("Canadian Ratecenter needs to be a str (Values from dids.get_rate_centers_can)")
            else:
                parameters["ratecenter"] = ratecenter

        return self._voipms_client._get(method, parameters)

    def get_provinces(self):
        """
        Retrieves a list of Canadian Provinces

        :returns: :py:class:`dict`
        """
        method = "getProvinces"

        return self._voipms_client._get(method)

    def get_rate_centers_can(self, province):
        """
        Retrieves a list of Canadian Ratecenters by Province

        :param province: [Required] Canadian Province (Values from dids.get_provinces)
        :type province: :py:class:`str`
        :returns: :py:class:`dict`
        """
        method = "getRateCentersCAN"

        parameters = {}
        if province:
            if not isinstance(province, str):
                raise ValueError("Canadian Province needs to be a str (Values from dids.get_provinces)")
            parameters["province"] = province

        return self._voipms_client._get(method, parameters)

    def get_rate_centers_usa(self, state):
        """
        Retrieves a list of USA Ratecenters by State

        :param state: [Required] United States State (Values from dids.get_states)
        :type state: :py:class:`str`
        :returns: :py:class:`dict`
        """
        method = "getRateCentersUSA"

        parameters = {}
        if state:
            if not isinstance(state, str):
                raise ValueError("United States State needs to be a str (Values from dids.get_states)")
            parameters["state"] = state

        return self._voipms_client._get(method, parameters)

    def get_states(self):
        """
        Retrieves a list of USA States

        :returns: :py:class:`dict`
        """
        method = "getStates"

        return self._voipms_client._get(method)
