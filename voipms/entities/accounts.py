import socket

from voipms.baseapi import BaseApi
from voipms.helpers import validate_date


class Accounts(BaseApi):
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(Accounts, self).__init__(*args, **kwargs)
        self.endoint = 'accounts'

    def create_sub_account(self, username, password, protocol, auth_type, device_type,
                           lock_international, international_route, music_on_hold,
                           allowed_codecs, dtmf_mode, nat, **kwargs):
        """
        Adds a new Sub Account entry to your Account

        :param username: [Required] Username for the Sub Account (Example: 'VoIP')
        :type username: All :py:class:`str`
        :param password: [Required] Sub Account Password (For Password Authentication)
        :type password: All :py:class:`str`
        :param protocol: [Required] Protocol used for the Sub Account (Values from accounts.get_protocols)
        :type protocol: All :py:class:`int`
        :param auth_type: [Required] Authorization Type Code (Values from accounts.get_auth_types)
        :type auth_type: All :py:class:`int`
        :param device_type: [Required] Device Type Code (Values from accounts.get_device_types)
        :type device_type: All :py:class:`int`
        :param lock_international: [Required] Lock International Code (Values from accounts.get_lock_international)
        :type lock_international: All :py:class:`int`
        :param international_route: [Required] Route Code (Values from accounts.get_routes)
        :type international_route: All :py:class:`int`
        :param music_on_hold: [Required] Music on Hold Code (Values from accounts.get_music_on_hold)
        :type music_on_hold: All :py:class:`str`
        :param allowed_codecs: [Required] List of Allowed Codecs (Values from accounts.get_allowed_codecs)
                               Codecs separated by semicolon (Example: ulaw;g729;gsm)
        :type allowed_codecs: All :py:class:`str`
        :param dtmf_mode: [Required] DTMF Mode Code (Values from accounts.get_dtmf_modes)
        :type dtmf_mode: All :py:class:`str`
        :param nat: [Required] NAT Mode Code (Values from accounts.get_nat)
        :type nat: All :py:class:`str`
        :param **kwargs: All optional parameters
        :type **kwargs: All :py:class:`str`

        :param description:  Sub Account Description (Example: 'VoIP Account')
        :type description: All :py:class:`str`
        :param ip: Sub Account IP  (For IP Authentication)
        :type ip: All :py:class:`str`
        :param callerid_number: Caller ID Override
        :type callerid_number: All :py:class:`str`
        :param canada_routing: Route Code (Values from accounts.get_routes)
        :type canada_routing: All :py:class:`int`
        :param internal_extension: Sub Account Internal Extension (Example: 1 -> Creates 101)
        :type internal_extension: All :py:class:`int`
        :param internal_voicemail: Sub Account Internal Voicemail (Example: 101)
        :type internal_voicemail: All :py:class:`str`
        :param internal_dialtime: Sub Account Internal Dialtime (Example: 60 -> seconds)
        :type internal_dialtime: All :py:class:`int`
        :param reseller_client: Reseller Account ID (Example: 561115)
        :type reseller_client: All :py:class:`int`
        :param reseller_package: Reseller Package (Example: 92364)
        :type reseller_package: All :py:class:`int`
        :param reseller_nextbilling: Reseller Next Billing Date (Example: '2012-12-31')
        :type reseller_nextbilling: All :py:class:`str`
        :param reseller_chargesetup: True if you want to charge Package Setup Fee after Save
        :type reseller_chargesetup: All :py:class:`bool`

        :returns: :py:class:`dict`
        """
        method = "createSubAccount"

        if not isinstance(username, str):
            raise ValueError("Username needs to be a str")

        if not isinstance(password, str):
            raise ValueError("Sub Account Password needs to be a str (For Password Authentication)")

        if not isinstance(protocol, int):
            raise ValueError("Protocol value needs to be an int (Values from accounts.get_protocols)")

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
            "username": username,
            "password": password,
            "protocol": protocol,
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

        parameters.update(kwargs)

        return self._voipms_client._get(method, parameters)

    def del_sub_account(self, account_id):
        """
        Retrieves a list of Allowed Codecs if no additional parameter is provided

        - Retrieves a specific Allowed Codec if a codec code is provided

        :param auth_type: Code for a specific Codec (Example: 'ulaw;g729;gsm')
        :type auth_type: :py:class:`str`
        :returns: :py:class:`dict`
        """
        method = "delSubAccount"

        parameters = {}
        if account_id:
            if not isinstance(account_id, int):
                raise ValueError("ID for a specific Sub Account as int (Example: 99785) ")
            else:
                parameters["id"] = account_id
        return self._voipms_client._get(method, parameters)

    def get_allowed_codecs(self, codec=None):
        """
        Retrieves a list of Allowed Codecs if no additional parameter is provided

        - Retrieves a specific Allowed Codec if a codec code is provided

        :param auth_type: Code for a specific Codec (Example: 'ulaw;g729;gsm')
        :type auth_type: :py:class:`str`
        :returns: :py:class:`dict`
        """
        method = "getAllowedCodecs"

        parameters = {}
        if codec:
            if not isinstance(codec, str):
                raise ValueError("Code for a specific Codec as str (Example: 'ulaw')")
            else:
                parameters["codec"] = codec
        return self._voipms_client._get(method, parameters)

    def get_auth_types(self, auth_type=None):
        """
        Retrieves a list of Authentication Types if no additional parameter is provided

        - Retrieves a specific Authentication Type if an auth type code is provided

        :param auth_type: Code for a specific Authorization Type (Example: 2)
        :type auth_type: :py:class:`int`
        :returns: :py:class:`dict`
        """
        method = "getAuthTypes"

        parameters = {}
        if auth_type:
            if not isinstance(auth_type, int):
                raise ValueError("Code for a specific Authorization Type as int (Example: 2)")
            else:
                parameters["type"] = auth_type
        return self._voipms_client._get(method, parameters)

    def get_device_types(self, device_type=None):
        """
        Retrieves a list of Device Types if no additional parameter is provided

        - Retrieves a specific Device Type if a device type code is provided

        :param device_type: Code for a specific Device Type (Example: 1)
        :type device_type: :py:class:`int`
        :returns: :py:class:`dict`
        """
        method = "getDeviceTypes"

        parameters = {}
        if device_type:
            if not isinstance(device_type, int):
                raise ValueError("Code for a specific Device Type as int (Example: 1)")
            else:
                parameters["device_type"] = device_type
        return self._voipms_client._get(method, parameters)

    def get_dtmf_modes(self, dtmf_mode=None):
        """
        Retrieves a list of DTMF Modes if no additional parameter is provided

        - Retrieves a specific DTMF Mode if a DTMF mode code is provided

        :param dtmf_mode: Code for a specific DTMF Mode (Example: 'inband')
        :type dtmf_mode: :py:class:`str`
        :returns: :py:class:`dict`
        """
        method = "getDTMFModes"

        parameters = {}
        if dtmf_mode:
            if not isinstance(dtmf_mode, str):
                raise ValueError("Code for a specific DTMF Mode as str (Example: 'inband')")
            else:
                parameters["dtmf_mode"] = dtmf_mode
        return self._voipms_client._get(method, parameters)

    def get_lock_international(self, lock_international=None):
        """
        Retrieves a list of Lock Modes if no additional parameter is provided

        - Retrieves a specific Lock Mode if a lock code is provided

        :param lock_international: Code for a specific Lock International Mode (Example: 1)
        :type lock_international: :py:class:`int`
        :returns: :py:class:`dict`
        """
        method = "getLockInternational"

        parameters = {}
        if lock_international:
            if not isinstance(lock_international, int):
                raise ValueError("Code for a specific Lock International Mode as int (Example: 1)")
            else:
                parameters["lock_international"] = lock_international
        return self._voipms_client._get(method, parameters)

    def get_music_on_hold(self, music_on_hold=None):
        """
        Retrieves a list of Music on Hold Options if no additional parameter is provided

        - Retrieves a specific Music on Hold Option if a MOH code is provided

        :param music_on_hold: Code for a specific Music on Hold (Example: 'jazz')
        :type music_on_hold: :py:class:`str`
        :returns: :py:class:`dict`
        """
        method = "getMusicOnHold"

        parameters = {}
        if music_on_hold:
            if not isinstance(music_on_hold, str):
                raise ValueError("Code for a specific Music on Hold as str (Example: 'jazz')")
            else:
                parameters["music_on_hold"] = music_on_hold
        return self._voipms_client._get(method, parameters)

    def get_nat(self, nat=None):
        """
        Retrieves a list of NAT Options if no additional parameter is provided

        - Retrieves a specific NAT Option if a NAT code is provided

        :param nat: Code for a specific NAT Option (Example: 'route')
        :type nat: :py:class:`str`
        :returns: :py:class:`dict`
        """
        method = "getNAT"

        parameters = {}
        if nat:
            if not isinstance(nat, str):
                raise ValueError("Code for a specific NAT Option as str (Example: 'route')")
            else:
                parameters["nat"] = nat
        return self._voipms_client._get(method, parameters)

    def get_protocols(self, protocol=None):
        """
        Retrieves a list of Protocols if no additional parameter is provided

        - Retrieves a specific Protocol if a protocol code is provided

        :param protocol: Code for a specific Protocol (Example: 3)
        :type protocol: :py:class:`int`
        :returns: :py:class:`dict`
        """
        method = "getProtocols"

        parameters = {}
        if protocol:
            if not isinstance(protocol, int):
                raise ValueError("Code for a specific Protocol as int (Example: 3)")
            else:
                parameters["protocol"] = protocol
        return self._voipms_client._get(method, parameters)

    def get_registration_status(self, account):
        """
        Retrieves the Registration Status of a specific account

        :param account: Specific Account (Example: '100001_VoIP')
        :type account: :py:class:`str`
        :returns: :py:class:`dict`
        """
        method = "getRegistrationStatus"

        parameters = {}
        if account:
            if not isinstance(account, str):
                raise ValueError("Specific Account as str (Example: '100001_VoIP')")
            else:
                parameters["account"] = account
        else:
            raise ValueError("Specific Account (Example: '100001_VoIP')")
        return self._voipms_client._get(method, parameters)

    def get_report_estimated_hold_time(self, time_type=None):
        """
        Retrieves a list of 'ReportEstimateHoldTime' Types if no additional parameter is provided

        - Retrieves a specific 'ReportEstimateHoldTime' Type if a type code is provided

        :param time_type: Code for a specific 'ReportEstimatedHoldTime' Type (Example: 'yes')
        :type time_type: :py:class:`str`
        :returns: :py:class:`dict`
        """
        method = "getReportEstimatedHoldTime"

        parameters = {}
        if time_type:
            if not isinstance(time_type, str):
                raise ValueError("Code for a specific ReportEstimatedHoldTime Type as str (Example: 'yes')")
            else:
                parameters["type"] = time_type
        return self._voipms_client._get(method, parameters)

    def get_routes(self, route=None):
        """
        Retrieves a list of Route Options if no additional parameter is provided

        - Retrieves a specific Route Option if a route code is provided

        :param route: Code for a specific Route (Example: 2)
        :type route: :py:class:`int`
        :returns: :py:class:`dict`
        """
        method = "getRoutes"

        parameters = {}
        if route:
            if not isinstance(route, int):
                raise ValueError("Code for a specific Route as int (Example: 2)")
            else:
                parameters["route"] = route
        return self._voipms_client._get(method, parameters)

    def get_sub_accounts(self, account=None):
        """
        Retrieves all Sub Accounts if no additional parameter is provided

        - Retrieves Reseller Client Accounts if Reseller Client ID is provided
        - Retrieves a specific Sub Account if a Sub Account is provided

        :param account: Parameter could have the following values:
                            * Empty Value [Not Required]
                            * Specific Sub Account (Example: '100000_VoIP')
                            * Specific Reseller Client ID (Example: 561115)
        :type account: :py:class:`str`
        :returns: :py:class:`dict`
        """
        method = "getSubAccounts"

        parameters = {}
        if account:
            if not isinstance(account, str):
                raise ValueError("Parameter could have the following values: Empty Value, Specific Sub Account (Example: '100000_VoIP'), Specific Reseller Client ID (Example: 561115)")
            else:
                parameters["account"] = account
        return self._voipms_client._get(method, parameters)

    def set_sub_account(self, account_id, password, auth_type, device_type,
                        lock_international, international_route, music_on_hold,
                        allowed_codecs, dtmf_mode, nat, **kwargs):
        """
        Updates Sub Account information

        :param account_id: [Required] Sub Account ID (Example: 10236)
        :type account_id: All :py:class:`int`
        :param password:  [Required] Sub Account Password (For Password Authentication)
        :type password: All :py:class:`str`
        :param auth_type: [Required] Authorization Type Code (Values from accounts.get_auth_types)
        :type auth_type: All :py:class:`int`
        :param device_type: [Required] Device Type Code (Values from accounts.get_device_types)
        :type device_type: All :py:class:`int`
        :param lock_international: [Required] Lock International Code (Values from accounts.get_lock_international)
        :type lock_international: All :py:class:`int`
        :param international_route: [Required] Route Code (Values from accounts.get_routes)
        :type international_route: All :py:class:`int`
        :param music_on_hold: [Required] Music on Hold Code (Values from accounts.get_music_on_hold)
        :type music_on_hold: All :py:class:`str`
        :param allowed_codecs: [Required] List of Allowed Codecs (Values from accounts.get_allowed_codecs)
                               Codecs separated by semicolon (Example: ulaw;g729;gsm)
        :type allowed_codecs: All :py:class:`str`
        :param dtmf_mode: [Required] DTMF Mode Code (Values from accounts.get_dtmf_modes)
        :type dtmf_mode: All :py:class:`str`
        :param nat: [Required] NAT Mode Code (Values from accounts.get_nat)
        :type nat: All :py:class:`str`
        :param **kwargs: All optional parameters
        :type **kwargs: All :py:class:`str`

        :param description:  Sub Account Description (Example: 'VoIP Account')
        :type description: All :py:class:`str`
        :param ip: Sub Account IP  (For IP Authentication)
        :type ip: All :py:class:`str`
        :param callerid_number: Caller ID Override
        :type callerid_number: All :py:class:`str`
        :param canada_routing: Route Code (Values from accounts.get_routes)
        :type canada_routing: All :py:class:`int`
        :param internal_extension: Sub Account Internal Extension (Example: 1 -> Creates 101)
        :type internal_extension: All :py:class:`int`
        :param internal_voicemail: Sub Account Internal Voicemail (Example: 101)
        :type internal_voicemail: All :py:class:`str`
        :param internal_dialtime: Sub Account Internal Dialtime (Example: 60 -> seconds)
        :type internal_dialtime: All :py:class:`int`
        :param reseller_client: Reseller Account ID (Example: 561115)
        :type reseller_client: All :py:class:`int`
        :param reseller_package: Reseller Package (Example: 92364)
        :type reseller_package: All :py:class:`int`
        :param reseller_nextbilling: Reseller Next Billing Date (Example: '2012-12-31')
        :type reseller_nextbilling: All :py:class:`str`
        :param reseller_chargesetup: True if you want to charge Package Setup Fee after Save
        :type reseller_chargesetup: All :py:class:`bool`

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

        parameters.update(kwargs)

        return self._voipms_client._get(method, parameters)
