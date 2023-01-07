# coding=utf-8
"""
The Dids API endpoint send

Documentation: https://voip.ms/m/apidocs.php
"""
from voipms.baseapi import BaseApi
import validators
from validators import ValidationFailure
import base64

def isBase64(s):
    try:
        return base64.b64encode(base64.b64decode(s)) == s
    except Exception:
        return False
    
def valid_url(url_string: str) -> bool:
    result = validators.url(url_string)

    if isinstance(result, ValidationFailure):
        return False

    return result

class DidsSend(BaseApi):
    """
    Send for the Dids endpoint.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(DidsSend, self).__init__(*args, **kwargs)
        self.endpoint = 'dids'

    def sms(self, did, dst, message):
        """
        Send a SMS message to a Destination Number

        :param did: [Required] DID Numbers which is sending the message (Example: 5551234567)
        :type did: :py:class:`int`
        :param dst: [Required] Destination Number (Example: 5551234568)
        :type dst: :py:class:`int`
        :param message: [Required] Message to be sent (Example: 'hello John Smith' max chars: 160)
        :type message: :py:class:`str`

        :returns: :py:class:`dict`
        """
        method = "sendSMS"

        if not isinstance(did, int):
            raise ValueError("DID Numbers which is sending the message needs to be an int (Example: 5551234567)")

        if not isinstance(dst, int):
            raise ValueError("Destination Number needs to be an int (Example: 5551234568) ")

        if not isinstance(message, str):
            raise ValueError("Message to be sent needs to be a str (Example: 'hello John Smith' max chars: 160)")
        else:
            if len(message) > 160:
                raise ValueError("Message to be sent can only have 160 chars")

        parameters = {
            "did": did,
            "dst": dst,
            "message": message,
        }

        return self._voipms_client._get(method, parameters)

    def mms(self, did, dst, message, media1=None, media2=None):
        """
        Send a MMS message to a Destination Number

        :param did: [Required] DID Numbers which is sending the message (Example: 5551234567)
        :type did: :py:class:`int`
        :param dst: [Required] Destination Number (Example: 5551234568)
        :type dst: :py:class:`int`
        :param message: [Required] Message to be sent (Example: 'hello John Smith' max chars: 1600)
        :type message: :py:class:`str`
        :param media1: [Optional]  Url to media file (Example: 'https://voip.ms/themes/voipms/assets/img/talent.jpg?v=2' 
        :type media1: :py:class:`str`
        :param media2: [Optional] Base 64 image encode (Example: data:image/png;base64,iVBORw0KGgoAAAANSUh...)
        :type media2: :py:class:`str`

        :returns: :py:class:`dict`
        """
        method = "sendMMS"

        if not isinstance(did, int):
            raise ValueError("DID Numbers which is sending the message needs to be an int (Example: 5551234567)")

        if not isinstance(dst, int):
            raise ValueError("Destination Number needs to be an int (Example: 5551234568) ")

        if not isinstance(message, str):
            raise ValueError("Message to be sent needs to be a str (Example: 'hello John Smith' max chars: 1600)")
            
        if media1:
            if not valid_url(media1):
                raise ValueError("Media1 to be sent needs to be a valid url to media file (Example: 'https://voip.ms/themes/voipms/assets/img/talent.jpg?v=2' ")
            
        if media2:
            if not isBase64(media2):
                raise ValueError("Media2 to be sent needs to be a base 64 image encode (Example: data:image/png;base64,iVBORw0KGgoAAAANSUh...)")
        else:
            if len(message) > 1600:
                raise ValueError("Message to be sent can only have 1600 chars")

        if media1:
            parameters = {
                "did": did,
                "dst": dst,
                "message": message,
                "media1":  media1,
            }
        elif media2:
            parameters = {
                "did": did,
                "dst": dst,
                "message": message,
                "media2": media2,
            }
        else:
            parameters = {
                "did": did,
                "dst": dst,
                "message": message,
            }

        return self._voipms_client._get(method, parameters)
