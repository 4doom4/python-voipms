# coding=utf-8
"""
The Voicemail API endpoint get

Documentation: https://voip.ms/m/apidocs.php
"""
from voipms.baseapi import BaseApi
from voipms.helpers import validate_date


class VoicemailGet(BaseApi):
    """
    Get for the Voicemail endpoint.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(VoicemailGet, self).__init__(*args, **kwargs)
        self.endpoint = 'voicemail'

    def play_instructions(self, play_instructions=None):
        """
        Retrieves a list of Play Instructions modes if no additional parameter is provided

        - Retrieves a specific Play Instructions mode if a play code is provided

        :param play_instructions: Code for a specific Play Instructions setting (Example: 'u')
        :type play_instructions: :py:class:`str`

        :returns: :py:class:`dict`
        """
        method = "getPlayInstructions"

        parameters = {
        }

        if play_instructions:
            if not isinstance(play_instructions, str):
                raise ValueError("Code for a specific Play Instructions setting needs to be a str (Example: 'u')")
            else:
                parameters["play_instructions"] = play_instructions

        return self._voipms_client._get(method, parameters)

    def timezones(self, timezone=None):
        """
        Retrieves a list of Timezones if no additional parameter is provided

        - Retrieves a specific Timezone if a timezone code is provided

        :param timezone: Code for a specific Time Zone (Example: 'America/Buenos_Aires')
        :type timezone: :py:class:`str`

        :returns: :py:class:`dict`
        """
        method = "getTimezones"

        parameters = {
        }

        if timezone:
            if not isinstance(timezone, str):
                raise ValueError("Code for a specific Time Zone needs to be a str (Example: 'America/Buenos_Aires')")
            else:
                parameters["timezone"] = timezone

        return self._voipms_client._get(method, parameters)

    def voicemails(self, mailbox=None):
        """
        Retrieves a list of Voicemails if no additional parameter is provided

        - Retrieves a specific Voicemail if a voicemail code is provided

        :param mailbox: ID for specific Mailbox (Example: 1001)
        :type mailbox: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "getVoicemails"

        parameters = {
        }

        if mailbox:
            if not isinstance(mailbox, int):
                raise ValueError("ID for specific Mailbox needs to be an int (Example: 1001)")
            else:
                parameters["mailbox"] = mailbox

        return self._voipms_client._get(method, parameters)

    def voicemail_folders(self, folder=None):
        """
        Retrieves a list of your Voicemail Folders if no additional parameter is provided

        - Retrieves a specific Folder if a folder name is provided

        :param folder: Folder Name (Example: 'INBOX')
        :type folder: :py:class:`str`

        :returns: :py:class:`dict`
        """
        method = "getVoicemailFolders"

        parameters = {
        }

        if folder:
            if not isinstance(folder, str):
                raise ValueError("Folder Name needs to be a str (Example: 'INBOX')")
            else:
                parameters["folder"] = folder

        return self._voipms_client._get(method, parameters)

    def voicemail_message_file(self, mailbox, folder, message_num):
        """
        Retrieves a specific Voicemail Message File in Base64 format

        :param mailbox: [Required] ID for a specific Mailbox (Example: 1001)
        :type mailbox: :py:class:`int`
        :param folder: [required] Name for specific Folder (Required if message id is passed, Example: 'INBOX', values from: voicemail.voicemail_folders)
        :type folder: :py:class:`str`
        :param message_num: [required] ID for specific Voicemail Message (Required if folder is passed, Example: 1)
        :type message_num: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "getVoicemailMessageFile"

        if not isinstance(mailbox, int):
            raise ValueError("ID for a specific Mailbox needs to be an int (Example: 1001)")

        if not isinstance(folder, str):
            raise ValueError("Name for specific Folder needs to be a str (Required if message id is passed, Example: 'INBOX', values from: voicemail.voicemail_folders)")

        if not isinstance(message_num, int):
            raise ValueError("ID for specific Voicemail Message needs to be an int (Required if folder is passed, Example: 1)")

        parameters = {
            "mailbox": mailbox,
            "folder": folder,
            "message_num": message_num,
        }

        return self._voipms_client._get(method, parameters)

    def voicemail_messages(self, mailbox, **kwargs):
        """
        Retrieves a list of Voicemail Messages if mailbox parameter is provided

        - Retrieves a list of Voicemail Messages in a Folder if a folder is provided
        - Retrieves a list of Voicemail Messages in a date range if a from and to are provided

        :param mailbox: [Required] ID for a specific Mailbox (Example: 1001)
        :type mailbox: :py:class:`int`

        :param folder: Name for specific Folder (Required if message id is passed, Example: 'INBOX', values from: voicemail.voicemail_folders)
        :type folder: :py:class:`str`
        :param date_from: Start Date for Filtering Voicemail Messages (Example: '2016-01-30')
        :type date_from: :py:class:`str`
        :param date_to: End Date for Filtering Voicemail Messages (Example: '2016-01-30')
        :type date_to: :py:class:`str`

        :returns: :py:class:`dict`
        """
        method = "getVoicemailMessages"

        if not isinstance(mailbox, int):
            raise ValueError("ID for a specific Mailbox needs to be an int (Example: 1001)")

        parameters = {
            "mailbox": mailbox,
        }

        if "folder" in kwargs:
            if not isinstance(kwargs["folder"], str):
                raise ValueError("Name for specific Folder needs to be a str (Required if message id is passed, Example: 'INBOX', values from: voicemail.voicemail_folders)")
            parameters["folder"] = kwargs.pop("folder")

        if "date_from" in kwargs:
            if not isinstance(kwargs["date_from"], str):
                raise ValueError("Start Date for Filtering Voicemail Messages needs to be a str (Example: '2014-03-30')")
            validate_date(kwargs["date_from"])
            parameters["date_from"] = kwargs.pop("date_from")

        if "date_to" in kwargs:
            if not isinstance(kwargs["date_to"], str):
                raise ValueError("End Date for Filtering Voicemail Messages needs to be a str (Example: '2014-03-30')")
            validate_date(kwargs["date_to"])
            parameters["date_to"] = kwargs.pop("date_to")

        if len(kwargs) > 0:
            not_allowed_parameters = ""
            for key, value in kwargs.items():
                not_allowed_parameters += key + " "
            raise ValueError("Parameters not allowed: {}".format(not_allowed_parameters))

        return self._voipms_client._get(method, parameters)
