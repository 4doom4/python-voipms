# coding=utf-8
"""
The Voicemail API endpoint move

Documentation: https://voip.ms/m/apidocs.php
"""
from voipms.baseapi import BaseApi


class VoicemailMove(BaseApi):
    """
    Move for the Voicemail endpoint.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(VoicemailMove, self).__init__(*args, **kwargs)
        self.endpoint = 'voicemail'

    def folder_voicemail_message(self, mailbox, folder, message_num, new_folder):
        """
        Move Voicemail Message to a Destination Folder

        :param mailbox: [Required] ID for a specific Mailbox (Example: 1001)
        :type mailbox: :py:class:`int`
        :param folder: [required] Name for specific Folder (Required if message id is passed, Example: 'INBOX', values from: voicemail.get_voicemail_folders)
        :type folder: :py:class:`str`
        :param message_num: [required] ID for specific Voicemail Message (Required if folder is passed, Example: 1)
        :type message_num: :py:class:`int`
        :param new_folder: [required] Destination Folder (Example: 'Urgent', values from: voicemail.get_voicemail_folders)
        :type new_folder: :py:class:`str`

        :returns: :py:class:`dict`
        """
        method = "moveFolderVoicemailMessage"

        if not isinstance(mailbox, int):
            raise ValueError("ID for a specific Mailbox needs to be an int (Example: 1001)")

        if not isinstance(folder, str):
            raise ValueError("Name for specific Folder needs to be a str (Required if message id is passed, Example: 'INBOX', values from: voicemail.get_voicemail_folders)")

        if not isinstance(message_num, int):
            raise ValueError("ID for specific Voicemail Message needs to be an int (Required if folder is passed, Example: 1)")

        if not isinstance(new_folder, str):
            raise ValueError("Destination Folder needs to be a str (Example: 'Urgent', values from: voicemail.get_voicemail_folders)")

        parameters = {
            "mailbox": mailbox,
            "folder": folder,
            "message_num": message_num,
            "new_folder": new_folder,
        }

        return self._voipms_client._get(method, parameters)
