# coding=utf-8
"""
The Fax API endpoint order

Documentation: https://voip.ms/m/apidocs.php
"""
from voipms.baseapi import BaseApi
from voipms.helpers import convert_bool, validate_email


class FaxOrder(BaseApi):
    """
    Order for the Fax endpoint.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(FaxOrder, self).__init__(*args, **kwargs)
        self.endpoint = 'fax'

    def fax_number(self, location, quantity, **kwargs):
        """
        Orders and Adds a new Fax Number to the Account

        :param location: [Required] Location ID of the Fax Number (Values from fax.get_fax_rate_centers_can/fax.get_fax_rate_centers_usa)
        :type location: :py:class:`int`
        :param quantity: [Required] Quantity of Fax Numbers to order (Example: 3)
        :type quantity: :py:class:`int`

        :param email: Email address where send notifications when receive Fax Messages (Example: yourname@company.com)
        :type email: :py:class:`str`
        :param email_enable: Flag to enable the email notifications (True/False default False)
        :type email_enable: :py:class:`bool`
        :param email_attach_file: Flag to enable attach the Fax Message as a PDF file in the notifications (True/False default False)
        :type email_attach_file: :py:class:`bool`
        :param url_callback: URL where make a POST when you receive a Fax Message
        :type url_callback: :py:class:`str`
        :param url_callback_enable: Flag to enable the URL Callback functionality (True/False default False)
        :type url_callback_enable: :py:class:`bool`
        :param url_callback_retry: Flag to enable retry the POST action in case we don't receive "ok" (True/False default False)
        :type url_callback_retry: :py:class:`bool`
        :param test: Set to true if testing how cancel a Fax Folder (True/False)
        :type test: :py:class:`bool`

        :returns: :py:class:`dict`
        """
        method = "orderFaxNumber"

        if not isinstance(location, int):
            raise ValueError("Location ID of the Fax Number needs to be an int (Values from fax.get_fax_rate_centers_can/fax.get_fax_rate_centers_usa)")

        if not isinstance(quantity, int):
            raise ValueError("Quantity of Fax Numbers to order needs to be an int (Example: 3)")

        parameters = {
            "location": location,
            "quantity": quantity,
        }

        if "email" in kwargs:
            email = kwargs.pop("email")
            if not isinstance(email, str):
                raise ValueError("Email address where send notifications when receive Fax Messages needs to be a str (Example: yourname@company.com)")
            elif not validate_email(email):
                raise ValueError("Email address where send notifications when receive Fax Messages is not a correct email syntax")
            parameters["email"] = email

        if "email_enabled" in kwargs:
            if not isinstance(kwargs["email_enabled"], bool):
                raise ValueError("Flag to enable the email notifications needs to be a bool (True/False default False)")
            parameters["email_enabled"] = convert_bool(kwargs.pop("email_enabled"))

        if "email_attach_file" in kwargs:
            if not isinstance(kwargs["email_attach_file"], bool):
                raise ValueError("Flag to enable attach the Fax Message as a PDF file in the notifications needs to be a bool (True/False default False)")
            parameters["email_attach_file"] = convert_bool(kwargs.pop("email_attach_file"))

        if "url_callback" in kwargs:
            if not isinstance(kwargs["url_callback"], str):
                raise ValueError("URL where make a POST when you receive a Fax Message needs to be a str")
            parameters["url_callback"] = convert_bool(kwargs.pop("url_callback"))

        if "url_callback_enable" in kwargs:
            if not isinstance(kwargs["url_callback_enable"], bool):
                raise ValueError("Flag to enable the URL Callback functionality needs to be a bool (True/False default False)")
            parameters["url_callback_enable"] = convert_bool(kwargs.pop("url_callback_enable"))

        if "url_callback_retry" in kwargs:
            if not isinstance(kwargs["url_callback_retry"], bool):
                raise ValueError("Flag to enable retry the POST action in case we don't receive \"ok\" (True/False default False)")
            parameters["url_callback_retry"] = convert_bool(kwargs.pop("url_callback_retry"))

        if "test" in kwargs:
            if not isinstance(kwargs["test"], bool):
                raise ValueError("Set to true if testing how cancel a Fax Folder needs to be a bool (True/False)")
            else:
                parameters["test"] = convert_bool(kwargs.pop("test"))

        if len(kwargs) > 0:
            not_allowed_parameters = ""
            for key, value in kwargs.items():
                not_allowed_parameters += key + " "
            raise ValueError("Parameters not allowed: {}".format(not_allowed_parameters))

        return self._voipms_client._get(method, parameters)
