from voipms.baseapi import BaseApi
from voipms.helpers import convert_bool, validate_date, validate_email


class Dids(BaseApi):
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(Dids, self).__init__(*args, **kwargs)
        self.endoint = 'fax'

    def cancel_fax_number(self, fax_id, test=None):
        """
        Deletes a specific Fax Number from your Account

        :param fax_id: [Required] ID for a specific Fax Number (Example: 923)
        :type fax_id: :py:class:`int`

        :param test: Set to true if testing how cancel a Fax Number (True/False)
        :type test: :py:class:`bool`

        :returns: :py:class:`dict`
        """
        method = "cancelFaxNumber"

        if not isinstance(fax_id, int):
            raise ValueError("ID for a specific Fax Number needs to be an int (Example: 923)")

        parameters = {
            "id": fax_id,
        }

        if test:
            if not isinstance(test, bool):
                raise ValueError("Set to true if testing how cancel a Fax Number needs to be a bool (True/False)")
            else:
                parameters["test"] = convert_bool(test)

        return self._voipms_client._get(method, parameters)

    def delete_fax_message(self, fax_id, test=None):
        """
        Deletes a specific Fax Message from your Account

        :param fax_id: [Required] ID for a specific Fax Number (Example: 923)
        :type fax_id: :py:class:`int`

        :param test: Set to true if testing how cancel a Fax Number (True/False)
        :type test: :py:class:`bool`

        :returns: :py:class:`dict`
        """
        method = "deleteFaxMessage"

        if not isinstance(fax_id, int):
            raise ValueError("ID for a specific Fax Number needs to be an int (Example: 923)")

        parameters = {
            "id": fax_id,
        }

        if test:
            if not isinstance(test, bool):
                raise ValueError("Set to true if testing how cancel a Fax Number needs to be a bool (True/False)")
            else:
                parameters["test"] = convert_bool(test)

        return self._voipms_client._get(method, parameters)

    def del_email_to_fax(self, fax_id, test=None):
        """
        Deletes a specific "Email to Fax configuration" from your Account

        :param fax_id: [Required] ID for a specific "Email To Fax Configuration" (Example: 923)
        :type fax_id: :py:class:`int`

        :param test: Set to true if testing how cancel a "Email To Fax Configuration" (True/False)
        :type test: :py:class:`bool`

        :returns: :py:class:`dict`
        """
        method = "delEmailToFax"

        if not isinstance(fax_id, int):
            raise ValueError("ID for a specific \"Email To Fax Configuration\" needs to be an int (Example: 923)")

        parameters = {
            "id": fax_id,
        }

        if test:
            if not isinstance(test, bool):
                raise ValueError("Set to true if testing how cancel a \"Email To Fax Configuration\" needs to be a bool (True/False)")
            else:
                parameters["test"] = convert_bool(test)

        return self._voipms_client._get(method, parameters)

    def del_fax_folder(self, folder_id, test=None):
        """
        Deletes a specific Fax Folder from your Account

        :param folder_id: [Required] ID for a specific Fax Folder (Example: 923)
        :type folder_id: :py:class:`int`

        :param test: Set to true if testing how cancel a Fax Folder (True/False)
        :type test: :py:class:`bool`

        :returns: :py:class:`dict`
        """
        method = "delFaxFolder"

        if not isinstance(folder_id, int):
            raise ValueError("ID for a specific Fax Folder needs to be an int (Example: 923)")

        parameters = {
            "id": folder_id,
        }

        if test:
            if not isinstance(test, bool):
                raise ValueError("Set to true if testing how cancel a Fax Folder needs to be a bool (True/False)")
            else:
                parameters["test"] = convert_bool(test)

        return self._voipms_client._get(method, parameters)

    def get_fax_provinces(self, province=None):
        """
        Retrieves a list of Canadian Fax Provinces if no additional parameter is provided

        - Retrieves a specific Canadian Fax Province if a province code is provided

        :param province: CODE for a specific Province (Example: AB)
        :type province: :py:class:`str`

        :returns: :py:class:`dict`
        """
        method = "getFaxProvinces"

        parameters = {
        }

        if province:
            if not isinstance(province, str):
                raise ValueError("CODE for a specific Province needs to be a str (Example: AB)")
            else:
                parameters["province"] = province

        return self._voipms_client._get(method, parameters)

    def get_fax_states(self, state=None):
        """
        Retrieves a list of American Fax States if no additional parameter is provided

        - Retrieves a specific American Fax State if a state code is provided

        :param state: CODE for a specific State (Example: AL)
        :type state: :py:class:`str`

        :returns: :py:class:`dict`
        """
        method = "getFaxStates"

        parameters = {
        }

        if state:
            if not isinstance(state, str):
                raise ValueError("CODE for a specific State needs to be a str (Example: AL)")
            else:
                parameters["state"] = state

        return self._voipms_client._get(method, parameters)

    def get_fax_rate_centers_can(self, province):
        """
        Retrieves a list of Canadian Ratecenters by Province

        :param province: [Required] Province two letters code (Example: AB)
        :type province: :py:class:`str`

        :returns: :py:class:`dict`
        """
        method = "getFaxRateCentersCAN"

        if not isinstance(province, str):
            raise ValueError("Province two letters code needs to be a str (Example: AB)")

        parameters = {
            "province": province,
        }

        return self._voipms_client._get(method, parameters)

    def get_fax_rate_centers_usa(self, state):
        """
        Retrieves a list of USA Ratecenters by State

        :param state: [Required] State two letters code (Example: AL)
        :type state: :py:class:`str`

        :returns: :py:class:`dict`
        """
        method = "getFaxRateCentersUSA"

        if not isinstance(state, str):
            raise ValueError("State two letters code needs to be a str (Example: AL)")

        parameters = {
            "state": state,
        }

        return self._voipms_client._get(method, parameters)

    def get_fax_numbers_info(self, did=None):
        """
        Retrieves a list of Fax Numbers

        :param did: Fax Number to retrieves the information of a single number, or not send if you want retrieves the information of all your Fax Numbers.
        :type did: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "getFaxNumbersInfo"

        parameters = {
        }

        if did:
            if not isinstance(did, int):
                raise ValueError("Fax Number to retrieves the information of a single number, or not send if you want retrieves the information of all your Fax Numbers needs to be an int")
            else:
                parameters["did"] = did

        return self._voipms_client._get(method, parameters)

    def get_fax_numbers_portability(self, did):
        """
        Shows if a Fax Number can be ported into our network

        :param did: [Required] DID Number to be ported into our network (Example: 5552341234)
        :type did: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "getFaxNumbersPortability"

        if not isinstance(did, int):
            raise ValueError("DID Number to be ported into our network needs to be an int (Example: 5552341234)")

        parameters = {
            "did": did,
        }

        return self._voipms_client._get(method, parameters)

    def get_fax_messages(self, **kwargs):
        """
        Retrieves a list of Fax Messages

        :param from: Start Date for Filtering Fax Messages (Example: '2014-03-30')
                     - Default value: Today
        :type from: :py:class:`str`
        :param to: End Date for Filtering Fax Messages (Example: '2014-03-30')
                   - Default value: Today
        :type to: :py:class:`str`
        :param folder: Name of specific Fax Folder (Example: SENT)
                       - Default value: ALL
        :type folder: :py:class:`str`

        :returns: :py:class:`dict`
        """
        method = "getFaxMessages"

        parameters = {
        }

        if "from" in kwargs:
            if not isinstance(kwargs["from"], str):
                raise ValueError("Start Date for Filtering Fax Messages needs to be a str (Example: '2014-03-30')")
            validate_date(kwargs["from"])
            parameters["from"] = kwargs.pop("from")

        if "to" in kwargs:
            if not isinstance(kwargs["to"], str):
                raise ValueError("End Date for Filtering Fax Messages needs to be a str (Example: '2014-03-30')")
            validate_date(kwargs["to"])
            parameters["to"] = kwargs.pop("to")

        if "folder" in kwargs:
            if not isinstance(kwargs["folder"], str):
                raise ValueError("Name of specific Fax Folder needs to be a str (Example: SENT)")
            parameters["folder"] = kwargs.pop("folder")

        if len(kwargs) > 0:
            not_allowed_parameters = ""
            for key, value in kwargs.items():
                not_allowed_parameters += key + " "
            raise ValueError("Parameters not allowed: {}".format(not_allowed_parameters))

        return self._voipms_client._get(method, parameters)

    def get_fax_message_pdf(self, fax_id):
        """
        Retrieves a Base64 code of the Fax Message to create a PDF file

        :param fax_id: [Required] ID of the Fax Message requested (Values from fax.get_fax_messages)
        :type fax_id: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "getFaxMessagePDF"

        if not isinstance(fax_id, int):
            raise ValueError("ID of the Fax Message requested needs to be an int (Values from fax.get_fax_messages)")

        parameters = {
            "id": fax_id,
        }

        return self._voipms_client._get(method, parameters)

    def get_fax_folders(self):
        """
        Retrieves a list of Fax Folders from your account

        :returns: :py:class:`dict`
        """
        method = "getFaxFolders"

        parameters = {
        }

        return self._voipms_client._get(method, parameters)

    def get_email_to_fax(self, fax_id=None):
        """
        Retrieves a list of "Email to Fax configurations" from your account if no additional parameter is provided

        - Retrieves a specific "Email to Fax configuration" from your account if a ID is provided

        :param fax_id: ID of the "Email to Fax" configuration
        :type fax_id: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "getEmailToFax"

        parameters = {
        }

        if fax_id:
            if not isinstance(fax_id, int):
                raise ValueError("ID of the \"Email to Fax\" configuration needs to be an int")
            else:
                parameters["id"] = fax_id

        return self._voipms_client._get(method, parameters)

    def mail_fax_message_pdf(self, fax_id, email):
        """
        Send a Fax Message attached as a PDF file to an email destination

        :param fax_id: [Required] ID of the Fax Message requested (Values from fax.get_fax_messages)
        :type fax_id: :py:class:`int`
        :param email: [Required] Destination email address (example: yourname@company.com)
        :type email: :py:class:`str`

        :returns: :py:class:`dict`
        """
        method = "mailFaxMessagePDF"

        if not isinstance(fax_id, int):
            raise ValueError("ID of the Fax Message requested needs to be an int (Values from fax.get_fax_messages)")

        if not isinstance(email, str):
            raise ValueError("Destination email address needs to be a str(example: yourname@company.com)")
        elif not validate_email(email):
                raise ValueError("Destination email address is not a correct email syntax")

        parameters = {
            "id": fax_id,
            "email": email,
        }

        return self._voipms_client._get(method, parameters)

    def move_fax_message(self, fax_id, folder_id, test=None):
        """
        Moves a Fax Message to a different folder

        :param fax_id: [Required] ID of the Fax Message requested (Values from fax.get_fax_messages)
        :type fax_id: :py:class:`int`
        :param folder_id: [Required] ID of the destination Fax Folder (Values from fax.get_fax_folders)
        :type folder_id: :py:class:`int`

        :param test: Set to true if testing how cancel a Fax Folder (True/False)
        :type test: :py:class:`bool`

        :returns: :py:class:`dict`
        """
        method = "moveFaxMessage"

        if not isinstance(fax_id, int):
            raise ValueError("ID for a specific \"Email To Fax Configuration\" needs to be an int (Example: 923)")
        if not isinstance(folder_id, int):
            raise ValueError("ID for a specific \"Email To Fax Configuration\" needs to be an int (Example: 923)")

        parameters = {
            "fax_id": fax_id,
            "folder_id": folder_id,
        }

        if test:
            if not isinstance(test, bool):
                raise ValueError("Set to true if testing how cancel a Fax Folder needs to be a bool (True/False)")
            else:
                parameters["test"] = convert_bool(test)

        return self._voipms_client._get(method, parameters)

    def order_fax_number(self, location, quantity, **kwargs):
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

    def set_fax_folder(self, name, **kwargs):
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

    def set_email_to_fax(self, auth_email, from_number_id, security_code, **kwargs):
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

    def search_fax_area_code_can(self, area_code):
        """
        Retrieves a list of Canadian Ratecenters searched by Area Code

        :param area_code: [Required] Area code number, as the initial of the Fax Number you looking for (values from fax.get_fax_rate_centers_can)
        :type area_code: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "searchFaxAreaCodeCAN"

        if not isinstance(area_code, int):
            raise ValueError("Area code number, as the initial of the Fax Number you looking for needs to be an int (values from fax.get_fax_rate_centers_can)")

        parameters = {
            "area_code": area_code,
        }

        return self._voipms_client._get(method, parameters)

    def search_fax_area_code_usa(self, area_code):
        """
        Retrieves a list of USA Ratecenters searched by Area Code

        :param area_code: [Required] Area code number, as the initial of the Fax Number you looking for (values from fax.get_fax_rate_centers_usa)
        :type area_code: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "searchFaxAreaCodeUSA"

        if not isinstance(area_code, int):
            raise ValueError("Area code number, as the initial of the Fax Number you looking for needs to be an int (values from fax.get_fax_rate_centers_usa)")

        parameters = {
            "area_code": area_code,
        }

        return self._voipms_client._get(method, parameters)

    def set_fax_number_info(self, did, **kwargs):
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

    def set_fax_number_email(self, did, **kwargs):
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

    def set_fax_number_url_callback(self, did, **kwargs):
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

    def send_fax_message(self, to_number, from_name, from_number, file, **kwargs):
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
