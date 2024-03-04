# coding=utf-8
"""
The Fax API endpoint unconnect

Documentation: https://voip.ms/m/apidocs.php
"""
from voipms.baseapi import BaseApi


class FaxUnconnect(BaseApi):
    """
    Unconnect for the Fax endpoint.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(FaxUnconnect, self).__init__(*args, **kwargs)
        self.endpoint = 'fax'

    def fax(self, fax):
        """
        Updates a specific FAX DID from Reseller Client Sub Account

        :param did: [Required] FAX DID to be Unconnected from Reseller Sub Account(Example: 5551234567)
        :type did: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "unconnectFAX"

        if not isinstance(did, int):
            raise ValueError("[Required] FAX DID to be Unconnected from Reseller Sub Account(Example: 5551234567)")

        parameters = {
            "did": did,
        }

        return self._voipms_client._get(method, parameters)
