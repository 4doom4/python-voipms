# coding=utf-8
"""
The Fax API endpoint delete

Documentation: https://voip.ms/m/apidocs.php
"""
from voipms.baseapi import BaseApi
from voipms.helpers import convert_bool


class FaxDelete(BaseApi):
    """
    Delete for the Fax endpoint.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(FaxDelete, self).__init__(*args, **kwargs)
        self.endpoint = 'fax'

    def fax_message(self, fax_id, test=None):
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

    def email_to_fax(self, fax_id, test=None):
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

    def fax_folder(self, folder_id, test=None):
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
