# coding=utf-8
"""
The Voicemail API endpoint delete

Documentation: https://voip.ms/m/apidocs.php
"""
from voipms.baseapi import BaseApi


class VoicemailDelete(BaseApi):
    """
    Delete for the Voicemail endpoint.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(VoicemailDelete, self).__init__(*args, **kwargs)
        self.endpoint = 'voicemail'

    def messages(self, mailbox, **kwargs):
        """
        Deletes all messages in all servers from a specific Voicemail from your Account

        :param mailbox: [Required] ID for a specific Mailbox (Example: 1001)
        :type mailbox: :py:class:`int`

        :param folder: Name for specific Folder (Required if message id is passed, Example: 'INBOX', values from: voicemail.get_voicemail_folders)
        :type folder: :py:class:`str`
        :param message_num: ID for specific Voicemail Message (Required if folder is passed, Example: 1)
        :type message_num: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "delMessages"

        if not isinstance(mailbox, int):
            raise ValueError("ID for a specific Mailbox needs to be an int (Example: 1001)")

        parameters = {
            "mailbox": mailbox,
        }

        if "folder" in kwargs:
            if not isinstance(kwargs["folder"], str):
                raise ValueError("Name for specific Folder needs to be a str (Required if message id is passed, Example: 'INBOX', values from: voicemail.get_voicemail_folders)")
            parameters["folder"] = kwargs.pop("folder")

        if "message_num" in kwargs:
            if not isinstance(kwargs["message_num"], int):
                raise ValueError("ID for specific Voicemail Message needs to be an int (Required if folder is passed, Example: 1)")
            parameters["message_num"] = kwargs.pop("message_num")

        if len(kwargs) > 0:
            not_allowed_parameters = ""
            for key, value in kwargs.items():
                not_allowed_parameters += key + " "
            raise ValueError("Parameters not allowed: {}".format(not_allowed_parameters))

        return self._voipms_client._get(method, parameters)

    def voicemail(self, mailbox):
        """
        Deletes a specific Voicemail from your Account

        :param mailbox: [Required] ID for a specific Mailbox (Example: 1001)
        :type mailbox: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "delVoicemail"

        if not isinstance(mailbox, int):
            raise ValueError("ID for a specific Mailbox needs to be an int (Example: 1001)")

        parameters = {
            "mailbox": mailbox,
        }

        return self._voipms_client._get(method, parameters)
