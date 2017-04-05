# coding=utf-8
"""
The Fax API endpoint send

Documentation: https://voip.ms/m/apidocs.php
"""
from voipms.baseapi import BaseApi
from voipms.helpers import validate_email, convert_bool


class FaxSend(BaseApi):
    """
    Send for the Fax endpoint.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(FaxSend, self).__init__(*args, **kwargs)
        self.endpoint = 'fax'

    def fax_message(self, to_number, from_name, from_number, file, **kwargs):
        """
        Send a Fax message to a Destination Number

        :param to_number: [Required] Destination DID Number (Example: 5552341234)
        :type to_number: :py:class:`int`
        :param from_name: [Required] Name of the sender
        :type from_name: :py:class:`str`
        :param from_number: [Required] DID number of the Fax sender (Example: 5552341234)
        :type from_number: :py:class:`int`
        :param file: [Required] The file must be encoded in Base64 and in one of the following formats: pdf, txt, jpg, gif, png, tif
        :type file: :py:class:`str`

        :param send_email_enabled: Flag to enable the send of a copy of your Fax via email (True/False default False)
        :type send_email_enabled: :py:class:`bool`
        :param send_email: Email address where you want send a copy of your Fax.
        :type send_email: :py:class:`str`
        :param station_id: A word to identify a equipment or department sending the Fax
        :type station_id: :py:class:`str`
        :param test: Set to true if testing how cancel a Fax Folder (True/False)
        :type test: :py:class:`bool`

        :returns: :py:class:`dict`
        """
        method = "sendFaxMessage"

        if not isinstance(to_number, int):
            raise ValueError("Destination DID Number needs to be an int (Example: 5552341234)")

        if not isinstance(from_name, str):
            raise ValueError("Name of the sender  needs to be a str")

        if not isinstance(from_number, int):
            raise ValueError("DID number of the Fax sender needs to be an int (Example: 5552341234)")

        if not isinstance(file, str):
            raise ValueError("The file must be encoded in Base64 and in one of the following formats: pdf, txt, jpg, gif, png, tif and needs to be a str")

        parameters = {
            "to_number": to_number,
            "from_name": from_name,
            "from_number": from_number,
            "file": file,
        }

        if "send_email_enabled" in kwargs:
            if not isinstance(kwargs["send_email_enabled"], bool):
                raise ValueError("Flag to enable the send of a copy of your Fax via email needs to be a bool (True/False default False)")
            parameters["send_email_enabled"] = convert_bool(kwargs.pop("send_email_enabled"))

        if "send_email" in kwargs:
            send_email = kwargs.pop("send_email")
            if not isinstance(send_email, str):
                raise ValueError("Email address where you want send a copy of your Fax needs to be a str (Example: yourname@company.com)")
            elif not validate_email(send_email):
                raise ValueError("Email address where you want send a copy of your Fax is not a correct email syntax")
            parameters["send_email"] = send_email

        if "station_id" in kwargs:
            if not isinstance(kwargs["station_id"], str):
                raise ValueError("A word to identify a equipment or department sending the Fax needs to be a str")
            parameters["station_id"] = kwargs.pop("station_id")

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
