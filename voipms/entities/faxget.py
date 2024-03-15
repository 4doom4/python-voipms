# coding=utf-8
"""
The Fax API endpoint get

Documentation: https://voip.ms/m/apidocs.php
"""
from voipms.baseapi import BaseApi
from voipms.helpers import validate_date


class FaxGet(BaseApi):
    """
    Get for the Fax endpoint.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(FaxGet, self).__init__(*args, **kwargs)
        self.endpoint = 'fax'

    def backorders(self, backorder_id=None):
        """
        Retrieves a list of backorder DIDs if no additional parameter is provided

        - Retrieves a specific backorder DID if a backorder DID code is provided

        :param backorder_id: ID for a specific backorder DID
        :type backorder_id: :py:class:`str`

        :returns: :py:class:`dict`
        """
        method = "getBackOrders"

        parameters = {
        }

        if backorder_id:
            if not isinstance(backorder_id, str):
                raise ValueError("ID for a specific backorder DID")
            else:
                parameters["backorder_id"] = backorder_id

        return self._voipms_client._get(method, parameters)

    def fax_provinces(self, province=None):
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

    def fax_states(self, state=None):
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

    def fax_rate_centers_can(self, province):
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

    def fax_rate_centers_usa(self, state):
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

    def fax_numbers_info(self, did=None):
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

    def fax_numbers_portability(self, did):
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

    def fax_messages(self, **kwargs):
        """
        Retrieves a list of Fax Messages

        :param date_from: Start Date for Filtering Fax Messages (Example: '2014-03-30')
                     - Default value: Today
        :type date_from: :py:class:`str`
        :param date_to: End Date for Filtering Fax Messages (Example: '2014-03-30')
                   - Default value: Today
        :type date_to: :py:class:`str`
        :param folder: Name of specific Fax Folder (Example: SENT)
                       - Default value: ALL
        :type folder: :py:class:`str`

        :returns: :py:class:`dict`
        """
        method = "getFaxMessages"

        parameters = {
        }

        if "date_from" in kwargs:
            if not isinstance(kwargs["date_from"], str):
                raise ValueError("Start Date for Filtering Fax Messages needs to be a str (Example: '2014-03-30')")
            validate_date(kwargs["date_from"])
            parameters["from"] = kwargs.pop("date_from")

        if "date_to" in kwargs:
            if not isinstance(kwargs["date_to"], str):
                raise ValueError("End Date for Filtering Fax Messages needs to be a str (Example: '2014-03-30')")
            validate_date(kwargs["date_to"])
            parameters["to"] = kwargs.pop("date_to")

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

    def fax_message_pdf(self, fax_id):
        """
        Retrieves a Base64 code of the Fax Message to create a PDF file

        :param fax_id: [Required] ID of the Fax Message requested (Values from fax.get.fax_messages)
        :type fax_id: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "getFaxMessagePDF"

        if not isinstance(fax_id, int):
            raise ValueError("ID of the Fax Message requested needs to be an int (Values from fax.get.fax_messages)")

        parameters = {
            "id": fax_id,
        }

        return self._voipms_client._get(method, parameters)

    def fax_folders(self):
        """
        Retrieves a list of Fax Folders from your account

        :returns: :py:class:`dict`
        """
        method = "getFaxFolders"

        parameters = {
        }

        return self._voipms_client._get(method, parameters)

    def email_to_fax(self, fax_id=None):
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
