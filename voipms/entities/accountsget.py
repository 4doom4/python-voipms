# coding=utf-8
"""
The Accounts API endpoint get

Documentation: https://voip.ms/m/apidocs.php
"""
from voipms.baseapi import BaseApi


class AccountsGet(BaseApi):
    """
    Get for the Accounts endpoint.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(AccountsGet, self).__init__(*args, **kwargs)
        self.endpoint = 'accounts'

    def allowed_codecs(self, codec=None):
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
            parameters["codec"] = codec
        return self._voipms_client._get(method, parameters)

    def auth_types(self, auth_type=None):
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
            parameters["type"] = auth_type
        return self._voipms_client._get(method, parameters)

    def device_types(self, device_type=None):
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
            parameters["device_type"] = device_type
        return self._voipms_client._get(method, parameters)

    def dtmf_modes(self, dtmf_mode=None):
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
            parameters["dtmf_mode"] = dtmf_mode
        return self._voipms_client._get(method, parameters)

    def lock_international(self, lock_international=None):
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
            parameters["lock_international"] = lock_international
        return self._voipms_client._get(method, parameters)

    def music_on_hold(self, music_on_hold=None):
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
            parameters["music_on_hold"] = music_on_hold
        return self._voipms_client._get(method, parameters)

    def nat(self, nat=None):
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
            parameters["nat"] = nat
        return self._voipms_client._get(method, parameters)

    def protocols(self, protocol=None):
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
            parameters["protocol"] = protocol
        return self._voipms_client._get(method, parameters)

    def registration_status(self, account):
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
            parameters["account"] = account
        else:
            raise ValueError("Specific Account (Example: '100001_VoIP')")
        return self._voipms_client._get(method, parameters)

    def report_estimated_hold_time(self, time_type=None):
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
            parameters["type"] = time_type
        return self._voipms_client._get(method, parameters)

    def routes(self, route=None):
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
            parameters["route"] = route
        return self._voipms_client._get(method, parameters)

    def sub_accounts(self, account=None):
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
            parameters["account"] = account
        return self._voipms_client._get(method, parameters)
