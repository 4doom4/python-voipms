from voipms.baseapi import BaseApi

from voipms.helpers import convert_bool, validate_email


class Clients(BaseApi):
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(Clients, self).__init__(*args, **kwargs)
        self.endoint = 'clients'

    def add_charge(self, client, charge, description=None, test=False):
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

    def add_payment(self, client, payment, description=None, test=False):
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

    def get_balance_management(self, balance_management=None):
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

    def get_charges(self, client):
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

    def get_client_packages(self, client):
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

    def get_clients(self, client=None):
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

    def get_client_threshold(self, client):
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

    def get_deposits(self, client):
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

    def get_packages(self, package=None):
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

    def get_reseller_balance(self, client):
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

    def set_client(self, client, email, password, firstname,
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

    def set_client_threshold(self, client, threshold, email=None):
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

    def signup_client(self, firstname, lastname, address, city, state, country,
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
