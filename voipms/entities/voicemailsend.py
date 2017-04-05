# coding=utf-8
"""
The Voicemail API endpoint send

Documentation: https://voip.ms/m/apidocs.php
"""
from voipms.baseapi import BaseApi
from voipms.helpers import validate_email


class VoicemailSend(BaseApi):
    """
    Send for the Voicemail endpoint.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(VoicemailSend, self).__init__(*args, **kwargs)
        self.endpoint = 'voicemail'

    def voicemail_email(self, mailbox, folder, message_num, email_address):
        """
        Move Voicemail Message to a Destination Folder

        :param mailbox: [Required] ID for a specific Mailbox (Example: 1001)
        :type mailbox: :py:class:`int`
        :param folder: [required] Name for specific Folder (Required if message id is passed, Example: 'INBOX', values from: voicemail.get_voicemail_folders)
        :type folder: :py:class:`str`
        :param message_num: [required] ID for specific Voicemail Message (Required if folder is passed, Example: 1)
        :type message_num: :py:class:`int`
        :param email_address: [required] Destination Email address (Example: john.doe@my-domain.com)
        :type email_address: :py:class:`str`

        :returns: :py:class:`dict`
        """
        method = "sendVoicemailEmail"

        if not isinstance(mailbox, int):
            raise ValueError("ID for a specific Mailbox needs to be an int (Example: 1001)")

        if not isinstance(folder, str):
            raise ValueError("Name for specific Folder needs to be a str (Required if message id is passed, Example: 'INBOX', values from: voicemail.get_voicemail_folders)")

        if not isinstance(message_num, int):
            raise ValueError("ID for specific Voicemail Message needs to be an int (Required if folder is passed, Example: 1)")

        if not isinstance(email_address, str):
            raise ValueError("Destination Email address needs to be a str (Example: john.doe@my-domain.com)")
        elif not validate_email(email_address):
                raise ValueError("Destination Email address is not a correct email syntax")

        parameters = {
            "mailbox": mailbox,
            "folder": folder,
            "message_num": message_num,
            "email_address": email_address,
        }

        return self._voipms_client._get(method, parameters)
