# coding=utf-8
"""
The Clients API endpoint get

Documentation: https://voip.ms/m/apidocs.php
"""
from voipms.baseapi import BaseApi


class ClientsGet(BaseApi):
    """
    Get for the Clients endpoint.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(ClientsGet, self).__init__(*args, **kwargs)
        self.endpoint = 'clients'

    def balance_management(self, balance_management=None):
        """
        Retrieves a list of Balance Management Options if no additional parameter is provided

        - Retrieves a specific Balance Management Option if a code is provided

        :param balance_management: Code for a specific Balance Management Setting (Example: 1)
        :type balance_management: :py:class:`int`
        :returns: :py:class:`dict`
        """
        method = "getBalanceManagement"

        parameters = {}
        if balance_management:
            if not isinstance(balance_management, int):
                raise ValueError("Code for a specific Balance Management Setting needs to be an int (Example: 1)")
            parameters["balance_management"] = balance_management

        return self._voipms_client._get(method, parameters)

    def charges(self, client):
        """
        Retrieves Charges made to a specific Reseller Client

        :param client: [Required] ID for a specific Reseller Client (Example: 561115)
        :type client: :py:class:`int`
        :returns: :py:class:`dict`
        """
        method = "getCharges"

        parameters = {}
        if client:
            if not isinstance(client, int):
                raise ValueError("ID for a specific Reseller Client needs to be an int (Example: 561115)")
            parameters["client"] = client

        return self._voipms_client._get(method, parameters)

    def client_packages(self, client):
        """
        Retrieves a list of Packages for a specific Reseller Client

        :param client: [Required] ID for a specific Reseller Client (Example: 561115)
        :type client: :py:class:`int`
        :returns: :py:class:`dict`
        """
        method = "getClientPackages"

        parameters = {}
        if client:
            if not isinstance(client, int):
                raise ValueError("ID for a specific Reseller Client needs to be an int (Example: 561115)")
            parameters["client"] = client

        return self._voipms_client._get(method, parameters)

    def clients(self, client=None):
        """
        Retrieves a list of all Clients if no additional parameter is provided

        - Retrieves a specific Reseller Client if a Reseller Client ID is provided
        - Retrieves a specific Reseller Client if a Reseller Client e-mail is provided

        :param client: Parameter could have the following values:
                            * Empty Value [Not Required]
                            * Specific Reseller Client ID (Example: 561115)
                            * Specific Reseller Client e-mail  (Example: 'john.doe@mydomain.com')
        :type client: :py:class:`int` or `str` or ``
        :returns: :py:class:`dict`
        """
        method = "getClients"

        if not client:
            client = ""

        parameters = {
            "client": client,
        }

        return self._voipms_client._get(method, parameters)

    def client_threshold(self, client):
        """
        Retrieves the Threshold Information for a specific Reseller Client

        :param client: [Required] ID for a specific Reseller Client (Example: 561115)
        :type client: :py:class:`int`
        :returns: :py:class:`dict`
        """
        method = "getClientThreshold"

        parameters = {}
        if client:
            if not isinstance(client, int):
                raise ValueError("ID for a specific Reseller Client needs to be an int (Example: 561115)")
            parameters["client"] = client

        return self._voipms_client._get(method, parameters)

    def deposits(self, client):
        """
        Retrieves Deposits made for a specific Reseller Client

        :param client: [Required] ID for a specific Reseller Client (Example: 561115)
        :type client: :py:class:`int`
        :returns: :py:class:`dict`
        """
        method = "getDeposits"

        parameters = {}
        if client:
            if not isinstance(client, int):
                raise ValueError("ID for a specific Reseller Client needs to be an int (Example: 561115)")
            parameters["client"] = client

        return self._voipms_client._get(method, parameters)

    def packages(self, package=None):
        """
        Retrieves Deposits made for a specific Reseller Client

        :param package: Code for a specific Package (Example: 8378)
        :type package: :py:class:`int`
        :returns: :py:class:`dict`
        """
        method = "getPackages"

        parameters = {}
        if package:
            if not isinstance(package, int):
                raise ValueError("Code for a specific Package needs to be an int (Example: 8378)")
            parameters["package"] = package

        return self._voipms_client._get(method, parameters)

    def reseller_balance(self, client):
        """
        Retrieves Balance and Calls Statistics for a specific Reseller Client for the last 30 days and current day

        :param client: [Required] ID for a specific Reseller Client (Example: 561115)
        :type client: :py:class:`int`
        :returns: :py:class:`dict`
        """
        method = "getResellerBalance"

        parameters = {}
        if client:
            if not isinstance(client, int):
                raise ValueError("ID for a specific Reseller Client needs to be an int (Example: 561115)")
            parameters["client"] = client

        return self._voipms_client._get(method, parameters)
