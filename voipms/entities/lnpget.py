# coding=utf-8
"""
The Local Number Portability (LNP) API endpoint get

Documentation: https://voip.ms/m/apidocs.php
"""
from voipms.baseapi import BaseApi
from voipms.helpers import validate_date


class LNPGet(BaseApi):
    """
    Get for the Local Number Portability (LNP) endpoint.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(LNPGet, self).__init__(*args, **kwargs)
        self.endpoint = 'lnp'

    def attach(self, portid, attachid):
        """
        Retrieve the details of an attached invoice. 

        :param portid: [Required] ID of the port previously created
        :type portid: :py:class:`str`
        :param attachid: [Required] ID of the invoice (attachment) previously uploaded
        :type attachid: :py:class:`str`

        :returns: :py:class:`dict`
        """
        method = "getLNPAttach"

        if not isinstance(portid, str):
            raise ValueError("")

        if not isinstance(attachid, str):
            raise ValueError("")

        parameters = {
            "portid": portid,
            "attachid": attachid
        }

        return self._voipms_client._get(method, parameters)

    def attach_list(self, portid):
        """
        Retrieve the list of invoice (attached) files from a given portability process.

        :param portid: [Required] ID of the port previously created
        :type portid: :py:class:`str`

        :returns: :py:class:`dict`
        """
        method = "getLNPAttachList"

        if not isinstance(portid, str):
            raise ValueError("")

        parameters = {
            "portid": portid
        }

        return self._voipms_client._get(method, parameters)

    def details(self, portid):
        """
        Retrieve the details of a given portability process.

        :param portid: [Required] ID of the port previously created
        :type portid: :py:class:`str`

        :returns: :py:class:`dict`
        """
        method = "getLNPDetails"

        if not isinstance(portid, str):
            raise ValueError("ID for a specific backorder DID")

        parameters = {
            "portid": portid
        }

        return self._voipms_client._get(method, parameters)

    def list(self, portid, portStatus=None, startDate=None, endDate=None):
        """
        Retrieve the full list of all your portability processes.

        :param portid: [Required] ID of the port previously created
        :type portid: :py:class:`int`
        :param partStatus: Status code to filtering Ports. Example: precessing. (You can use values returned by the method getLNPListStatus)
        :type partStatus: :py:class:`str`
        :param startDate: Start Date for filtering Ports. (Example: '2014-03-30')
        :type startDate: :py:class:`str`
        :param endDate: End Date for filtering Ports. (Example: '2014-03-30')
        :type endDate: :py:class:`str`

        :returns: :py:class:`dict`
        """
        method = "getLNPList"

        if not isinstance(portid, str):
            raise ValueError("[Required] ID of the port previously created")

        parameters = {
            "portid": portid
        }

        if portStatus:
            if not isinstance(portStatus, str):
                raise ValueError("Status code to filtering Ports. Example: precessing. (You can use values returned by the method getLNPListStatus)")
            parameters["portStatus"] = portStatus

        if startDate:
            if not isinstance(startDate, str):
                raise ValueError("Start Date for filtering Ports. (Example: '2014-03-30')")
            parameters["startDate"] = startDate

        if endDate:
            if not isinstance(endDate, str):
                raise ValueError("End Date for filtering Ports. (Example: '2014-03-30')")
            parameters["endDate"] = endDate

        return self._voipms_client._get(method, parameters)

    def list_status(self):
        """
        Retrieve the list of possible status of a portability process.

        No Parameters

        :returns: :py:class:`dict`
        """
        method = "getLNPListStatus"

        parameters = {}

        return self._voipms_client._get(method, parameters)

    def notes(self, portid):
        """
        Retrieve the list of notes from the given portability process.

        :param portid: [Required] ID of the port previously created
        :type portid: :py:class:`str`

        :returns: :py:class:`dict`
        """
        method = "getLNPNotes"

        if not isinstance(portid, str):
            raise ValueError("ID for a specific backorder DID")

        parameters = {
            "portid": portid
        }

        return self._voipms_client._get(method, parameters)

    def status(self, portid):
        """
        Retrieve the current status of a given portability process.

        :param portid: [Required] ID of the port previously created
        :type portid: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "getLNPStatus"

        if not isinstance(portid, str):
            raise ValueError("[Required] ID of the port previously created")

        parameters = {
            "portid": portid
        }

        return self._voipms_client._get(method, parameters)
