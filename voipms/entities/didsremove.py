# coding=utf-8
"""
The Dids API endpoint remove

Documentation: https://voip.ms/m/apidocs.php
"""
from voipms.baseapi import BaseApi


class DidsRemove(BaseApi):
    """
    Remove for the Dids endpoint.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(DidsRemove, self).__init__(*args, **kwargs)
        self.endpoint = 'dids'

    def did_vpri(self, did, vpri=None):
        """
        Removes a DID from a VPRI

        :param vpri: Id for specific Vpri
        :type vpri: :py:class:`int`
        :param did: [Required] DID Number to be remove from our Vpri (Example: 561115)
        :type did: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "removeDIDvPRI"

        parameters = {}
        if vpri:
            if not isinstance(callback, int):
                raise ValueError("ID for a specific Callback needs to be an int (Example: 19183)")
            parameters["vpri"] = vpri
        if not isinstance(callback, int):
            raise ValueError("ID for a specific Callback needs to be an int (Example: 19183)")
        parameters["did"] = did

        return self._voipms_client._get(method, parameters)
