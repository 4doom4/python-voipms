# coding=utf-8
"""
The Dids API endpoint unconnect

Documentation: https://voip.ms/m/apidocs.php
"""
from voipms.baseapi import BaseApi


class DidsUnconnect(BaseApi):
    """
    Unconnect for the Dids endpoint.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(DidsUnconnect, self).__init__(*args, **kwargs)
        self.endpoint = 'dids'

    def did(self, did):
        """
        Updates a specific Time Condition if a time condition code is provided

        - Adds a new Time Condition entry if no time condition code is provided

        :param did: [Required] DID to be Unconnected from Reseller Sub Account(Example: 5551234567)
        :type did: :py:class:`str`

        :returns: :py:class:`dict`
        """
        method = "unconnectDID"

        if not isinstance(did, int):
            raise ValueError("DID to be Unconnected from Reseller Sub Account needs to be an int (Example: 5551234567)")

        parameters = {
            "did": did,
        }

        return self._voipms_client._get(method, parameters)
