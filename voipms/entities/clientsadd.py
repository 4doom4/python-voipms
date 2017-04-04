# coding=utf-8
"""
The Clients API endpoint add

Documentation: https://voip.ms/m/apidocs.php
"""
from voipms.baseapi import BaseApi
from voipms.helpers import convert_bool, validate_email


class ClientsAdd(BaseApi):
    """
    Add for the Clients endpoint.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(ClientsAdd, self).__init__(*args, **kwargs)
        self.endpoint = 'clients'

    def charge(self, client, charge, description=None, test=False):
        """
        Adds a Charge to a specific Reseller Client

        :param client: [Required] ID for a specific Reseller Client (Example: 561115)
        :type client: :py:class:`int`
        :param charge: [Required] Amount of money that will be Debited from the customer (Example: 4.99)
        :type charge: :py:class:`float`
        :param description: Charge Description
        :type description: :py:class:`str`
        :param test: Set to true if testing how adding charges works
        :type test: :py:class:`str`
        :returns: :py:class:`dict`
        """
        method = "addCharge"

        if not isinstance(client, int):
            raise ValueError("ID for a specific Reseller Client needs to be an int (Example: 561115)")

        if not isinstance(charge, float):
            raise ValueError("Amount of money that will be Debited from the customer needs to be a float (Example: 4.99)")

        parameters = {
            "client": client,
            "charge": charge,
        }

        if description:
            if not isinstance(description, str):
                raise ValueError("Charge Description needs to be a str")
            parameters["description"] = description

        if test:
            if not isinstance(test, bool):
                raise ValueError("Set to True if testing how adding charges works")
            parameters["test"] = convert_bool(test)

        return self._voipms_client._get(method, parameters)

    def client(self, firstname, lastname, address, city, state, country,
               zip_code, phone_number, email, confirm_email, password,
               confirm_password, **kwargs):
        """
        Signs a new Reseller Client to your Reseller Account

        :param firstname: [Required] Client's Firstname
        :type firstname: :py:class:`str`
        :param lastname: [Required] Client's Lastname
        :type lastname: :py:class:`str`
        :param address: Client's Address
        :type address: :py:class:`str`
        :param city: Client's City
        :type city: :py:class:`str`
        :param state: Client's State
        :type state: :py:class:`str`
        :param country: Client's Country (Values from general.get_countries)
        :type country: :py:class:`str`
        :param zip_code: Client's Zip Code
        :type zip_code: :py:class:`str`
        :param phone_number: [Required] Client's Phone Number
        :type phone_number: :py:class:`str`
        :param email: [Required] Client's e-mail
        :type email: :py:class:`str`
        :param confirm_email: [Required] Client's Confirmation e-mail
        :type confirm_email: :py:class:`str`
        :param password: [Required] Client's Password
        :type password: :py:class:`str`
        :param confirm_password: [Required] Client's Password
        :type confirm_password: :py:class:`str`
        :param **kwargs: All optional parameters
        :type **kwargs: :py:class:`dict`

        :param company: Client's Company
        :type company: :py:class:`str`
        :param activate: Activates Client (Boolean: True/False)
        :type activate: :py:class:`bool`
        :param balance_management: Balance Management for Client (Values from clients.get_balance_management)
        :type balance_management: :py:class:`str`

        :returns: :py:class:`dict`
        """
        method = "signupClient"

        if not isinstance(firstname, str):
            raise ValueError("Client's Firstname needs to be a str")

        if not isinstance(lastname, str):
            raise ValueError("Client's Lastname needs to be a str")

        if not isinstance(address, str):
            raise ValueError("Client's Address needs to be a str")

        if not isinstance(city, str):
            raise ValueError("Client's City needs to be a str")

        if not isinstance(state, str):
            raise ValueError("Client's State needs to be a str")

        if not isinstance(country, str):
            raise ValueError("Client's Country needs to be a str (Values from general.get_countries)")

        if not isinstance(zip_code, str):
            raise ValueError("Client's Zip Code needs to be a str")

        if not isinstance(phone_number, str):
            raise ValueError("Client's Phone Number needs to be a str")

        if not isinstance(email, str):
            raise ValueError("Client's e-mail needs to be a str")
        else:
            if not validate_email(email):
                raise ValueError("Client's e-mail is not a correct email syntax")

        if not isinstance(confirm_email, str):
            raise ValueError("Client's Confirmation e-mail needs to be a str")
        else:
            if not validate_email(confirm_email):
                raise ValueError("Client's Confirmation e-mail is not a correct email syntax")

        if email != confirm_email:
            raise ValueError("The two provided e-mails do not match")

        if not isinstance(password, str):
            raise ValueError("Client's Password needs to be a str")

        if not isinstance(confirm_password, str):
            raise ValueError("Client's Confirmation Password needs to be a str")

        if password != confirm_password:
            raise ValueError("The two provided passwords do not match")

        parameters = {
            "firstname": firstname,
            "lastname": lastname,
            "address": address,
            "city": city,
            "state": state,
            "country": country,
            "zip": zip_code,
            "phone_number": phone_number,
            "email": email,
            "confirm_email": confirm_email,
            "password": password,
            "confirm_password": confirm_password,
        }

        if "activate" in kwargs:
            if not isinstance(kwargs["activate"], bool):
                raise ValueError("Activates Client needs to be a bool")
            parameters["activate"] = convert_bool(kwargs.pop("activate"))

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

    def payment(self, client, payment, description=None, test=False):
        """
        Adds a Payment to a specific Reseller Client

        :param client: [Required] ID for a specific Reseller Client (Example: 561115)
        :type client: :py:class:`int`
        :param payment: [Required] Amount of money that will be Credited to the customer (Example: 4.99)
        :type payment: :py:class:`float`
        :param description: Charge Description
        :type description: :py:class:`str`
        :param test: Set to true if testing how adding charges works
        :type test: :py:class:`str`
        :returns: :py:class:`dict`
        """
        method = "addPayment"

        if not isinstance(client, int):
            raise ValueError("ID for a specific Reseller Client needs to be an int (Example: 561115)")

        if not isinstance(payment, float):
            raise ValueError("Amount of money that will be Credited to the customer needs to be a float (Example: 4.99)")

        parameters = {
            "client": client,
            "payment": payment,
        }

        if description:
            if not isinstance(description, str):
                raise ValueError("Charge Description needs to be a str")
            parameters["description"] = description

        if test:
            if not isinstance(test, bool):
                raise ValueError("Set to True if testing how adding charges works")
            parameters["test"] = convert_bool(test)

        return self._voipms_client._get(method, parameters)
