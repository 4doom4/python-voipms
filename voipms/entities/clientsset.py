# coding=utf-8
"""
The Clients API endpoint set

Documentation: https://voip.ms/m/apidocs.php
"""
from voipms.baseapi import BaseApi
from voipms.helpers import validate_email


class ClientsSet(BaseApi):
    """
    Set for the Clients endpoint.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(ClientsSet, self).__init__(*args, **kwargs)
        self.endpoint = 'clients'

    def client(self, client, email, password, firstname,
               lastname, phone_number, **kwargs):
        """
        Updates Reseller Client information

        :param client: [Required] ID for a specific Reseller Client (Example: 561115)
        :type client: :py:class:`int`
        :param email: [Required] Client's e-mail
        :type email: :py:class:`str`
        :param password: [Required] Client's Password
        :type password: :py:class:`str`
        :param firstname: [Required] Client's Firstname
        :type firstname: :py:class:`str`
        :param lastname: [Required] Client's Lastname
        :type lastname: :py:class:`str`
        :param phone_number: [Required] Client's Phone Number
        :type phone_number: :py:class:`str`
        :param **kwargs: All optional parameters
        :type **kwargs: :py:class:`dict`

        :param company: Client's Company
        :type company: :py:class:`str`
        :param address: Client's Address
        :type address: :py:class:`str`
        :param city: Client's City
        :type city: :py:class:`str`
        :param state: Client's State
        :type state: :py:class:`str`
        :param country: Client's Country (Values from general.get_countries)
        :type country: :py:class:`str`
        :param zip: Client's Zip Code
        :type zip: :py:class:`str`
        :param balance_management: Balance Management for Client (Values from clients.get_balance_management)
        :type balance_management: :py:class:`str`

        :returns: :py:class:`dict`
        """
        method = "setClient"

        if not isinstance(client, int):
            raise ValueError("ID for a specific Reseller Client needs to be in int (Example: 561115)")

        if not isinstance(email, str):
            raise ValueError("Client's e-mail needs to be a str")
        else:
            if not validate_email(email):
                raise ValueError("Client's e-mail is not a correct email syntax")

        if not isinstance(password, str):
            raise ValueError("Client's Password needs to be a str")

        if not isinstance(firstname, str):
            raise ValueError("Client's Firstname needs to be a str")

        if not isinstance(lastname, str):
            raise ValueError("Client's Lastname needs to be a str")

        if not isinstance(phone_number, str):
            raise ValueError("Client's Phone Number needs to be a str")

        parameters = {
            "client": client,
            "email": email,
            "password": password,
            "firstname": firstname,
            "lastname": lastname,
            "phone_number": phone_number,
        }

        if "company" in kwargs:
            if not isinstance(kwargs["company"], str):
                raise ValueError("Client's Company needs to be a str")
            parameters["company"] = kwargs.pop("company")

        if "address" in kwargs:
            if not isinstance(kwargs["address"], str):
                raise ValueError("Client's Address needs to be a str")
            parameters["address"] = kwargs.pop("address")

        if "city" in kwargs:
            if not isinstance(kwargs["city"], str):
                raise ValueError("Client's City needs to be a str")
            parameters["city"] = kwargs.pop("city")

        if "state" in kwargs:
            if not isinstance(kwargs["state"], str):
                raise ValueError("Client's State needs to be a str")
            parameters["state"] = kwargs.pop("state")

        if "country" in kwargs:
            if not isinstance(kwargs["country"], str):
                raise ValueError("Client's Country needs to be a str (Values from general.get_countries)")
            parameters["country"] = kwargs.pop("country")

        if "zip" in kwargs:
            if not isinstance(kwargs["zip"], str):
                raise ValueError("Client's Zip Code needs to be a str")
            parameters["zip"] = kwargs.pop("zip")

        if "balance_management" in kwargs:
            if not isinstance(kwargs["balance_management"], str):
                raise ValueError("Balance Management for Client (Values from clients.get_balance_management)")
            parameters["balance_management"] = kwargs.pop("balance_management")

        if len(kwargs) > 0:
            not_allowed_parameters = ""
            for key, value in kwargs.items():
                not_allowed_parameters += key + " "
            raise ValueError("Parameters not allowed: {}".format(not_allowed_parameters))

        return self._voipms_client._get(method, parameters)

    def client_threshold(self, client, threshold, email=None):
        """
        Update the Threshold Amount for a specific Reseller Client

        - Update the Threshold notification e-mail for a specific Reseller Client if the e-mail address is provided

        :param client: [Required] ID for a specific Reseller Client (Example: 561115)
        :type client: :py:class:`int`
        :param threshold: [Required] Threshold amount between 1 and 250 (Example: 10)
        :type threshold: :py:class:`int`
        :param email: Client's e-mail for balance threshold notification
        :type email: :py:class:`str`
        :returns: :py:class:`dict`
        """
        method = "setClientThreshold"

        if not isinstance(client, int):
            raise ValueError("ID for a specific Reseller Client needs to be an int (Example: 561115)")

        if not isinstance(threshold, int):
            raise ValueError("Threshold amount between 1 and 250 needs to be an int (Example: 10)")
        else:
            if not 1 <= threshold <= 250:
                raise ValueError("Threshold amount needs to be between 1 and 250")

        parameters = {
            "client": client,
            "threshold": threshold,
        }

        if email:
            if not isinstance(email, str):
                raise ValueError("Client's e-mail for balance threshold notification needs to be a str")
            else:
                if not validate_email(email):
                    raise ValueError("Client's e-mail is not a correct email syntax")
                else:
                    parameters["email"] = email

        return self._voipms_client._get(method, parameters)
