# coding=utf-8
"""
The Dids API endpoint set

Documentation: https://voip.ms/m/apidocs.php
"""
from voipms.baseapi import BaseApi
from voipms.helpers import convert_bool, validate_email


class DidsSet(BaseApi):
    """
    Set for the Dids endpoint.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(DidsSet, self).__init__(*args, **kwargs)
        self.endpoint = 'dids'

    def callback(self, description, number, delay_before, response_timeout, digit_timeout, **kwargs):
        """
        Updates a specific Callback if a callback code is provided

        - Adds a new Callback entry if no callback code is provided

        :param description: [Required] Description for the Callback
        :type description: :py:class:`str`
        :param number: [Required] Number that will be called back
        :type number: :py:class:`int`
        :param delay_before: [Required] Delay befor calling back
        :type delay_before: :py:class:`int`
        :param response_timeout: [Required] Time before hanging up for incomplete input
        :type response_timeout: :py:class:`int`
        :param digit_timeout: [Required] Time between digits input
        :type digit_timeout: :py:class:`int`

        :param callback: ID for a specific Callback (Example: 2359 / Leave empty to create a new one)
        :type callback: :py:class:`int`
        :param callerid_number: Caller ID Override for the callback
        :type callerid_number: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "setCallback"

        if not isinstance(description, str):
            raise ValueError("Description for the Callback needs to be a str")

        if not isinstance(number, int):
            raise ValueError("Number that will be called back needs to be an int")

        if not isinstance(delay_before, int):
            raise ValueError("Delay befor calling back needs to be an int")

        if not isinstance(response_timeout, int):
            raise ValueError("Time before hanging up for incomplete input needs to be an int")

        if not isinstance(digit_timeout, int):
            raise ValueError("Time between digits input needs to be an int")

        parameters = {
            "description": description,
            "number": number,
            "delay_before": delay_before,
            "response_timeout": response_timeout,
            "digit_timeout": digit_timeout,
        }

        if "callback" in kwargs:
            if not isinstance(kwargs["callback"], int):
                raise ValueError("ID for a specific Callback needs to be an int (Example: 2359 / Leave empty to create a new one)")
            parameters["callback"] = kwargs.pop("callback")

        if "callerid_number" in kwargs:
            if not isinstance(kwargs["callerid_number"], int):
                raise ValueError("Caller ID Override for the callback needs to be an int")
            parameters["callerid_number"] = kwargs.pop("callerid_number")

        if len(kwargs) > 0:
            not_allowed_parameters = ""
            for key, value in kwargs.items():
                not_allowed_parameters += key + " "
            raise ValueError("Parameters not allowed: {}".format(not_allowed_parameters))

        return self._voipms_client._get(method, parameters)

    def caller_id_filtering(self, callerid, did, routing, **kwargs):
        """
        Updates a specific Caller ID Filtering if a filtering code is provided

        - Adds a new Caller ID Filtering if no filtering code is provided

        :param callerid: [Required] Caller ID that triggers the Filter (i = Non USA, 0 = Anonymous, NPANXXXXXX)
        :type callerid: :py:class:`str`
        :param did: [Required] DIDs affected by the filter (all, NPANXXXXXX)
        :type did: :py:class:`str`
        :param routing: [Required] Route the call follows when filter is triggered
        :type routing: :py:class:`str`

        :param filter: ID for a specific Caller ID Filtering (Example: 18915 / Leave empty to create a new one)
        :type filter: :py:class:`int`
        :param failover_unreachable: Route the call follows when unreachable
        :type failover_unreachable: :py:class:`str`
        :param failover_busy: Route the call follows when busy
        :type failover_busy: :py:class:`str`
        :param failover_noanswer: Route the call follows when noanswer
        :type failover_noanswer: :py:class:`str`
        :param note: Note for the Caller ID Filtering
        :type note: :py:class:`str`

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
        method = "setCallerIDFiltering"

        if not isinstance(callerid, str):
            raise ValueError("Caller ID that triggers the Filter needs to be a str (i = Non USA, 0 = Anonymous, NPANXXXXXX)")

        if not isinstance(did, str):
            raise ValueError("DIDs affected by the filter needs to be a str (all, NPANXXXXXX)")

        if not isinstance(routing, str):
            raise ValueError("Route the call follows when filter is triggered needs to be a str")

        parameters = {
            "callerid": callerid,
            "did": did,
            "routing": routing,
        }

        if "filter" in kwargs:
            if not isinstance(kwargs["filter"], int):
                raise ValueError("ID for a specific Caller ID Filtering needs to be an int (Example: 18915 / Leave empty to create a new one)")
            parameters["filter"] = kwargs.pop("filter")

        if "failover_unreachable" in kwargs:
            if not isinstance(kwargs["failover_unreachable"], str):
                raise ValueError("Route the call follows when unreachable needs to be a str")
            parameters["failover_unreachable"] = kwargs.pop("failover_unreachable")

        if "failover_busy" in kwargs:
            if not isinstance(kwargs["failover_busy"], str):
                raise ValueError("Route the call follows when busy to be a str")
            parameters["failover_busy"] = kwargs.pop("failover_busy")

        if "failover_noanswer" in kwargs:
            if not isinstance(kwargs["failover_noanswer"], str):
                raise ValueError("Route the call follows when noanswer needs to be a str")
            parameters["failover_noanswer"] = kwargs.pop("failover_noanswer")

        if "note" in kwargs:
            if not isinstance(kwargs["note"], str):
                raise ValueError("Note for the Caller ID Filtering needs to be a str")
            parameters["note"] = kwargs.pop("note")

        if len(kwargs) > 0:
            not_allowed_parameters = ""
            for key, value in kwargs.items():
                not_allowed_parameters += key + " "
            raise ValueError("Parameters not allowed: {}".format(not_allowed_parameters))

        return self._voipms_client._get(method, parameters)

    def did_billing_type(self, did, billing_type):
        """
        Updates the Billing Plan from a specific DID

        :param did: [Required] DID affected by the new billing plan
        :type did: :py:class:`int`
        :param billing_type: [Required] Billing type for the DID (1 = Per Minute, 2 = Flat)
        :type billing_type: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "setDIDBillingType"

        if not isinstance(did, int):
            raise ValueError("DID affected by the new billing plan needs to be an int")

        if not isinstance(billing_type, int):
            raise ValueError("Billing type for the DID needs to be an int (1 = Per Minute, 2 = Flat)")

        parameters = {
            "did": did,
            "billing_type": billing_type,
        }

        return self._voipms_client._get(method, parameters)

    def did_info(self, did, routing, pop, dialtime, cnam, billing_type, **kwargs):
        """
        Updates the information from a specific DID

        :param did: [Required] DID to be Ordered (Example: 5551234567)
        :type did: :py:class:`int`
        :param routing: [Required] Main Routing for the DID
        :type routing: :py:class:`str`
        :param pop: [Required] Point of Presence for the DID (Example: 3)
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
        method = "setDIDInfo"

        kwargs.update({
            "method": method,
            "did": did,
            "routing": routing,
            "pop": pop,
            "dialtime": dialtime,
            "cnam": cnam,
            "billing_type": billing_type,
        })

        return self._order(**kwargs)

    def did_pop(self, did, pop):
        """
        Updates the POP from a specific DID

        :param did: [Required] DID affected by the new billing plan
        :type did: :py:class:`int`
        :param pop: [Required] Point of Presence for the DID ("server_pop" values from general.get_servers_info Example: 3)
        :type pop: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "setDIDPOP"

        if not isinstance(did, int):
            raise ValueError("DID affected by the new billing plan needs to be an int")

        if not isinstance(pop, int):
            raise ValueError("Point of Presence for the DID needs to be an int ('server_pop' values from general.get_servers_info() Example: 3)")

        parameters = {
            "did": did,
            "pop": pop,
        }

        return self._voipms_client._get(method, parameters)

    def did_routing(self, did, routing):
        """
        Updates the Routing from a specific DID

        :param did: [Required] DID affected by the new billing plan
        :type did: :py:class:`int`
        :param routing: [Required] Main Routing for the DID
        :type routing: :py:class:`str`

        :returns: :py:class:`dict`

        routing can receive values in the following format => header:record_id
        Where header could be: account, fwd, vm, sip, grp, ivr, sys, recording, queue, cb, tc, disa, none.
        Examples:

            account     Used for routing calls to Sub Accounts
                        You can get all sub accounts using the accounts.get_sub_accounts function

            fwd         Used for routing calls to Forwarding entries.
                        You can get the ID right after creating a Forwarding with setForwarding
                        or by requesting all forwardings entries with getForwardings.

            vm          Used for routing calls to a Voicemail.
                        You can get all voicemails and their IDs using the voicemail.get_voicemails function

        Examples:
            'account:100001_VoIP'
            'fwd:1026'
            'vm:101'
        """
        method = "setDIDRouting"

        if not isinstance(did, int):
            raise ValueError("DID affected by the new billing plan needs to be an int")

        if not isinstance(routing, str):
            raise ValueError("Main Routing for the DID needs to be a str")

        parameters = {
            "did": did,
            "routing": routing,
        }

        return self._voipms_client._get(method, parameters)

    def did_voicemail(self, did, voicemail=None):
        """
        Updates the Voicemail from a specific DID

        :param did: [Required] DID affected by the new billing plan
        :type did: :py:class:`int`

        :param voicemail: Mailbox for the DID (Example: 101)
        :type voicemail: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "setDIDVoicemail"

        if not isinstance(did, int):
            raise ValueError("DID affected by the new billing plan needs to be an int")

        parameters = {
            "did": did,
        }

        if voicemail:
            if not isinstance(voicemail, int):
                raise ValueError("Mailbox for the DID needs to be an int (Example: 101)")
            else:
                parameters["voicemail"] = voicemail

        return self._voipms_client._get(method, parameters)

    def disa(self, name, pin, digit_timeout, **kwargs):
        """
        Updates a specific DISA if a disa code is provided

        - Adds a new DISA entry if no disa code is provided

        :param name: [Required] Name for the DISA
        :type name: :py:class:`str`
        :param pin: [Required] Password for the DISA
        :type pin: :py:class:`int`
        :param digit_timeout: [Required] Time between digits
        :type digit_timeout: :py:class:`int`

        :param disa: ID for a specific DISA (Example: 2114 / Leave empty to create a new one)
        :type disa: :py:class:`int`
        :param callerid_override: Caller ID Override for the DISA
        :type callerid_override: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "setDISA"

        if not isinstance(name, str):
            raise ValueError("Name for the DISA needs to be a str")

        if not isinstance(pin, int):
            raise ValueError("Password for the DISA needs to be an int")

        if not isinstance(digit_timeout, int):
            raise ValueError("Time between digits needs to be an int")

        parameters = {
            "name": name,
            "pin": pin,
            "digit_timeout": digit_timeout,
        }

        if "disa" in kwargs:
            if not isinstance(kwargs["disa"], int):
                raise ValueError("ID for a specific DISA needs to be an int (Example: 2114 / Leave empty to create a new one)")
            parameters["disa"] = kwargs.pop("disa")

        if "callerid_override" in kwargs:
            if not isinstance(kwargs["callerid_override"], int):
                raise ValueError("Caller ID Override for the DISA needs to be an int")
            parameters["callerid_override"] = kwargs.pop("callerid_override")

        if len(kwargs) > 0:
            not_allowed_parameters = ""
            for key, value in kwargs.items():
                not_allowed_parameters += key + " "
            raise ValueError("Parameters not allowed: {}".format(not_allowed_parameters))

        return self._voipms_client._get(method, parameters)

    def forwarding(self, phone_number, **kwargs):
        """
        Updates a specific Forwarding if a fwd code is provided

        - Adds a new Forwarding entry if no fwd code is provided

        :param phone_number: [Required] Phone Number for the Forwarding
        :type phone_number: :py:class:`int`

        :param forwarding: ID for a specific Forwarding (Example: 19183 / Leave empty to create a new one)
        :type forwarding: :py:class:`int`
        :param callerid_override: Caller ID Override for the Forwarding
        :type callerid_override: :py:class:`int`
        :param description: Description for the Forwarding
        :type description: :py:class:`str`
        :param dtmf_digits:  Send DTMF digits when call is answered
        :type dtmf_digits: :py:class:`str`
        :param pause: Pause (seconds) when call is answered before sending digits (Example: 1.5 / Values: 0 to 10 in increments of 0.5)
        :type pause: :py:class:`float`

        :returns: :py:class:`dict`
        """
        method = "setForwarding"

        if not isinstance(phone_number, int):
            raise ValueError("Phone Number for the Forwarding needs to be an int")

        parameters = {
            "phone_number": phone_number,
        }

        if "forwarding" in kwargs:
            if not isinstance(kwargs["forwarding"], int):
                raise ValueError("ID for a specific Forwarding needs to be an int (Example: 19183 / Leave empty to create a new one)")
            parameters["forwarding"] = kwargs.pop("forwarding")

        if "callerid_override" in kwargs:
            if not isinstance(kwargs["callerid_override"], int):
                raise ValueError("Caller ID Override for the Forwarding needs to be an int")
            parameters["callerid_override"] = kwargs.pop("callerid_override")

        if "description" in kwargs:
            if not isinstance(kwargs["description"], str):
                raise ValueError("Description for the Forwarding needs to be a str")
            parameters["description"] = kwargs.pop("description")

        if "dtmf_digits" in kwargs:
            if not isinstance(kwargs["dtmf_digits"], str):
                raise ValueError("Send DTMF digits when call is answered needs to be a str")
            parameters["dtmf_digits"] = kwargs.pop("dtmf_digits")

        if "pause" in kwargs:
            if not isinstance(kwargs["pause"], float):
                raise ValueError("Pause (seconds) when call is answered before sending digits needs to be a float (Example: 1.5 / Values: 0 to 10 in increments of 0.5)")
            parameters["pause"] = kwargs.pop("pause")

        if len(kwargs) > 0:
            not_allowed_parameters = ""
            for key, value in kwargs.items():
                not_allowed_parameters += key + " "
            raise ValueError("Parameters not allowed: {}".format(not_allowed_parameters))

        return self._voipms_client._get(method, parameters)

    def ivr(self, name, recording, timeout, language, voicemailsetup, choices, ivr=None):
        """
        Updates a specific IVR if an IVR code is provided

        - Adds a new IVR entry if no IVR code is provided

        :param name: [Required] Name for the IVR
        :type name: :py:class:`str`
        :param recording: [Required] Recording for the IVR (values from dids.get_recordings)
        :type recording: :py:class:`int`
        :param timeout: [Required] Maximum time for type in a choice after recording
        :type timeout: :py:class:`int`
        :param language: [Required] Language for the IVR (values from general.get_languages)
        :type language: :py:class:`str`
        :param voicemailsetup: [Required] Voicemail Setup for the IVR (values from dids.get_voicemail_setups)
        :type voicemailsetup: :py:class:`int`
        :param choices: [Required] Choices for the IVR (Example: '1=sip:5096 ; 2=fwd:20222')
        :type choices: :py:class:`str`

        :param voicemail: ID for a specific IVR (Example: 4636 / Leave empty to create a new one)
        :type voicemail: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "setIVR"

        if not isinstance(name, str):
            raise ValueError("Name for the IVR needs to be a str")

        if not isinstance(recording, int):
            raise ValueError("Recording for the IVR needs to be an int (values from dids.get_recordings)")

        if not isinstance(timeout, int):
            raise ValueError("Maximum time for type in a choice after recording needs to be an int")

        if not isinstance(language, str):
            raise ValueError("Language for the IVR to be a str (values from general.get_languages)")

        if not isinstance(voicemailsetup, int):
            raise ValueError("Voicemail Setup for the IVR to be an int (values from dids.get_voicemail_setups)")

        if not isinstance(choices, str):
            raise ValueError("Choices for the IVR to be a str (Example: '1=sip:5096 ; 2=fwd:20222')")

        parameters = {
            "name": name,
            "recording": recording,
            "timeout": timeout,
            "language": language,
            "voicemailsetup": voicemailsetup,
            "choices": choices,
        }

        if ivr:
            if not isinstance(ivr, int):
                raise ValueError("ID for a specific IVR needs to be an int (Example: 4636 / Leave empty to create a new one)")
            else:
                parameters["ivr"] = ivr

        return self._voipms_client._get(method, parameters)

    def phonebook(self, name, number, **kwargs):
        """
        Updates a specific Phonebook entry if a phonebook code is provided

        - Adds a new Phonebook entry if no phonebook code is provided

        :param name: [Required] Name for the Phonebook Entry
        :type name: :py:class:`str`
        :param number: [Required] Number or SIP for the Phonebook entry (Example: 'sip:2563' or '5552223333')
        :type number: :py:class:`str`

        :param phonebook: ID for a specific Phonebook entry (Example: 32207 / Leave empty to create a new one)
        :type phonebook: :py:class:`int`
        :param speed_dial: Speed Dial for the Phonebook entry
        :type speed_dial: :py:class:`str`
        :param callerid: Caller ID Override when dialing via Speed Dial
        :type callerid: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "setPhonebook"

        if not isinstance(name, str):
            raise ValueError("Name for the Phonebook Entry needs to be a str")

        if not isinstance(number, str):
            raise ValueError("Number or SIP for the Phonebook entry needs to be a str (Example: 'sip:2563' or '5552223333')")

        parameters = {
            "name": name,
            "number": number,
        }

        if "phonebook" in kwargs:
            if not isinstance(kwargs["phonebook"], int):
                raise ValueError("ID for a specific Phonebook entry needs to be an int (Example: 32207 / Leave empty to create a new one)")
            parameters["phonebook"] = kwargs.pop("phonebook")

        if "speed_dial" in kwargs:
            if not isinstance(kwargs["speed_dial"], str):
                raise ValueError("Speed Dial for the Phonebook entry needs to be a str")
            parameters["speed_dial"] = kwargs.pop("speed_dial")

        if "callerid" in kwargs:
            if not isinstance(kwargs["callerid"], int):
                raise ValueError("Caller ID Override when dialing via Speed Dial needs to be an int")
            parameters["callerid"] = kwargs.pop("callerid")

        if len(kwargs) > 0:
            not_allowed_parameters = ""
            for key, value in kwargs.items():
                not_allowed_parameters += key + " "
            raise ValueError("Parameters not allowed: {}".format(not_allowed_parameters))

        return self._voipms_client._get(method, parameters)

    def queue(self, queue_name, queue_number, queue_language, priority_weight, report_hold_time_agent, join_when_empty, leave_when_empty, ring_strategy, ring_inuse, **kwargs):
        """
        Updates a specific Queue entry if a queue code is provided

        - Adds a new Queue entry if no queue code is provided

        :param queue_name: [Required] Queue entry name
        :type queue_name: :py:class:`str`
        :param queue_number: [Required] Queue entry number
        :type queue_number: :py:class:`int`
        :param queue_language: [Required] Language Code (Values from general.get_languages)
        :type queue_language: :py:class:`str`
        :param priority_weight: [Required] weight/priority of queue (Values 1 to 60)
        :type priority_weight: :py:class:`int`
        :param report_hold_time_agent: [Required] Report hold time to agent (Values from accounts.get_report_estimated_hold_time)
        :type report_hold_time_agent: :py:class:`str`
        :param join_when_empty: [Required] How caller join to the queue (Values from dids.get_join_when_empty_types)
                                Examples:
                                yes     Callers can join a queue with no members or
                                        only unavailable members
                                no      Callers cannot join a queue with no members
                                strict  Callers cannot join a queue with no members
                                        or only unavailable members
        :type join_when_empty: :py:class:`str`
        :param leave_when_empty: [Required] How caller leave the queue (Values 'yes'/'no'/'strict')
                                 Examples:
                                 yes     Callers are sent to failover when
                                         there are no members
                                 no      Callers will remain in the queue even
                                         if there are no members
                                 strict  Callers are sent to failover if there are
                                         members but none of them is available.
        :type leave_when_empty: :py:class:`str`
        :param ring_strategy: Ring strategy (Values from dids.get_ring_strategies)
        :type ring_strategy: :py:class:`str`
        :param ring_inuse: If you want the queue to avoid sending calls to members (Values 'yes'/'no')
        :type ring_inuse: :py:class:`str`

        :param queue: ID for a specific Queue entry (Example: 32208 / Leave empty to create a new one)
        :type queue: :py:class:`int`
        :param queue_password: Queue Password
        :type queue_password: :py:class:`int`
        :param callerid_prefix: Caller ID Prefix for queue
        :type callerid_prefix: :py:class:`str`
        :param join_announcement: Recording Code (Values from dids.get_recordings or 'none')
        :type join_announcement: :py:class:`int`
        :param agent_announcement: Recording Code (Values from dids.get_recordings or 'none')
        :type agent_announcement: :py:class:`int`
        :param member_delay: Member delay when the agent is connected to the caller (Values 1 to 15 in seconds or 'none')
        :type member_delay: :py:class:`int`
        :param maximum_wait_time: Ammount of time a caller can wait in queue (Values in seconds: multiples of 30, max value: 1200 or 'unlimited')
        :type maximum_wait_time: :py:class:`int`
        :param maximum_callers: Maximum callers (Values: 1 to 60 or 'unlimited')
        :type maximum_callers: :py:class:`int`
        :param agent_ring_timeout: Number of seconds to ring an agent (Values 5 to 60)
        :type agent_ring_timeout: :py:class:`int`
        :param retry_timer: How long do we wait before trying all the members again (Values 5 to 60 seconds or 'none'= No Delay)
        :type retry_timer: :py:class:`int`
        :param wrapup_time: After a successful call, the number of seconds to wait before sending a free agent another call (Values 1 to 60 seconds or 'none'= No Delay)
        :type wrapup_time: :py:class:`int`
        :param voice_announcement: Code for Recording (Values from dids.get_recordings or 'none')
        :type voice_announcement: :py:class:`int`
        :param frequency_announcement: Periodic interval to play voice announce recording (Values in seconds: multiples of 15, max value: 1200 or 'none' = No announcement)
        :type frequency_announcement: :py:class:`int`
        :param announce_position_frecuency: How often to make any periodic announcement (Values in seconds: multiples of 15, max value: 1200 or 'none' = No announcement)
        :type announce_position_frecuency: :py:class:`int`
        :param announce_round_seconds: Announce seconds (Values in seconds: 1 to 60  or 'none' = Do not announce)
        :type announce_round_seconds: :py:class:`int`
        :param if_announce_position_enabled_report_estimated_hold_time: Include estimated hold time in position announcements (Values 'yes'/'no'/'once')
        :type if_announce_position_enabled_report_estimated_hold_time: :py:class:`str`
        :param thankyou_for_your_patience: Yes to say "Thank you for your patience" immediatly after announcing Queue Position and Estimated hold time left (Values 'yes'/'no')
        :type thankyou_for_your_patience: :py:class:`int`
        :param music_on_hold: Music on Hold Code (Values from accounts.get_music_on_hold)
        :type music_on_hold: :py:class:`str`
        :param fail_over_routing_timeout: Failover routing to Maximum wait time reached
        :type fail_over_routing_timeout: :py:class:`str`
        :param fail_over_routing_full: Failover routing to Maximum callers reached
        :type fail_over_routing_full: :py:class:`str`
        :param fail_over_routing_join_empty: A call was sent to the queue but the queue had no members (Only works when Join when Empty is set to no)
        :type fail_over_routing_join_empty: :py:class:`str`
        :param fail_over_routing_leave_empty: The last agent was removed form the queue before all calls were handled (Only works when Leave when Empty is set to yes)
        :type fail_over_routing_leave_empty: :py:class:`str`
        :param fail_over_routing_join_unavail: Same as routingjoinempty, except that there were still queue members, but all were status unavailable
        :type fail_over_routing_join_unavail: :py:class:`str`
        :param fail_over_routing_leave_unavail: Same as routingleaveempty, except that there were still queue members, but all were status unavailable
        :type fail_over_routing_leave_unavail: :py:class:`int`

        :returns: :py:class:`dict`

        routings can receive values in the following format => header:record_id
        Where header could be: account, fwd, vm, sip, grp, ivr, sys, recording, queue, cb, tc, disa, none.
        Examples:

            account     Used for routing calls to Sub Accounts
                        You can get all sub accounts using the accounts.get_sub_accounts function

            fwd         Used for routing calls to Forwarding entries.
                        You can get the ID right after creating a Forwarding with setForwarding
                        or by requesting all forwardings entries with getForwardings.

            vm          Used for routing calls to a Voicemail.
                        You can get all voicemails and their IDs using the voicemail.get_voicemails function

        Examples:
            'account:100001_VoIP'
            'fwd:1026'
            'vm:101'
        """
        method = "setQueue"

        if not isinstance(queue_name, str):
            raise ValueError("Queue entry name needs to be a str")

        if not isinstance(queue_number, str):
            raise ValueError("Queue entry number needs to be an int")

        if not isinstance(queue_language, str):
            raise ValueError("Language Code needs to be a str (Values from general.get_languages)")

        if not isinstance(priority_weight, int):
            raise ValueError("weight/priority of queue to be an int (Values 1 to 60) ")

        if not isinstance(report_hold_time_agent, str):
            raise ValueError("Report hold time to agent needs to be a str (Values from accounts.get_report_estimated_hold_time)")

        if not isinstance(join_when_empty, str):
            raise ValueError("How caller join to the queue needs to be a str (Values from dids.get_join_when_empty_types)")

        if not isinstance(leave_when_empty, str):
            raise ValueError("How caller leave the queue needs to be a str (Values 'yes'/'no'/'strict')")

        if not isinstance(ring_strategy, str):
            raise ValueError("Ring strategy needs to be a str (Values from dids.get_ring_strategies)")

        if not isinstance(ring_inuse, str):
            raise ValueError("If you want the queue to avoid sending calls to members needs to be a str (Values 'yes'/'no')")

        parameters = {
            "queue_name": queue_name,
            "queue_number": queue_number,
            "queue_language": queue_language,
            "priority_weight": priority_weight,
            "report_hold_time_agent": report_hold_time_agent,
            "join_when_empty": join_when_empty,
            "leave_when_empty": leave_when_empty,
            "ring_strategy": ring_strategy,
            "ring_inuse": ring_inuse,
        }

        if "queue" in kwargs:
            if not isinstance(kwargs["queue"], int):
                raise ValueError("ID for a specific Queue entry needs to be an int (Example: 32208 / Leave empty to create a new one)")
            parameters["queue"] = kwargs.pop("queue")

        if "queue_password" in kwargs:
            if not isinstance(kwargs["queue_password"], int):
                raise ValueError("Queue Password needs to be an int")
            parameters["queue_password"] = kwargs.pop("queue_password")

        if "callerid_prefix" in kwargs:
            if not isinstance(kwargs["callerid_prefix"], str):
                raise ValueError("Caller ID Prefix for queue needs to be a str")
            parameters["callerid_prefix"] = kwargs.pop("callerid_prefix")

        if "join_announcement" in kwargs:
            if not isinstance(kwargs["join_announcement"], int) and kwargs["join_announcement"] != "none":
                raise ValueError("Recording Code needs to be an int (Values from dids.get_recordings or 'none')")
            parameters["join_announcement"] = kwargs.pop("join_announcement")

        if "agent_announcement" in kwargs:
            if not isinstance(kwargs["agent_announcement"], int) and kwargs["join_announcement"] != "none":
                raise ValueError("Recording Code needs to be an int (Values from dids.get_recordings or 'none')")
            parameters["agent_announcement"] = kwargs.pop("agent_announcement")

        if "member_delay" in kwargs:
            if not isinstance(kwargs["member_delay"], int) and kwargs["member_delay"] != "none":
                raise ValueError("Member delay when the agent is connected to the caller needs to be an int (Values 1 to 15 in seconds or 'none')")
            parameters["member_delay"] = kwargs.pop("member_delay")

        if "maximum_wait_time" in kwargs:
            maximum_wait_time = kwargs.pop("maximum_wait_time")
            if not isinstance(maximum_wait_time, int) and maximum_wait_time != "unlimited":
                raise ValueError("Ammount of time a caller can wait in queue needs to be an int (Values in seconds: multiples of 30, max value: 1200 or 'unlimited')")
            elif maximum_wait_time % 30 != 0:
                raise ValueError("Ammount of time a caller can wait in queue needs to be a multiples of 30")
            elif maximum_wait_time > 1200:
                raise ValueError("Ammount of time a caller can wait in queue needs smaller than 1200 or 'unlimited'")
            parameters["maximum_wait_time"] = maximum_wait_time

        if "maximum_callers" in kwargs:
            if not isinstance(kwargs["maximum_callers"], int):
                raise ValueError("Maximum callers needs to be an int (Values: 1 to 60 or 'unlimited')")
            parameters["maximum_callers"] = kwargs.pop("maximum_callers")

        if "agent_ring_timeout" in kwargs:
            agent_ring_timeout = kwargs.pop("agent_ring_timeout")
            if not isinstance(agent_ring_timeout, int):
                raise ValueError("Number of seconds to ring an agent needs to be an int (Values 5 to 60)")
            elif not 5 <= agent_ring_timeout <= 60:
                raise ValueError("Number of seconds to ring an agent needs to be between 5 and 60")
            parameters["agent_ring_timeout"] = agent_ring_timeout

        if "retry_timer" in kwargs:
            retry_timer = kwargs.pop("retry_timer")
            if not isinstance(retry_timer, int) and retry_timer != 'none':
                raise ValueError("How long do we wait before trying all the members again needs to be an int (Values 5 to 60 seconds or 'none'= No Delay)")
            elif not 5 <= retry_timer <= 60:
                raise ValueError("How long do we wait before trying all the members again needs to be between 5 and 60")
            parameters["retry_timer"] = retry_timer

        if "wrapup_time" in kwargs:
            wrapup_time = kwargs.pop("wrapup_time")
            if not isinstance(wrapup_time, int) and wrapup_time != 'none':
                raise ValueError("After a successful call, the number of seconds to wait before sending a free agent another call needs to be an int (Values 1 to 60 seconds or 'none'= No Delay)")
            elif not 1 <= wrapup_time <= 60:
                raise ValueError("After a successful call, the number of seconds to wait before sending a free agent another call needs to be between 1 and 60 seconds")
            parameters["wrapup_time"] = wrapup_time

        if "voice_announcement" in kwargs:
            voice_announcement = kwargs.pop("voice_announcement")
            if not isinstance(voice_announcement, int) and voice_announcement != 'none':
                raise ValueError("Code for Recording needs to be an int (Values from dids.get_recordings or 'none')")
            parameters["voice_announcement"] = voice_announcement

        if "frequency_announcement" in kwargs:
            frequency_announcement = kwargs.pop("frequency_announcement")
            if not isinstance(frequency_announcement, int) and frequency_announcement != 'none':
                raise ValueError("Periodic interval to play voice announce recording needs to be an int (Values in seconds: multiples of 15, max value: 1200 or 'none' = No announcement)")
            elif frequency_announcement > 1200:
                raise ValueError("Periodic interval to play voice announce recording needs to be smaller than 1200")
            elif frequency_announcement % 15 != 0:
                raise ValueError("Periodic interval to play voice announce recording needs to be multiples of 15")
            parameters["frequency_announcement"] = frequency_announcement

        if "announce_position_frecuency" in kwargs:
            announce_position_frecuency = kwargs.pop("announce_position_frecuency")
            if not isinstance(announce_position_frecuency, int) and announce_position_frecuency != 'none':
                raise ValueError("How often to make any periodic announcement needs to be an int (Values in seconds: multiples of 15, max value: 1200 or 'none' = No announcement)")
            elif frequency_announcement > 1200:
                raise ValueError("How often to make any periodic announcement needs to be smaller than 1200")
            elif frequency_announcement % 15 != 0:
                raise ValueError("How often to make any periodic announcement needs to be multiples of 15")
            parameters["announce_position_frecuency"] = announce_position_frecuency

        if "announce_round_seconds" in kwargs:
            announce_round_seconds = kwargs.pop("announce_round_seconds")
            if not isinstance(announce_round_seconds, int) and announce_round_seconds != 'none':
                raise ValueError("Announce seconds needs to be an int (Values in seconds: 1 to 60  or 'none' = Do not announce)")
            elif not 1 <= announce_round_seconds <= 60:
                raise ValueError("Announce seconds needs to be between 1 and 60 seconds")
            parameters["announce_round_seconds"] = announce_round_seconds

        if "if_announce_position_enabled_report_estimated_hold_time" in kwargs:
            if_announce_position_enabled_report_estimated_hold_time = kwargs.pop("if_announce_position_enabled_report_estimated_hold_time")
            if not isinstance(if_announce_position_enabled_report_estimated_hold_time, str):
                raise ValueError("Include estimated hold time in position announcements needs to be a str (Values 'yes'/'no'/'once')")
            elif if_announce_position_enabled_report_estimated_hold_time not in ("yes", "no", "once"):
                raise ValueError("Include estimated hold time in position announcements needs 'yes', 'no' or 'once'")
            parameters["if_announce_position_enabled_report_estimated_hold_time"] = if_announce_position_enabled_report_estimated_hold_time

        if "thankyou_for_your_patience" in kwargs:
            thankyou_for_your_patience = kwargs.pop("thankyou_for_your_patience")
            if not isinstance(thankyou_for_your_patience, str):
                raise ValueError("Yes to say \"Thank you for your patience\" immediatly after announcing Queue Position and Estimated hold time left needs to be a str (Values 'yes'/'no')")
            elif thankyou_for_your_patience not in ("yes", "no"):
                raise ValueError("Yes to say \"Thank you for your patience\" immediatly after announcing Queue Position and Estimated hold time left needs to be 'yes' or 'no'")
            parameters["thankyou_for_your_patience"] = thankyou_for_your_patience

        if "music_on_hold" in kwargs:
            if not isinstance(kwargs["music_on_hold"], str):
                raise ValueError("Music on Hold Code needs to be a str (Values from accounts.get_music_on_hold)")
            parameters["music_on_hold"] = kwargs.pop("music_on_hold")

        if "fail_over_routing_timeout" in kwargs:
            if not isinstance(kwargs["fail_over_routing_timeout"], str):
                raise ValueError("Failover routing to Maximum wait time reached needs to be a str")
            parameters["fail_over_routing_timeout"] = kwargs.pop("fail_over_routing_timeout")

        if "fail_over_routing_full" in kwargs:
            if not isinstance(kwargs["fail_over_routing_full"], str):
                raise ValueError("Failover routing to Maximum callers reached needs to be a str")
            parameters["fail_over_routing_full"] = kwargs.pop("fail_over_routing_full")

        if "fail_over_routing_join_empty" in kwargs:
            if not isinstance(kwargs["fail_over_routing_join_empty"], str):
                raise ValueError("A call was sent to the queue but the queue had no members needs to be a str (Only works when Join when Empty is set to no)")
            parameters["fail_over_routing_join_empty"] = kwargs.pop("fail_over_routing_join_empty")

        if "fail_over_routing_leave_empty" in kwargs:
            if not isinstance(kwargs["fail_over_routing_leave_empty"], str):
                raise ValueError("The last agent was removed form the queue before all calls were handled needs to be a str (Only works when Leave when Empty is set to yes)")
            parameters["fail_over_routing_leave_empty"] = kwargs.pop("fail_over_routing_leave_empty")

        if "fail_over_routing_join_unavail" in kwargs:
            if not isinstance(kwargs["fail_over_routing_join_unavail"], str):
                raise ValueError("Same as routingjoinempty, except that there were still queue members, but all were status unavailable needs to be a str")
            parameters["fail_over_routing_join_unavail"] = kwargs.pop("fail_over_routing_join_unavail")

        if "fail_over_routing_leave_unavail" in kwargs:
            if not isinstance(kwargs["fail_over_routing_leave_unavail"], int):
                raise ValueError("Same as routingleaveempty, except that there were still queue members, but all were status unavailable needs to be a str")
            parameters["fail_over_routing_leave_unavail"] = kwargs.pop("fail_over_routing_leave_unavail")

        if len(kwargs) > 0:
            not_allowed_parameters = ""
            for key, value in kwargs.items():
                not_allowed_parameters += key + " "
            raise ValueError("Parameters not allowed: {}".format(not_allowed_parameters))

        return self._voipms_client._get(method, parameters)

    def recording(self, file, name, recording=None):
        """
        Updates a specific Recording File if a Recording ID is provided

        - Adds a new Recording file entry if no Recording ID is provided

        :param file: [Required] Base64 encoded file (Provide Recording ID and file if you want update the file only)
        :type file: :py:class:`str`
        :param name: [Required] Name for the Recording Entry (Example: 'recording1')
                     - Provide Recording ID and name if you want update the name only
                     - Provide Recording ID, file and name if you want update both parameters at the same time
        :type name: :py:class:`str`

        :param recording: ID for a specific Phonebook entry (Example: 33221 / Leave empty to create a new one)
        :type recording: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "setRecording"

        if not isinstance(file, str):
            raise ValueError("Base64 encoded file needs to be a str (Provide Recording ID and file if you want update the file only)")

        if not isinstance(name, str):
            raise ValueError("Name for the Recording Entry needs to be a str(Example: 'recording1')")

        parameters = {
            "file": file,
            "name": name,
        }

        if recording:
            if not isinstance(recording, int):
                raise ValueError("ID for a specific Phonebook entry needs to be an int (Example: 33221 / Leave empty to create a new one)")
            else:
                parameters["recording"] = recording

        return self._voipms_client._get(method, parameters)

    def ring_group(self, name, members, voicemail, **kwargs):
        """
        Updates a specific Ring Group if a ring group code is provided

        - Adds a new Ring Group entry if no ring group code is provided

        :param name: [Required] Name for the Ring Group
        :type name: :py:class:`str`
        :param members: [Required] Members for the Ring Group (Example: 'account:100001;fwd:16006')
        :type members: :py:class:`str`
        :param voicemail: [Required] Voicemail for the Ring Group (Values from voicemail.get_voicemails)
        :type voicemail: :py:class:`int`

        :param ring_group: ID for a specific Ring Group (Example: 4768 / Leave empty to create a new one)
        :type ring_group: :py:class:`int`
        :param caller_announcement: Recording Code (Values from dids.get_recordings)
        :type caller_announcement: :py:class:`int`
        :param music_on_hold: Music on Hold Code (Values from accounts.get_music_on_hold)
        :type music_on_hold: :py:class:`str`
        :param language: Code for Language (Values from general.get_languages)
        :type language: :py:class:`str`

        :returns: :py:class:`dict`
        """
        method = "setRingGroup"

        if not isinstance(name, str):
            raise ValueError("Name for the Ring Group needs to be a str")

        if not isinstance(members, str):
            raise ValueError("Members for the Ring Group needs to be a str (Example: 'account:100001;fwd:16006')")

        if not isinstance(voicemail, int):
            raise ValueError("Voicemail for the Ring Group needs to be an int (Values from voicemail.get_voicemails)")

        parameters = {
            "name": name,
            "members": members,
            "voicemail": voicemail,
        }

        if "ring_group" in kwargs:
            if not isinstance(kwargs["ring_group"], int):
                raise ValueError("ID for a specific Ring Group needs to be an int (Example: 4768 / Leave empty to create a new one)")
            parameters["ring_group"] = kwargs.pop("ring_group")

        if "caller_announcement" in kwargs:
            if not isinstance(kwargs["caller_announcement"], int):
                raise ValueError("Recording Code needs to be an int (Values from dids.get_recordings)")
            parameters["caller_announcement"] = kwargs.pop("caller_announcement")

        if "music_on_hold" in kwargs:
            if not isinstance(kwargs["music_on_hold"], str):
                raise ValueError("Music on Hold Code needs to be a str (Values from accounts.get_music_on_hold)")
            parameters["music_on_hold"] = kwargs.pop("music_on_hold")

        if "language" in kwargs:
            if not isinstance(kwargs["language"], str):
                raise ValueError("Code for Language needs to be a str (Values from general.get_languages)")
            parameters["language"] = kwargs.pop("language")

        if len(kwargs) > 0:
            not_allowed_parameters = ""
            for key, value in kwargs.items():
                not_allowed_parameters += key + " "
            raise ValueError("Parameters not allowed: {}".format(not_allowed_parameters))

        return self._voipms_client._get(method, parameters)

    def sip_uri(self, uri, **kwargs):
        """
        Updates a specific SIP URI if a SIP URI code is provided

        - Adds a new SIP URI entry if no SIP URI code is provided

        :param uri: [Required] SIP URI (Example: '5552223333@sip.voip.ms')
        :type uri: :py:class:`str`

        :param sipuri: ID for a specific SIP URI (Example: 6199 / Leave empty to create a new one)
        :type sipuri: :py:class:`int`
        :param description: Description for the SIP URI
        :type description: :py:class:`str`

        :returns: :py:class:`dict`
        """
        method = "setSIPURI"

        if not isinstance(uri, str):
            raise ValueError("Name for the Ring Group needs to be a str")

        parameters = {
            "uri": uri,
        }

        if "sipuri" in kwargs:
            if not isinstance(kwargs["sipuri"], int):
                raise ValueError("ID for a specific SIP URI needs to be an int (Example: 6199 / Leave empty to create a new one)")
            parameters["sipuri"] = kwargs.pop("sipuri")

        if "description" in kwargs:
            if not isinstance(kwargs["description"], str):
                raise ValueError("Description for the SIP URI needs to be a str")
            parameters["description"] = kwargs.pop("description")

        if len(kwargs) > 0:
            not_allowed_parameters = ""
            for key, value in kwargs.items():
                not_allowed_parameters += key + " "
            raise ValueError("Parameters not allowed: {}".format(not_allowed_parameters))

        return self._voipms_client._get(method, parameters)

    def sms(self, did, enable, **kwargs):
        """
        Updates a specific SIP URI if a SIP URI code is provided

        - Adds a new SIP URI entry if no SIP URI code is provided

        :param did: [Required] DID to be Updated (Example: 5551234567)
        :type did: :py:class:`int`
        :param enable: Enable/Disable the DID to receive SMS Messages (Values:True=Enable / False=Disable)
        :type enable: :py:class:`bool`

        :param email_enabled: If Enable, SMS Messages received by your DID will be sent to the email address provided (Values:True=Enable / False=Disable)
        :type email_enabled: :py:class:`bool`
        :param email_address: SMS Messages received by your DID will be sent to the email address provided
        :type email_address: :py:class:`str`
        :param sms_forward_enable: If Enable, SMS Messages received by your DID will be forwarded to the phone number provided (Values:True=Enable / False=Disable)
        :type sms_forward_enable: :py:class:`bool`
        :param sms_forward: SMS Messages received by your DID will be forwarded to the phone number provided (Example: 5551234567)
        :type sms_forward: :py:class:`int`
        :param url_callback_enable: If Enable, SMS Messages received by your DID will be send a GET request to the URL callback provided (Values:True=Enable / False=Disable)
        :type url_callback_enable: :py:class:`bool`
        :param url_callback: SMS Messages received by your DID will be send a GET request to the URL callback provided Available Variables for your URL:
                             - {FROM}    The phone number that sent you the message.
                             - {TO}      The DID number that received the message.
                             - {MESSAGE} The content of the message.
                             Example:
                             http://mysite.com/sms.php?to={TO}&from={FROM}&message={MESSAGE}
        :type url_callback: :py:class:`str`
        :param url_callback_retry: Enable URL callback Retry (Values:True=Enable / False=Disable)
                                    we will be expecting an "ok" output (without quotes) from your URL callback
                                    page as an indicator that you have received the message correctly.
                                    If we don't receive the "ok" letters (wihtout quotes) from your callback
                                    page, we will keep sending you the same message every 30 minutes.
        :type url_callback_retry: :py:class:`bool`

        :returns: :py:class:`dict`
        """
        method = "setSMS"

        if not isinstance(did, int):
            raise ValueError("DID to be Updated needs to be an int (Example: 5551234567)")

        if not isinstance(enable, bool):
            raise ValueError("Enable/Disable the DID to receive SMS Messages needs to be a bool (Values:True=Enable / False=Disable)")

        parameters = {
            "did": did,
            "enable": convert_bool(enable),
        }

        if "email_enabled" in kwargs:
            if not isinstance(kwargs["email_enabled"], bool):
                raise ValueError("If Enable, SMS Messages received by your DID will be sent to the email address provided needs to be a bool (Values:True=Enable / False=Disable)")
            parameters["email_enabled"] = convert_bool(kwargs.pop("email_enabled"))

        if "email_address" in kwargs:
            email_address = kwargs.pop("email_address")
            if not isinstance(email_address, str):
                raise ValueError("SMS Messages received by your DID will be sent to the email address provided needs to be a str")
            elif not validate_email(email_address):
                raise ValueError("Client's e-mail is not a correct email syntax")
            parameters["email_address"] = email_address

        if "sms_forward_enable" in kwargs:
            if not isinstance(kwargs["sms_forward_enable"], bool):
                raise ValueError("If Enable, SMS Messages received by your DID will be forwarded to the phone number provided needs to be a bool (Values:True=Enable / False=Disable)")
            parameters["sms_forward_enable"] = convert_bool(kwargs.pop("sms_forward_enable"))

        if "sms_forward" in kwargs:
            if not isinstance(kwargs["sms_forward"], int):
                raise ValueError("SMS Messages received by your DID will be forwarded to the phone number provided needs to be int (Example: 5551234567)")
            parameters["sms_forward"] = convert_bool(kwargs.pop("sms_forward"))

        if "url_callback_enable" in kwargs:
            if not isinstance(kwargs["url_callback_enable"], bool):
                raise ValueError("If Enable, SMS Messages received by your DID will be send a GET request to the URL callback provided needs to be a bool (Values:True=Enable / False=Disable)")
            parameters["url_callback_enable"] = convert_bool(kwargs.pop("url_callback_enable"))

        if "url_callback" in kwargs:
            if not isinstance(kwargs["url_callback"], str):
                raise ValueError("SMS Messages received by your DID will be send a GET request to the URL callback provided needs to be a str")
            parameters["url_callback"] = convert_bool(kwargs.pop("url_callback"))

        if "url_callback_retry" in kwargs:
            if not isinstance(kwargs["url_callback_retry"], bool):
                raise ValueError("Enable URL callback Retry needs to be a bool (Values:True=Enable / False=Disable)")
            parameters["url_callback_retry"] = convert_bool(kwargs.pop("url_callback_retry"))

        if len(kwargs) > 0:
            not_allowed_parameters = ""
            for key, value in kwargs.items():
                not_allowed_parameters += key + " "
            raise ValueError("Parameters not allowed: {}".format(not_allowed_parameters))

        return self._voipms_client._get(method, parameters)

    def static_member(self, queue, member_name, priority, **kwargs):
        """
        Updates a specific SIP URI if a SIP URI code is provided

        - Adds a new SIP URI entry if no SIP URI code is provided

        :param queue: [Required] ID for a specific Queue
        :type queue: :py:class:`int`
        :param member_name: [Required] Member Description Static Member Routing to receive calls (You can get all sub accounts using the accounts.get_sub_accounts function)
        :type member_name: :py:class:`str`
        :param priority: [Required] Values for get calls first (Example: 0)
        :type priority: :py:class:`int`

        :param member: ID for a specific Member (Example: 619 / Leave empty to create a new one)
        :type member: :py:class:`int`
        :param account: Static Member Routing to receive calls (You can get all sub accounts using the accounts.get_sub_accounts function)
        :type account: :py:class:`str`

        :returns: :py:class:`dict`
        """
        method = "setStaticMember"

        if not isinstance(queue, int):
            raise ValueError("ID for a specific Queue needs to be an int")

        if not isinstance(member_name, str):
            raise ValueError("Member Description Static Member Routing to receive calls needs to be a str (You can get all sub accounts using the accounts.get_sub_accounts function)")

        if not isinstance(priority, int):
            raise ValueError("Values for get calls first needs to be an int (Example: 0)")

        parameters = {
            "queue": queue,
            "member_name": member_name,
            "priority": priority,
        }

        if "member" in kwargs:
            if not isinstance(kwargs["member"], int):
                raise ValueError("ID for a specific Member needs to be an int (Example: 619 / Leave empty to create a new one)")
            parameters["member"] = kwargs.pop("member")

        if "account" in kwargs:
            if not isinstance(kwargs["account"], str):
                raise ValueError("Static Member Routing to receive calls needs to be a str (You can get all sub accounts using the accounts.get_sub_accounts function)")
            parameters["account"] = kwargs.pop("account")

        if len(kwargs) > 0:
            not_allowed_parameters = ""
            for key, value in kwargs.items():
                not_allowed_parameters += key + " "
            raise ValueError("Parameters not allowed: {}".format(not_allowed_parameters))

        return self._voipms_client._get(method, parameters)

    def time_condition(self, name, routing_match, routing_nomatch, starthour, startminute, endhour, endminute, weekdaystart, weekdayend, timecondition=None):
        """
        Updates a specific Time Condition if a time condition code is provided

        - Adds a new Time Condition entry if no time condition code is provided

        :param name: [Required] Name for the Time Condition
        :type name: :py:class:`str`
        :param routing_match: [Required] Routing for the Call when condition matches
        :type routing_match: :py:class:`str`
        :param routing_nomatch: Routing for the Call when condition does not match
        :type routing_nomatch: :py:class:`str`
        :param starthour: [Required] All the Start Hour Conditions (Example: '8;8')
        :type starthour: :py:class:`str`
        :param startminute: [Required] All the Start Minute Conditions (Example: '0;0')
        :type startminute: :py:class:`str`
        :param endhour: [Required] All the End Hour Conditions (Example: '16;12')
        :type endhour: :py:class:`str`
        :param endminute: [Required] All the End Minute Conditions (Example: '0;0')
        :type endminute: :py:class:`str`
        :param weekdaystart: [Required] All the Week Day Start Conditions (Example: 'mon;sat')
        :type weekdaystart: :py:class:`str`
        :param weekdayend: [Required] All the Week Day End Conditions (Example: 'fri;sat')
        :type weekdayend: :py:class:`str`


        :param member: ID for a specific Time Condition (Example: 1830 / Leave empty to create a new one)
        :type member: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "setTimeCondition"

        if not isinstance(name, str):
            raise ValueError("Name for the Time Condition needs to be a str")

        if not isinstance(routing_match, str):
            raise ValueError("Routing for the Call when condition matches needs to be a str")

        if not isinstance(routing_nomatch, str):
            raise ValueError("Routing for the Call when condition does not match needs to be a str")

        if not isinstance(starthour, str):
            raise ValueError("All the Start Hour Conditions needs to be a str (Example: '8;8')")

        if not isinstance(endhour, str):
            raise ValueError("All the End Hour Conditions needs to be a str (Example: '16;12')")

        if not isinstance(endminute, str):
            raise ValueError("All the End Minute Conditions needs to be a str (Example: '0;0')")

        if not isinstance(weekdaystart, str):
            raise ValueError("All the Week Day Start Conditions needs to be a str (Example: 'mon;sat')")

        if not isinstance(weekdayend, str):
            raise ValueError("All the Week Day End Conditions needs to be a str (Example: 'fri;sat')")

        parameters = {
            "name": name,
            "routing_match": routing_match,
            "routing_nomatch": routing_nomatch,
            "starthour": starthour,
            "endhour": endhour,
            "endminute": endminute,
            "weekdaystart": weekdaystart,
            "weekdayend": weekdayend,
        }

        if timecondition:
            if not isinstance(timecondition, int):
                raise ValueError("ID for a specific Time Condition needs to be an int (Example: 1830 / Leave empty to create a new one)")
            else:
                parameters["timecondition"] = timecondition

        return self._voipms_client._get(method, parameters)
