# coding=utf-8
"""
The Fax API endpoint move

Documentation: https://voip.ms/m/apidocs.php
"""
from voipms.baseapi import BaseApi
from voipms.helpers import convert_bool


class FaxMove(BaseApi):
    """
    Move for the Fax endpoint.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(FaxMove, self).__init__(*args, **kwargs)
        self.endpoint = 'fax'

    def fax_message(self, fax_id, folder_id, test=None):
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
