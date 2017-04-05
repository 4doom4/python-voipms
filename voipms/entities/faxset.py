# coding=utf-8
"""
The Fax API endpoint set

Documentation: https://voip.ms/m/apidocs.php
"""
from voipms.baseapi import BaseApi
from voipms.helpers import convert_bool, validate_email


class FaxSet(BaseApi):
    """
    Set for the Fax endpoint.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(FaxSet, self).__init__(*args, **kwargs)
        self.endpoint = 'fax'

    def fax_folder(self, name, **kwargs):
        """
        Create or update the information of a specific Fax Folder

        :param name: [Required] Name of the Fax Folder to create or update (Example: FAMILY)
        :type name: :py:class:`int`

        :param fax_id: ID of the Fax Folder to edit (Values from fax.get_fax_folders)
        :type fax_id: :py:class:`int`
        :param test: Set to true if testing how cancel a Fax Folder (True/False)
        :type test: :py:class:`bool`

        :returns: :py:class:`dict`
        """
        method = "setFaxFolder"

        if not isinstance(name, str):
            raise ValueError("Name of the Fax Folder to create or update needs to be a str (Example: FAMILY)")

        parameters = {
            "name": name,
        }

        if "fax_id" in kwargs:
            if not isinstance(kwargs["fax_id"], int):
                raise ValueError("ID of the Fax Folder to edit needs to be an int (Values from fax.get_fax_folders)")
            parameters["id"] = kwargs.pop("fax_id")

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

    def email_to_fax(self, auth_email, from_number_id, security_code, **kwargs):
        """
        eate or update the information of a specific "Email to Fax configuration"

        :param auth_email: [Required] Email address from you will sent Fax Messages
        :type auth_email: :py:class:`str`
        :param from_number_id: [Required] Fax number that will appear as fax sender. (values from fax.get_fax_numbers_info)
        :type from_number_id: :py:class:`int`
        :param security_code: [Required] An alphanumeric code to identify your emails before send as Fax
        :type security_code: :py:class:`str`

        :param fax_id: ID of the "Email to Fax" to edit (Values from fax.get_email_to_fax)
        :type fax_id: :py:class:`int`
        :param enabled: If Enable, we will send Fax Message when we receive an email from the provided address (True/False)
        :type enabled: :py:class:`bool`
        :param security_code_enabled: If Enable, we will check the mail subject if this include a Security Code before send the Fax (True/False)
        :type security_code_enabled: :py:class:`bool`
        :param test: Set to true if testing how cancel a Fax Folder (True/False)
        :type test: :py:class:`bool`

        :returns: :py:class:`dict`
        """
        method = "setEmailToFax"

        if not isinstance(auth_email, str):
            raise ValueError("Email address from you will sent Fax Messages needs to be a str")
        elif not validate_email(auth_email):
                raise ValueError("Email address from you will sent Fax Messages is not a correct email syntax")

        if not isinstance(from_number_id, int):
            raise ValueError("Fax number that will appear as fax sender needs to be an int (values from fax.get_fax_numbers_info)")

        if not isinstance(security_code, str):
            raise ValueError("An alphanumeric code to identify your emails before send as Fax needs to be a str")

        parameters = {
            "auth_email": auth_email,
            "from_number_id": from_number_id,
            "security_code": security_code,
        }

        if "fax_id" in kwargs:
            if not isinstance(kwargs["fax_id"], int):
                raise ValueError("ID of the \"Email to Fax\" to edit (Values from fax.get_fax_folders)")
            parameters["id"] = kwargs.pop("fax_id")

        if "enabled" in kwargs:
            if not isinstance(kwargs["enabled"], bool):
                raise ValueError("If Enable, we will send Fax Message when we receive an email from the provided address needs to be a bool (True/False)")
            else:
                parameters["enabled"] = convert_bool(kwargs.pop("enabled"))

        if "security_code_enabled" in kwargs:
            if not isinstance(kwargs["security_code_enabled"], bool):
                raise ValueError("If Enable, we will check the mail subject if this include a Security Code before send the Fax needs to be a bool (True/False)")
            else:
                parameters["security_code_enabled"] = convert_bool(kwargs.pop("security_code_enabled"))

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

    def fax_number_info(self, did, **kwargs):
        """
        Updates the information from a specific Fax Number

        :param did: [Required] DID Number to be ported into our network (Example: 5552341234)
        :type did: :py:class:`int`

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
        method = "setFaxNumberInfo"

        if not isinstance(did, int):
            raise ValueError("DID Number to be ported into our network needs to be an int (Example: 5552341234)")

        parameters = {
            "did": did,
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

    def fax_number_email(self, did, **kwargs):
        """
        Updates the email configuration from a specific Fax Number

        :param did: [Required] DID Number to be ported into our network (Example: 5552341234)
        :type did: :py:class:`int`

        :param email: Email address where send notifications when receive Fax Messages (Example: yourname@company.com)
        :type email: :py:class:`str`
        :param email_enable: Flag to enable the email notifications (True/False default False)
        :type email_enable: :py:class:`bool`
        :param email_attach_file: Flag to enable attach the Fax Message as a PDF file in the notifications (True/False default False)
        :type email_attach_file: :py:class:`bool`
        :param test: Set to true if testing how cancel a Fax Folder (True/False)
        :type test: :py:class:`bool`

        :returns: :py:class:`dict`
        """
        method = "setFaxNumberEmail"

        if not isinstance(did, int):
            raise ValueError("DID Number to be ported into our network needs to be an int (Example: 5552341234)")

        parameters = {
            "did": did,
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

    def fax_number_url_callback(self, did, **kwargs):
        """
        Updates the url callback configuration from a specific Fax Number

        :param did: [Required] DID Number to be ported into our network (Example: 5552341234)
        :type did: :py:class:`int`

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
        method = "setFaxNumberURLCallback"

        if not isinstance(did, int):
            raise ValueError("DID Number to be ported into our network needs to be an int (Example: 5552341234)")

        parameters = {
            "did": did,
        }

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
