# coding=utf-8
"""
The Accounts API endpoint set

Documentation: https://voip.ms/m/apidocs.php
"""
import socket

from voipms.baseapi import BaseApi
from voipms.helpers import validate_date


class AccountsSet(BaseApi):
    """
    Set for the Accounts endpoint.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(AccountsSet, self).__init__(*args, **kwargs)
        self.endpoint = 'accounts'

    def sub_account(self, account_id, password, auth_type, device_type,
                    lock_international, international_route, music_on_hold,
                    allowed_codecs, dtmf_mode, nat, **kwargs):
        """
        Updates Sub Account information

        :param account_id: [Required] Sub Account ID (Example: 10236)
        :type account_id: :py:class:`int`
        :param password:  [Required] Sub Account Password (For Password Authentication)
        :type password: :py:class:`str`
        :param auth_type: [Required] Authorization Type Code (Values from accounts.get_auth_types)
        :type auth_type: :py:class:`int`
        :param device_type: [Required] Device Type Code (Values from accounts.get_device_types)
        :type device_type: :py:class:`int`
        :param lock_international: [Required] Lock International Code (Values from accounts.get_lock_international)
        :type lock_international: :py:class:`int`
        :param international_route: [Required] Route Code (Values from accounts.get_routes)
        :type international_route: :py:class:`int`
        :param music_on_hold: [Required] Music on Hold Code (Values from accounts.get_music_on_hold)
        :type music_on_hold: :py:class:`str`
        :param allowed_codecs: [Required] List of Allowed Codecs (Values from accounts.get_allowed_codecs)
                               Codecs separated by semicolon (Example: ulaw;g729;gsm)
        :type allowed_codecs: :py:class:`str`
        :param dtmf_mode: [Required] DTMF Mode Code (Values from accounts.get_dtmf_modes)
        :type dtmf_mode: :py:class:`str`
        :param nat: [Required] NAT Mode Code (Values from accounts.get_nat)
        :type nat: :py:class:`str`
        :param **kwargs: All optional parameters
        :type **kwargs: :py:class:`dict`

        :param description:  Sub Account Description (Example: 'VoIP Account')
        :type description: :py:class:`str`
        :param ip: Sub Account IP  (For IP Authentication)
        :type ip: :py:class:`str`
        :param callerid_number: Caller ID Override
        :type callerid_number: :py:class:`str`
        :param canada_routing: Route Code (Values from accounts.get_routes)
        :type canada_routing: :py:class:`int`
        :param internal_extension: Sub Account Internal Extension (Example: 1 -> Creates 101)
        :type internal_extension: :py:class:`int`
        :param internal_voicemail: Sub Account Internal Voicemail (Example: 101)
        :type internal_voicemail: :py:class:`str`
        :param internal_dialtime: Sub Account Internal Dialtime (Example: 60 -> seconds)
        :type internal_dialtime: :py:class:`int`
        :param reseller_client: Reseller Account ID (Example: 561115)
        :type reseller_client: :py:class:`int`
        :param reseller_package: Reseller Package (Example: 92364)
        :type reseller_package: :py:class:`int`
        :param reseller_nextbilling: Reseller Next Billing Date (Example: '2012-12-31')
        :type reseller_nextbilling: :py:class:`str`
        :param reseller_chargesetup: True if you want to charge Package Setup Fee after Save
        :type reseller_chargesetup: :py:class:`bool`

        :returns: :py:class:`dict`
        """
        method = "setSubAccount"

        if not isinstance(account_id, int):
            raise ValueError("Sub Account ID needs to be an int (Example: 10236)")

        if not isinstance(password, str):
            raise ValueError("Sub Account Password needs to be a str (For Password Authentication)")

        if not isinstance(auth_type, int):
            raise ValueError("Auth type value needs to be an int (Values from accounts.get_auth_types)")

        if not isinstance(device_type, int):
            raise ValueError("Device type value needs to be an int (Values from accounts.get_device_types)")

        if not isinstance(lock_international, int):
            raise ValueError("Lock International Code value needs to be an int (Values from accounts.get_lock_international)")

        if not isinstance(international_route, int):
            raise ValueError("Route Code value needs to be an int (Values from accounts.get_routes)")

        if not isinstance(music_on_hold, str):
            raise ValueError("Music on Hold Code value needs to be str (Values from accounts.get_music_on_hold)")

        if not isinstance(allowed_codecs, str):
            raise ValueError("List of Allowed Codecs value needs to be str (Values from accounts.get_allowed_codecs)")

        if not isinstance(dtmf_mode, str):
            raise ValueError("DTMF Mode Code (Values from needs to be str accounts.get_dtmf_modes)")

        if not isinstance(nat, str):
            raise ValueError("DTMF Mode Code (Values from needs to be str accounts.get_nat)")

        parameters = {
            "id": account_id,
            "password": password,
            "auth_type": auth_type,
            "device_type": device_type,
            "lock_international": lock_international,
            "international_route": international_route,
            "music_on_hold": music_on_hold,
            "allowed_codecs": allowed_codecs,
            "dtmf_mode": dtmf_mode,
            "nat": nat,
        }

        if "description" in kwargs:
            if not isinstance(kwargs["description"], str):
                raise ValueError("Sub Account Description needs to be a str (Example: 'VoIP Account')")
            parameters["description"] = kwargs.pop("description")

        if "ip" in kwargs:
            ip = kwargs["ip"]
            if not isinstance(ip, str):
                raise ValueError("Sub Account IP needs to be a str (For IP Authentication)")
            try:
                socket.inet_aton(ip)
            except socket.error:
                raise ValueError("The provided IP: {} is not in the correct format (Example: 127.0.0.1)".format(ip))
            parameters["ip"] = kwargs.pop("ip")

        if "callerid_number" in kwargs:
            if not isinstance(kwargs["callerid_number"], str):
                raise ValueError("Caller ID Override needs to be a str")
            parameters["callerid_number"] = kwargs.pop("callerid_number")

        if "canada_routing" in kwargs:
            if not isinstance(kwargs["canada_routing"], int):
                raise ValueError("Route Code needs to be an int (Values from accounts.get_routes)")
            parameters["canada_routing"] = kwargs.pop("canada_routing")

        if "internal_extension" in kwargs:
            if not isinstance(kwargs["internal_extension"], int):
                raise ValueError("Sub Account Internal Extension needs to be an int (Example: 1 -> Creates 101)")
            parameters["internal_extension"] = kwargs.pop("internal_extension")

        if "internal_voicemail" in kwargs:
            if not isinstance(kwargs["internal_voicemail"], int):
                raise ValueError("Sub Account Internal Voicemail needs to be an int (Example: 101)")
            parameters["internal_voicemail"] = kwargs.pop("internal_voicemail")

        if "internal_dialtime" in kwargs:
            if not isinstance(kwargs["internal_dialtime"], int):
                raise ValueError("Sub Account Internal Dialtime needs to be an int (Example: 60 -> seconds)")
            parameters["internal_dialtime"] = kwargs.pop("internal_dialtime")

        if "reseller_client" in kwargs:
            if not isinstance(kwargs["reseller_client"], int):
                raise ValueError("Reseller Account ID needs to be an int (Example: 561115)")
            parameters["reseller_client"] = kwargs.pop("reseller_client")

        if "reseller_package" in kwargs:
            if not isinstance(kwargs["reseller_package"], int):
                raise ValueError("Reseller Package needs to be an int (Example: 92364)")
            parameters["reseller_package"] = kwargs.pop("reseller_package")

        if "reseller_nextbilling" in kwargs:
            reseller_nextbilling = kwargs["reseller_nextbilling"]
            if not isinstance(reseller_nextbilling, int):
                raise ValueError("Reseller Next Billing Date needs to be a string (Example: '2012-12-31')")
            validate_date(reseller_nextbilling)
            parameters["reseller_nextbilling"] = kwargs.pop("reseller_nextbilling")

        if "reseller_chargesetup" in kwargs:
            if not isinstance(kwargs["reseller_chargesetup"], bool):
                raise ValueError("True if you want to charge Package Setup Fee after Save")
            parameters["reseller_chargesetup"] = kwargs.pop("reseller_chargesetup")

        if len(kwargs) > 0:
            not_allowed_parameters = ""
            for key, value in kwargs.items():
                not_allowed_parameters += key + " "
            raise ValueError("Parameters not allowed: {}".format(not_allowed_parameters))

        return self._voipms_client._get(method, parameters)
