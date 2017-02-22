from voipms.baseapi import BaseApi


class Accounts(BaseApi):
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(Accounts, self).__init__(*args, **kwargs)
        self.endoint = 'accounts'

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
                raise ValueError("Code for a specific Authorization Type (Example: 2)")
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
                raise ValueError("Code for a specific Device Type (Example: 1)")
            else:
                parameters["device_type"] = device_type
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
                raise ValueError("Code for a specific Lock International Mode (Example: 1)")
            else:
                parameters["lock_international"] = lock_international
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
                raise ValueError("Code for a specific Route (Example: 2)")
            else:
                parameters["route"] = route
        return self._voipms_client._get(method, parameters)

    def create_subaccount(self, username, password, protocol, auth_type, device_type,
                          lock_international, international_route, music_on_hold,
                          allowed_codecs, dtmf_mode, nat, **kwargs):
        """
        Adds a new Sub Account entry to your Account

        :param username: [Required] Username for the Sub Account (Example: 'VoIP')
        :type username: All :py:class:`str`
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
        :param music_on_hold: [Required] Music on Hold Code (Values from getMusicOnHold)
        :type music_on_hold: All :py:class:`str`
        :param allowed_codecs: [Required] List of Allowed Codecs (Values from getAllowedCodecs)
                               Codecs separated by semicolon (Example: ulaw;g729;gsm)
        :type allowed_codecs: All :py:class:`str`
        :param dtmf_mode: [Required] DTMF Mode Code (Values from getDTMFModes)
        :type dtmf_mode: All :py:class:`str`
        :param nat: [Required] NAT Mode Code (Values from getNAT)
        :type nat: All :py:class:`str`
        :param **kwargs: All optional parameters
        :type **kwargs: All :py:class:`str`
        :returns: :py:class:`dict`
        """
        method = "createSubAccount"

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

        if not isinstance(username, str):
            raise ValueError("Username needs to be a string")

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

        return self._voipms_client._get(method, parameters)
