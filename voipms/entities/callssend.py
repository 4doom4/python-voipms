# coding=utf-8
"""
The Calls API endpoint send

Documentation: https://voip.ms/m/apidocs.php
"""
from datetime import datetime

from voipms.baseapi import BaseApi
from voipms.helpers import validate_date, convert_bool


class CallsSend(BaseApi):
    """
    Send for the Calls endpoint.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(CallsSend, self).__init__(*args, **kwargs)
        self.endpoint = 'calls'

    def recording_email(self, client=None):
        """
        Send information and audio file to email account

        :param acount: [Required] Filter Call Recordings by Account (Values from getCallAccounts)
        :type acount: :py:class:`int`
        :param email: [Required] Email to send call recording
        :type email: :py:class:`str`
        :param callrecording: [Required] Call Recording (Values from getCallRecordings)
        :type callrecording: :py:class:`str`
        :returns: :py:class:`dict`
        """
        method = "sendCallRecordingEmail"

        if not isinstance(account, int):
            raise ValueError("[Required] Filter Call Recordings by Account (Values from getCallAccounts)")

        if not isinstance(email, str):
            raise ValueError("[Required] Email to send call recording")

        if not isinstance(callrecording, str):
            raise ValueError("[Required] Call Recording (Values from getCallRecordings)")

        parameters = {
            "account": account,
            "email": email,
            "callrecording": callrecording,
        }
        return self._voipms_client._get(method, parameters)
