# coding=utf-8
"""
The General API endpoint get

Documentation: https://voip.ms/m/apidocs.php
"""
from datetime import datetime

from voipms.baseapi import BaseApi
from voipms.helpers import validate_date, convert_bool


class GeneralGet(BaseApi):
    """
    Get for the General endpoint.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(GeneralGet, self).__init__(*args, **kwargs)
        self.endpoint = 'general'

    def balance(self, advanced=False):
        """
        Retrieves Balance for your Account if no additional parameter is provided

        - Retrieves Balance and Calls Statistics for your Account if "advanced" parameter is true

        :param advanced: True for Calls Statistics
        :type advanced: :py:class:`bool`
        :returns: :py:class:`dict`
        """
        method = "getBalance"

        parameters = {}
        if advanced:
            if not isinstance(advanced, bool):
                raise ValueError("To retrieve Balance and Calls Statistics use True")
            parameters["advanced"] = convert_bool(advanced)
        return self._voipms_client._get(method, parameters)

    def conference(self, conference=None):
        """
        Retrieves a list of Conferences if no additional parameter is provided

        - Retrieves a specific Conference if a conference code is provided

        :param conference: Code for a specific Conference (Example: 1599)
        :type conference: :py:class:`int`
        :returns: :py:class:`dict`
        """
        method = "getConference"

        parameters = {}
        if conference:
            if not isinstance(conference, int):
                raise ValueError("Code for a specific Conference (Example: 1599)")
            parameters["conference"] = conference
        return self._voipms_client._get(method, parameters)

    def conference_members(self, member=None):
        """
        Retrieves a list of Member profiles if no additional parameter is provided

        - Retrieves a specific member if a member code is provided

        :param member: Code for a specific Member profile (Example: 1599)
        :type member: :py:class:`int`
        :returns: :py:class:`dict`
        """
        method = "getConferenceMembers"

        parameters = {}
        if member:
            if not isinstance(member, int):
                raise ValueError("Code for a specific Member profile (Example: 1599)")
            parameters["member"] = member
        return self._voipms_client._get(method, parameters)

    def conference_recordings(self, conference, **kwargs):
        """
        Retrieves a list of recordings of a specific conference

        :param conference: [Required] ID for a specific Conference (Example: 5356)
        :type conference: :py:class:`int`
        :param date_from: Start Date for Filtering Transactions (Example: '2016-06-03')
        :type date_from: :py:class:`str`
        :param date_to: End Date for Filtering Transactions (Example: '2016-06-04')
        :type date_to: :py:class:`str`
        :returns: :py:class:`dict`
        """
        method = "getConferenceRecordings"

        parameters = {}

        if not isinstance(conference, int):
            raise ValueError("[Required] ID for a specific Conference (Example: 5356)")
        parameters["conference"] = conference

        if "date_from" in kwargs:
            if not isinstance(kwargs["date_from"], str):
                raise ValueError("Start Date for Filtering SMSs needs to be a str (Example: '2014-03-30')")
            validate_date(kwargs["date_from"])
            parameters["date_from"] = kwargs.pop("date_from")

        if "date_to" in kwargs:
            if not isinstance(kwargs["date_to"], str):
                raise ValueError("End Date for Filtering SMSs needs to be a str (Example: '2014-03-30')")
            validate_date(kwargs["date_to"])
            parameters["date_to"] = kwargs.pop("date_to")

        if parameters.get("date_from", None) != None and parameters.get("date_to", None) != None:
            if date_from_object > date_to_object:
                raise ValueError("The start date needs to be ealier or the same as the end date.")
            if date_to_object > datetime.now():
                raise ValueError("The end date can't be in the future.")

        return self._voipms_client._get(method, parameters)

    def conference_recording_file(self, conference, recording):
        """
        Retrieves a specific Recording File data in Base64 format

        :param conference: [Required] ID for a specific Conference (Example: 5356)
        :type conference: :py:class:`int`
        :param recording: [Required] ID for a specific Conference Recording (Example: 1543338379)
        :type recording: :py:class:`int`
        :returns: :py:class:`dict`
        """
        method = "getConferenceRecordingFile"

        parameters = {}

        if not isinstance(conference, int):
            raise ValueError("[Required] ID for a specific Conference (Example: 5356)")
        parameters["conference"] = conference

        if not isinstance(recording, int):
            raise ValueError("[Required] ID for a specific Conference Recording (Example: 1543338379)")
        parameters["recording"] = recording

        return self._voipms_client._get(method, parameters)

    def countries(self, country=None):
        """
        Retrieves a list of Countries if no additional parameter is provided

        - Retrieves a specific Country if a country code is provided

        :param country: Code for a specific Country (Example: 'CA')
        :type country: :py:class:`str`
        :returns: :py:class:`dict`
        """
        method = "getCountries"

        parameters = {}
        if country:
            if not isinstance(country, str):
                raise ValueError("Code for a specific Country as string (Example: CA)")
            parameters["country"] = country
        return self._voipms_client._get(method, parameters)

    def ip(self):
        """
        Shows the IP used by the client application requesting information from the API

        - this is the only function not using the IP for authentication.
        - the IP returned should be the one used in the API Configuration.

        :returns: :py:class:`dict`
        """
        method = "getIP"
        return self._voipms_client._get(method)

    def languages(self, language=None):
        """
        Retrieves a list of Languages if no additional parameter is provided

        - Retrieves a specific Language if a language code is provided

        :param language: Code for a specific Language (Example: 'en')
        :type language: :py:class:`str`
        :returns: :py:class:`dict`
        """
        method = "getLanguages"

        parameters = {}
        if language:
            if not isinstance(language, str):
                raise ValueError("Code for a specific Language as string (Example: 'en')")
            parameters["language"] = language
        return self._voipms_client._get(method, parameters)

    def locales(self, locales=None):
        """
        Retrieves a list of locale codes if no additional parameter is provided

        - Retrieves a specific locale code if a language code is provided

        :param locale: Code for a specific Locale Code (Example: 'en-US')
        :type locale: :py:class:`str`
        :returns: :py:class:`dict`
        """
        method = "getLocales"

        parameters = {}
        if locale:
            if not isinstance(locale, str):
                raise ValueError("Code for a specific Locale Code (Example: 'en-US')")
            parameters["locale"] = locale
        return self._voipms_client._get(method, parameters)

    def servers_info(self, server_pop=None):
        """
        Retrieves a list of Servers with their info if no additional parameter is provided

        - Retrieves a specific Server with its info if a Server POP is provided.

        :param server_pop: POP for a specific Server (Example: 1).
        :type server_pop: :py:class:`int`
        :returns: :py:class:`dict`
        """
        method = "getServersInfo"
        parameters = {}
        if server_pop:
            if not isinstance(server_pop, int):
                raise ValueError("To select a specific server use an integer (Example: 1)")
            parameters["server_pop"] = server_pop
        return self._voipms_client._get(method, parameters)

    def sequences(self, sequences=None, client=None):
        """
        Retrieves a list of Sequences if no Sequence ID is provided

        - Retrieves a specific Sequence if a Sequence ID is provided

        :param sequences: ID for a specific Sequence (Example: 5356)
        :type sequences: :py:class:`int`
        :param sequences: [Optional] ID for a specific Reseller Client (Example: 561115)
        :type sequences: :py:class:`int`
        :returns: :py:class:`dict`
        """
        method = "getSequences"

        parameters = {}
        if sequences:
            if not isinstance(sequences, int):
                raise ValueError("ID for a specific Sequence (Example: 5356)")
            parameters["sequences"] = sequences

        if client:
            if not isinstance(client, int):
                raise ValueError("[Optional] ID for a specific Reseller Client (Example: 561115)")
            parameters["client"] = client
        return self._voipms_client._get(method, parameters)

    def transaction_history(self, date_from, date_to):
        """
        Retrieves the Transaction History records between two dates

        :param date_from: [Required] Start Date for Filtering Transactions (Example: '2016-06-03')
        :type date_from: :py:class:`str`
        :param date_to: [Required] End Date for Filtering Transactions (Example: '2016-06-04')
        :type date_to: :py:class:`str`
        :returns: :py:class:`dict`
        """
        method = "getTransactionHistory"

        if not isinstance(date_from, str):
            raise ValueError("Start Date for Filtering Transactions needs to be str (Example: '2016-06-03')")

        if not isinstance(date_to, str):
            raise ValueError("End Date for Filtering Transactions needs to be str (Example: '2016-06-04')")

        date_from_object = validate_date(date_from)
        date_to_object = validate_date(date_to)
        if date_from_object > date_to_object:
            raise ValueError("The start date needs to be ealier or the same as the end date.")
        if date_to_object > datetime.now():
            raise ValueError("The end date can't be in the future.")

        parameters = {
            "date_from": date_from,
            "date_to": date_to,
        }
        return self._voipms_client._get(method, parameters)
