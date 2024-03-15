# coding=utf-8
"""
The Calls API endpoint delete

Documentation: https://voip.ms/m/apidocs.php
"""
from datetime import datetime

from voipms.baseapi import BaseApi
from voipms.helpers import validate_date, convert_bool


class CallsDelete(BaseApi):
    """
    Delete for the Calls endpoint.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(CallsDelete, self).__init__(*args, **kwargs)
        self.endpoint = 'calls'

    def recording(self, account, callrecording):
        """
        Delete specific call recording, audio file and information related

        :param account: [Required] Filter Call Recordings by Account (Values from getCallAccounts)
        :type account: :py:class:`int`
        :param callrecording: [Required] Call Recording (Values from getCallRecordings)
        :type callrecording: :py:class:`str`
        :returns: :py:class:`dict`
        """
        method = "delCallRecording"

        if not isinstance(account, int):
            raise ValueError("[Required] Filter Call Recordings by Account (Values from getCallAccounts)")

        if not isinstance(callrecording, str):
            raise ValueError("[Required] Call Recording (Values from getCallRecordings)")

        parameters = {
            "account": account,
            "callrecording": callrecording,
        }
        return self._voipms_client._get(method, parameters)

    def parking(self, callparking):
        """
        Deletes a specific Call Parking entry from your Account

        :param callparking: ID for a specific Call Parking (Example: 323)
        :type callparking: :py:class:`int`
        :returns: :py:class:`dict`
        """
        method = "delCallParking"

        if not isinstance(callparking, int):
            raise ValueError("ID for a specific Call Parking (Example: 323)")

        parameters = {
            "callparking": callparking,
        }
        return self._voipms_client._get(method, parameters)
