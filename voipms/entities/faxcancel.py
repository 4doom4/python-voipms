# coding=utf-8
"""
The Fax API endpoint cancel

Documentation: https://voip.ms/m/apidocs.php
"""
from voipms.baseapi import BaseApi
from voipms.helpers import convert_bool


class FaxCancel(BaseApi):
    """
    Cancel for the Fax endpoint.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(FaxCancel, self).__init__(*args, **kwargs)
        self.endpoint = 'fax'

    def fax_number(self, fax_id, test=None):
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
