# coding=utf-8
"""
The Voicemail API endpoint mark

Documentation: https://voip.ms/m/apidocs.php
"""
from voipms.baseapi import BaseApi


class VoicemailMark(BaseApi):
    """
    Mark for the Voicemail endpoint.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(VoicemailMark, self).__init__(*args, **kwargs)
        self.endpoint = 'voicemail'

    def listened_voicemail_message(self, mailbox, folder, message_num, listened):
        """
        Mark a Voicemail Message as Listened or Unlistened

        - If value is 'yes', the voicemail message will be marked as listened and will be moved to the Old Folder
        - If value is 'no', the voicemail message will be marked as not-listened and will be moved to the INBOX Folder

        :param mailbox: [Required] ID for a specific Mailbox (Example: 1001)
        :type mailbox: :py:class:`int`
        :param folder: [required] Name for specific Folder (Required if message id is passed, Example: 'INBOX', values from: voicemail.get_voicemail_folders)
        :type folder: :py:class:`str`
        :param message_num: [required] ID for specific Voicemail Message (Required if folder is passed, Example: 1)
        :type message_num: :py:class:`int`
        :param listened: [required] Code for mark voicemail as listened or not-listened (Values: 'yes'/'no')
        :type listened: :py:class:`str`

        :returns: :py:class:`dict`
        """
        method = "markListenedVoicemailMessage"

        if not isinstance(mailbox, int):
            raise ValueError("ID for a specific Mailbox needs to be an int (Example: 1001)")

        if not isinstance(folder, str):
            raise ValueError("Name for specific Folder needs to be a str (Required if message id is passed, Example: 'INBOX', values from: voicemail.get_voicemail_folders)")

        if not isinstance(message_num, int):
            raise ValueError("ID for specific Voicemail Message needs to be an int (Required if folder is passed, Example: 1)")

        if not isinstance(listened, str):
            raise ValueError("Code for mark voicemail as listened or not-listened needs to be a str (Values: 'yes'/'no')")
        elif listened not in ("yes", "no"):
            raise ValueError("Code for mark voicemail as listened or not-listened only allows values: 'yes'/'no'")

        parameters = {
            "mailbox": mailbox,
            "folder": folder,
            "message_num": message_num,
            "listened": listened,
        }

        return self._voipms_client._get(method, parameters)

    def urgent_voicemail_message(self, mailbox, folder, message_num, urgent):
        """
        Mark Voicemail Message as Urgent or not Urgent

        - If value is 'yes', the voicemail message will be marked as urgent and will be moved to the Urgent Folder
        - If value is 'no', the voicemail message will be unmarked as urgent and will be moved to the INBOX Folder

        :param mailbox: [Required] ID for a specific Mailbox (Example: 1001)
        :type mailbox: :py:class:`int`
        :param folder: [required] Name for specific Folder (Required if message id is passed, Example: 'INBOX', values from: voicemail.get_voicemail_folders)
        :type folder: :py:class:`str`
        :param message_num: [required] ID for specific Voicemail Message (Required if folder is passed, Example: 1)
        :type message_num: :py:class:`int`
        :param listened: [required] Code for mark voicemail as urgent or not-urgent (Values: 'yes'/'no')
        :type listened: :py:class:`str`

        :returns: :py:class:`dict`
        """
        method = "markUrgentVoicemailMessage"

        if not isinstance(mailbox, int):
            raise ValueError("ID for a specific Mailbox needs to be an int (Example: 1001)")

        if not isinstance(folder, str):
            raise ValueError("Name for specific Folder needs to be a str (Required if message id is passed, Example: 'INBOX', values from: voicemail.get_voicemail_folders)")

        if not isinstance(message_num, int):
            raise ValueError("ID for specific Voicemail Message needs to be an int (Required if folder is passed, Example: 1)")

        if not isinstance(urgent, str):
            raise ValueError("Code for mark voicemail as urgent or not-urgent needs to be a str (Values: 'yes'/'no')")
        elif urgent not in ("yes", "no"):
            raise ValueError("Code for mark voicemail as urgent or not-urgent only allows values: 'yes'/'no'")

        parameters = {
            "mailbox": mailbox,
            "folder": folder,
            "message_num": message_num,
            "urgent": urgent,
        }

        return self._voipms_client._get(method, parameters)
