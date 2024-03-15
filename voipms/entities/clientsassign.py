# coding=utf-8
"""
The Clients API endpoint assign

Documentation: https://voip.ms/m/apidocs.php
"""
from voipms.baseapi import BaseApi
from voipms.helpers import convert_bool, validate_email


class ClientsAssign(BaseApi):
    """
    Assign for the Clients endpoint.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(ClientsAssign, self).__init__(*args, **kwargs)
        self.endpoint = 'clients'

    def did_vpri(self, did, vpri):
        """
        Assigns a Per Minute DID to a VPRI (Flat Rate DIDs can't be assigned)

        :param did: [Required] DID Number to be assigned into our Vpri (Example: 561115)
        :type did: :py:class:`int`
        :param vpri: [Required] Id for specific Vpri
        :type vpri: :py:class:`int`
        :returns: :py:class:`dict`
        """
        method = "assignDIDvPRI"

        if not isinstance(did, int):
            raise ValueError("[Required] DID Number to be assigned into our Vpri (Example: 561115)")

        if not isinstance(vpri, int):
            raise ValueError("[Required] Id for specific Vpri")

        parameters = {
            "did": did,
            "vpri": vpri,
        }

        return self._voipms_client._get(method, parameters)
