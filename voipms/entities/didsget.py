# coding=utf-8
"""
The Dids API endpoint get

Documentation: https://voip.ms/m/apidocs.php
"""
from voipms.baseapi import BaseApi
from voipms.helpers import validate_date, convert_bool


class DidsGet(BaseApi):
    """
    Get for the General endpoint.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(DidsGet, self).__init__(*args, **kwargs)
        self.endpoint = 'dids'

    def callbacks(self, callback=None):
        """
        Retrieves a list of Callbacks if no additional parameter is provided

        - Retrieves a specific Callback if a Callback code is provided

        :param callback: ID for a specific Callback (Example: 2359)
        :type callback: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "getCallbacks"

        parameters = {}
        if callback:
            if not isinstance(callback, int):
                raise ValueError("ID for a specific Callback needs to be an int (Example: 2359)")
            parameters["callback"] = callback

        return self._voipms_client._get(method, parameters)

    def caller_id_filtering(self, filtering=None):
        """
        Retrieves a list of CallerID Filterings if no additional parameter is provided

        - Retrieves a specific CallerID Filtering if a CallerID Filtering code is provided

        :param filtering: ID for a specific CallerID Filtering (Example: 18915)
        :type filtering: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "getCallerIDFiltering"

        parameters = {}
        if filtering:
            if not isinstance(filtering, int):
                raise ValueError("ID for a specific CallerID Filtering needs to be an int (Example: 18915)")
            parameters["filtering"] = filtering

        return self._voipms_client._get(method, parameters)

    def did_countries(self, international_type, country_id=None):
        """
        Retrieves a list of Countries for International DIDs if no country code is provided

        - Retrieves a specific Country for International DIDs if a country code is provided

        :param international_type: [Required] Type of International DID (Values from dids.get.international_types)
        :type international_type: :py:class:`str`

        :param country_id: ID for a specific country (Example: 205)
        :type country_id: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "getDIDCountries"

        if not isinstance(international_type, str):
            raise ValueError("Type of International DID needs to be a str (Values from dids.get.international_types)")
        parameters = {
            "type": international_type
        }

        if country_id:
            if not isinstance(country_id, int):
                raise ValueError("ID for a specific country needs to be an int (Example: 205)")
            parameters["country_id"] = country_id

        return self._voipms_client._get(method, parameters)

    def carriers(self, carrier=None):
        """
        Retrieves a list of Carriers for Vanity Numbers if no additional parameter is provided

        - Retrieves a specific Carrier for Vanity Numbers if a carrier code is provided

        :param carrier: Code for a specific Carrier (Example: 2)
        :type carrier: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "getCarriers"

        parameters = {}
        if carrier:
            if not isinstance(carrier, int):
                raise ValueError("ID for a specific CallerID Filtering needs to be an int (Example: 18915)")
            parameters["carrier"] = carrier

        return self._voipms_client._get(method, parameters)

    def dids_can(self, province, ratecenter=None):
        """
        Retrives a list of Canadian DIDs by Province and Ratecenter

        :param province: [Required] Canadian Province (Values from dids.get.provinces)
        :type province: :py:class:`str`

        :param ratecenter: Canadian Ratecenter (Values from dids.get.rate_centers_can)
        :type ratecenter: :py:class:`str`

        :returns: :py:class:`dict`
        """
        method = "getDIDsCAN"

        if not isinstance(province, str):
            raise ValueError("Canadian Province needs to be a str (Values from dids.get.provinces)")
        parameters = {
            "province": province
        }

        if ratecenter:
            if not isinstance(ratecenter, str):
                raise ValueError("Canadian Ratecenter needs to be a str (Values from dids.get.rate_centers_can)")
            else:
                parameters["ratecenter"] = ratecenter

        return self._voipms_client._get(method, parameters)

    def dids_info(self, client=None, did=None):
        """
        Retrieves information from all your DIDs if no additional parameter is provided

        - Retrieves information from Reseller Client's DIDs if a Reseller Client ID is provided.
        - Retrieves information from Sub Account's DIDs if a Sub Accunt is provided.
        - Retrieves information from a specific DID if a DID Number is provided.
        - Retrieves SMS information from a specific DID if the SMS is available.

        :param client: Parameter could have the following values
                            - Empty Value [Not Required]
                            - Specific Reseller Client ID (Example: 561115)
                            - Specific Sub Account (Example: '100001_VoIP')
        :type client: :py:class:`str`
        :param did: DID from Client or Sub Account (Example: 5551234567)
        :type did: :py:class:`str`

        :returns: :py:class:`dict`
        """
        method = "getDIDsInfo"

        parameters = {}

        if client:
            if not isinstance(client, str):
                raise ValueError("Parameter needs to be Empty Value [Not Required], Specific Reseller Client ID (Example: 561115) or Specific Sub Account (Example: '100001_VoIP'). The value needs to be a str.")
            else:
                parameters["client"] = client

        if did:
            if not isinstance(did, int):
                raise ValueError("DID from Client or Sub Account needs to be an int (Example: 5551234567)")
            else:
                parameters["did"] = did

        return self._voipms_client._get(method, parameters)

    def dids_international_geographic(self, country_id):
        """
        Retrieves a list of International Geographic DIDs by Country

        :param country_id: [Required] ID for a specific Country (Values from dids.get.did_countries)
        :type country_id: :py:class:`str`

        :returns: :py:class:`dict`
        """
        method = "getDIDsInternationalGeographic"

        if not isinstance(country_id, int):
            raise ValueError("ID for a specific Country needs to be an int (Values from dids.get.did_countries)")
        parameters = {
            "country_id": country_id
        }

        return self._voipms_client._get(method, parameters)

    def dids_international_national(self, country_id):
        """
        Retrieves a list of International National DIDs by Country

        :param country_id: [Required] ID for a specific Country (Values from dids.get.did_countries)
        :type country_id: :py:class:`str`

        :returns: :py:class:`dict`
        """
        method = "getDIDsInternationalNational"

        if not isinstance(country_id, int):
            raise ValueError("ID for a specific Country needs to be an int (Values from dids.get.did_countries)")
        parameters = {
            "country_id": country_id
        }

        return self._voipms_client._get(method, parameters)

    def dids_international_toll_free(self, country_id):
        """
        Retrieves a list of International TollFree DIDs by Country

        :param country_id: [Required] ID for a specific Country (Values from dids.get.did_countries)
        :type country_id: :py:class:`str`

        :returns: :py:class:`dict`
        """
        method = "getDIDsInternationalTollFree"

        if not isinstance(country_id, int):
            raise ValueError("ID for a specific Country needs to be an int (Values from dids.get.did_countries)")
        parameters = {
            "country_id": country_id
        }

        return self._voipms_client._get(method, parameters)

    def dids_usa(self, state, ratecenter=None):
        """
        Retrives a list of USA DIDs by State and Ratecenter

        :param state: [Required] United States State (Values from dids.get.states)
        :type state: :py:class:`str`

        :param ratecenter: United States Ratecenter (Values from dids.get.rate_centers_usa)
        :type ratecenter: :py:class:`str`

        :returns: :py:class:`dict`
        """
        method = "getDIDsUSA"

        if not isinstance(state, str):
            raise ValueError("United States State needs to be a str (Values from dids.get.states)")
        parameters = {
            "state": state
        }

        if ratecenter:
            if not isinstance(ratecenter, str):
                raise ValueError("United States Ratecenter (Values from dids.get.rate_centers_usa)")
            else:
                parameters["ratecenter"] = ratecenter

        return self._voipms_client._get(method, parameters)

    def disas(self, disa=None):
        """
        Retrieves a list of DISAs if no additional parameter is provided

        - Retrieves a specific DISA if a DISA code is provided

        :param disa: ID for a specific DISA (Example: 2114)
        :type disa: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "getDISAs"

        parameters = {}
        if disa:
            if not isinstance(disa, int):
                raise ValueError("ID for a specific DISA needs to be an int (Example: 2114)")
            parameters["disa"] = disa

        return self._voipms_client._get(method, parameters)

    def forwardings(self, forwarding=None):
        """
        Retrieves a list of Forwardings if no additional parameter is provided

        - Retrieves a specific Forwarding if a fwd code is provided

        :param forwarding: ID for a specific Forwarding (Example: 18635)
        :type forwarding: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "getForwardings"

        parameters = {}
        if forwarding:
            if not isinstance(forwarding, int):
                raise ValueError("ID for a specific Forwarding needs to be an int (Example: 18635)")
            parameters["forwarding"] = forwarding

        return self._voipms_client._get(method, parameters)

    def international_types(self, international_type=None):
        """
        Retrieves a list of Types for International DIDs if no additional parameter is provided

        - Retrieves a specific Types for International DIDs if a type code is provided

        :param international_type: Code for a specific International Type (Example: 'NATIONAL')
        :type international_type: :py:class:`str`

        :returns: :py:class:`dict`
        """
        method = "getInternationalTypes"

        parameters = {}
        if international_type:
            if not isinstance(international_type, str):
                raise ValueError("Code for a specific International Type needs to be a str (Example: 'NATIONAL')")
            parameters["type"] = international_type

        return self._voipms_client._get(method, parameters)

    def ivrs(self, ivr=None):
        """
        Retrieves a list of IVRs if no additional parameter is provided

        - Retrieves a specific IVR if a IVR code is provided

        :param ivr: ID for a specific IVR (Example: 4636)
        :type ivr: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "getIVRs"

        parameters = {}
        if ivr:
            if not isinstance(ivr, int):
                raise ValueError("ID for a specific IVR needs to be an int (Example: 4636)")
            parameters["ivr"] = ivr

        return self._voipms_client._get(method, parameters)

    def join_when_empty_types(self, join_type=None):
        """
        Retrieves a list of 'JoinWhenEmpty' Types if no additional parameter is provided

        - Retrieves a specific 'JoinWhenEmpty' Types if a type code is provided

        :param join_type: Code for a specific 'JoinWhenEmpty' Type (Example: 'yes')
        :type join_type: :py:class:`str`

        :returns: :py:class:`dict`
        """
        method = "getJoinWhenEmptyTypes"

        parameters = {}
        if join_type:
            if not isinstance(join_type, int):
                raise ValueError("Code for a specific 'JoinWhenEmpty' Type needs to be a str (Example: 'yes')")
            parameters["type"] = join_type

        return self._voipms_client._get(method, parameters)

    def phonebook(self, phonebook=None, name=None):
        """
        Retrieves a list of Phonebook entries if no additional parameter is provided

        - Retrieves a list of Phonebook entries if a name is provided.
        - Retrieves a specific Phonebook entry if a Phonebook code is provided.

        :param phonebook: ID for a specific Phonebook entry (Example: 32207)
        :type phonebook: :py:class:`int`
        :param name: Name to be searched in database (Example: 'jane')
        :type name: :py:class:`str`

        :returns: :py:class:`dict`
        """
        method = "getPhonebook"

        parameters = {}

        if phonebook:
            if not isinstance(phonebook, int):
                raise ValueError("ID for a specific Phonebook entry needs to an int (Example: 32207)")
            else:
                parameters["phonebook"] = phonebook

        if name:
            if not isinstance(name, str):
                raise ValueError("Name to be searched in database needs to be a str (Example: 'jane')")
            else:
                parameters["name"] = name

        return self._voipms_client._get(method, parameters)

    def portability(self, did):
        """
        Shows if a DID Number can be ported into our network

        - Display plans and rates available if the DID Number can be ported into our network.

        :param did: [Required] DID Number to be ported into our network (Example: 5552341234)
        :type did: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "getPortability"

        if not isinstance(did, int):
            raise ValueError("DID Number to be ported into our network needs to be an int (Example: 5552341234)")
        parameters = {
            "DID": did
        }

        return self._voipms_client._get(method, parameters)

    def provinces(self):
        """
        Retrieves a list of Canadian Provinces

        :returns: :py:class:`dict`
        """
        method = "getProvinces"

        return self._voipms_client._get(method)

    def queues(self, queue=None):
        """
        Retrieves a list of Queue entries if no additional parameter is provided

        - Retrieves a specific Queue entry if a Queue code is provided.

        :param queue: ID for a specific Queue (Example: 4764)
        :type queue: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "getQueues"

        parameters = {}
        if queue:
            if not isinstance(queue, int):
                raise ValueError("ID for a specific Queue needs to be an int (Example: 4764)")
            parameters["queue"] = queue

        return self._voipms_client._get(method, parameters)

    def rate_centers_can(self, province):
        """
        Retrieves a list of Canadian Ratecenters by Province

        :param province: [Required] Canadian Province (Values from dids.get.provinces)
        :type province: :py:class:`str`
        :returns: :py:class:`dict`
        """
        method = "getRateCentersCAN"

        parameters = {}
        if province:
            if not isinstance(province, str):
                raise ValueError("Canadian Province needs to be a str (Values from dids.get.provinces)")
            parameters["province"] = province

        return self._voipms_client._get(method, parameters)

    def rate_centers_usa(self, state):
        """
        Retrieves a list of USA Ratecenters by State

        :param state: [Required] United States State (Values from dids.get.states)
        :type state: :py:class:`str`
        :returns: :py:class:`dict`
        """
        method = "getRateCentersUSA"

        parameters = {}

        if not isinstance(state, str):
            raise ValueError("United States State needs to be a str (Values from dids.get.states)")
        parameters["state"] = state

        return self._voipms_client._get(method, parameters)

    def recordings(self, recording=None):
        """
        Retrieves a list of Recordings if no additional parameter is provided

        - Retrieves a specific Recording if a Recording code is provided

        :param recording: ID for a specific Recording (Example: 7567)
        :type recording: :py:class:`int`
        :returns: :py:class:`dict`
        """
        method = "getRecordings"

        parameters = {}

        if recording:
            if not isinstance(recording, int):
                raise ValueError("ID for a specific Recording needs to be an int (Example: 7567)")
            parameters["recording"] = recording

        return self._voipms_client._get(method, parameters)

    def recording_file(self, recording):
        """
        Retrieves a specific Recording File data in Base64 format

        :param recording: [Required] ID for a specific Recording (Example: 7567)
        :type recording: :py:class:`int`
        :returns: :py:class:`dict`
        """
        method = "getRecordingFile"

        parameters = {}

        if not isinstance(recording, int):
            raise ValueError("ID for a specific Recording needs to be an int (Example: 7567)")
        parameters["recording"] = recording

        return self._voipms_client._get(method, parameters)

    def ring_groups(self, ringgroup=None):
        """
        Retrieves a list of Ring Groups if no additional parameter is provided

        - Retrieves a specific Ring Group if a ring group code is provided

        :param ringgroup: ID for a specific Ring Group (Example: 4768)
        :type ringgroup: :py:class:`int`
        :returns: :py:class:`dict`
        """
        method = "getRingGroups"

        parameters = {}

        if ringgroup:
            if not isinstance(ringgroup, int):
                raise ValueError("ID for a specific Ring Group needs to be an int (Example: 4768)")
            parameters["ringgroup"] = ringgroup

        return self._voipms_client._get(method, parameters)

    def ring_strategies(self, strategy=None):
        """
        Retrieves a list of Ring Strategies if no additional parameter is provided

        - Retrieves a specific Ring Strategy if a ring strategy code is provided

        :param strategy: ID for a specific Ring Strategy (Example: 'rrmemory')
        :type strategy: :py:class:`str`
        :returns: :py:class:`dict`
        """
        method = "getRingStrategies"

        parameters = {}

        if strategy:
            if not isinstance(strategy, int):
                raise ValueError("ID for a specific Ring Strategy needs to be a str (Example: 'rrmemory')")
            parameters["strategy"] = strategy

        return self._voipms_client._get(method, parameters)

    def sip_uris(self, sipuri=None):
        """
        Retrieves a list of SIP URIs if no additional parameter is provided

        - Retrieves a specific SIP URI if a SIP URI code is provided

        :param sipuri: ID for a specific SIP URI (Example: 6199)
        :type sipuri: :py:class:`int`
        :returns: :py:class:`dict`
        """
        method = "getSIPURIs"

        parameters = {}

        if sipuri:
            if not isinstance(sipuri, int):
                raise ValueError("ID for a specific SIP URI needs to be an int (Example: 6199)")
            parameters["sipuri"] = sipuri

        return self._voipms_client._get(method, parameters)

    def sms(self, **kwargs):
        """
        Retrieves a list of SMS messages by: date range, sms type, DID number, and contact

        :param sms: ID for a specific SMS (Example: 5853)
        :type sms: :py:class:`int`
        :param from: Start Date for Filtering SMSs (Example: '2014-03-30')
                     - Default value: Today
        :type from: :py:class:`str`
        :param to: End Date for Filtering SMSs (Example: '2014-03-30')
                     - Default value: Today
        :type to: :py:class:`str`
        :param type: Filter SMSs by Type (Boolean: True = received / False = sent)
        :type type: :py:class:`bool`
        :param did: DID number for Filtering SMSs (Example: 5551234567)
        :type did: :py:class:`int`
        :param contact: Contact number for Filtering SMSs (Example: 5551234567)
        :type contact: :py:class:`int`
        :param limit: Number of records to be displayed (Example: 20)
                       - Default value: 50
        :type limit: :py:class:`int`
        :param timezone: Adjust time of SMSs according to Timezome (Numeric: -12 to 13)
        :type timezone: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "getSMS"

        parameters = {}

        if "sms" in kwargs:
            if not isinstance(kwargs["sms"], int):
                raise ValueError("ID for a specific SMS needs to be an int (Example: 5853)")
            parameters["sms"] = kwargs.pop("sms")

        if "from" in kwargs:
            if not isinstance(kwargs["from"], str):
                raise ValueError("Start Date for Filtering SMSs needs to be a str (Example: '2014-03-30')")
            validate_date(kwargs["from"])
            parameters["from"] = kwargs.pop("from")

        if "to" in kwargs:
            if not isinstance(kwargs["to"], str):
                raise ValueError("End Date for Filtering SMSs needs to be a str (Example: '2014-03-30')")
            validate_date(kwargs["to"])
            parameters["to"] = kwargs.pop("to")

        if "type" in kwargs:
            if not isinstance(kwargs["type"], bool):
                raise ValueError("Filter SMSs by Type needs to be a bool (Boolean: True = received / False = sent)")
            parameters["type"] = convert_bool(kwargs.pop("type"))

        if "did" in kwargs:
            if not isinstance(kwargs["did"], int):
                raise ValueError("DID number for Filtering SMSs needs to be an int (Example: 5551234567)")
            parameters["did"] = kwargs.pop("did")

        if "contact" in kwargs:
            if not isinstance(kwargs["contact"], int):
                raise ValueError("Contact number for Filtering SMSs needs to be an int (Example: 5551234567)")
            parameters["contact"] = kwargs.pop("contact")

        if "limit" in kwargs:
            if not isinstance(kwargs["limit"], int):
                raise ValueError("Number of records to be displayed needs to be an int (Example: 20)")
            parameters["limit"] = kwargs.pop("limit")

        if "timezone" in kwargs:
            if not isinstance(kwargs["timezone"], int):
                raise ValueError("Adjust time of SMSs according to Timezome needs to be an int (Numeric: -12 to 13)")
            parameters["timezone"] = kwargs.pop("timezone")

        if len(kwargs) > 0:
            not_allowed_parameters = ""
            for key, value in kwargs.items():
                not_allowed_parameters += key + " "
            raise ValueError("Parameters not allowed: {}".format(not_allowed_parameters))

        return self._voipms_client._get(method, parameters)

    def states(self):
        """
        Retrieves a list of USA States

        :returns: :py:class:`dict`
        """
        method = "getStates"

        return self._voipms_client._get(method)

    def static_members(self, queue, member=None):
        """
        Retrieves a list of Static Members from a queue if no additional parameter is provided

        - Retrieves a specific Static Member from a queue if Queue ID and Member ID are provided

        :param state: [Required] ID for a specific Queue (Example: 4136)
        :type state: :py:class:`int`

        :param ratecenter: ID for a specific Static Member (Example: 163)
                            - The Member must belong to the queue provided
        :type ratecenter: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "getStaticMembers"

        if not isinstance(queue, int):
            raise ValueError("ID for a specific Queue needs to be an int (Example: 4136)")
        parameters = {
            "queue": queue
        }

        if member:
            if not isinstance(member, str):
                raise ValueError("ID for a specific Static Member needs to be an int (Example: 163) and Member must belong to the queue provided")
            else:
                parameters["member"] = member

        return self._voipms_client._get(method, parameters)

    def time_conditions(self, timecondition=None):
        """
        Retrieves a list of Time Conditions if no additional parameter is provided

        - Retrieves a specific Time Condition if a time condition code is provided.

        :param timecondition: ID for a specific Time Condition (Example: 1830)
        :type timecondition: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "getTimeConditions"

        parameters = {}
        if timecondition:
            if not isinstance(timecondition, int):
                raise ValueError("ID for a specific Time Condition needs to be an int (Example: 1830)")
            parameters["timecondition"] = timecondition

        return self._voipms_client._get(method, parameters)

    def voicemail_setups(self, voicemailsetup=None):
        """
        Retrieves a list of Voicemail Setup Options if no additional parameter is provided

        - Retrieves a specific Voicemail Setup Option if a voicemail setup code is provided.

        :param voicemailsetup: ID for a specific Voicemail Setup (Example: 2)
        :type voicemailsetup: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "getVoicemailSetups"

        parameters = {}
        if voicemailsetup:
            if not isinstance(voicemailsetup, int):
                raise ValueError("ID for a specific Voicemail Setup needs to be an int (Example: 2)")
            parameters["voicemailsetup"] = voicemailsetup

        return self._voipms_client._get(method, parameters)

    def voicemail_attachment_formats(self, email_attachment_format=None):
        """
        Retrieves a list of Email Attachment Format Options if no additional parameter is provided

        - Retrieves a specific Email Attachment Format Option if a format value is provided.

        :param email_attachment_format: ID for a specific attachment format (Example: wav49)
        :type email_attachment_format: :py:class:`str`

        :returns: :py:class:`dict`
        """
        method = "getVoicemailAttachmentFormats"

        parameters = {}
        if email_attachment_format:
            if not isinstance(email_attachment_format, str):
                raise ValueError("ID for a specific Voicemail Setup needs to be an int (Example: 2)")
            parameters["email_attachment_format"] = email_attachment_format

        return self._voipms_client._get(method, parameters)