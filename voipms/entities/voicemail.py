from voipms.baseapi import BaseApi
from voipms.helpers import convert_bool, validate_date, validate_email


class Voicemail(BaseApi):
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(Voicemail, self).__init__(*args, **kwargs)
        self.endoint = 'voicemail'

    def create_voicemail(self, digits, name, password, skip_password, attach_message, delete_message,
                         say_time, timezone, say_callerid, play_instructions, language, **kwargs):
        """
        Adds a new Voicemail entry to your Account

        :param digits: [Required] Digits used to create the voicemail (Example: 01) Minimum 1 digit, maximum 10 digits
        :type digits: :py:class:`int`
        :param name: [Required] Name for the Mailbox
        :type name: :py:class:`str`
        :param password: [Required] Password for the Mailbox
        :type password: :py:class:`int`
        :param skip_password: [Required] True if Skipping Password (True/False)
        :type skip_password: :py:class:`bool`
        :param attach_message: [Required] Yes for Attaching WAV files to Message (Values: 'yes'/'no')
        :type attach_message: :py:class:`str`
        :param delete_message: [Required] Yes for Deleting Messages (Values: 'yes'/'no')
        :type delete_message: :py:class:`str`
        :param say_time: [Required] Yes for Saying Time Stamp (Values: 'yes'/'no')
        :type say_time: :py:class:`str`
        :param timezone: [Required] Time Zone for Mailbox (Values from voicemail.get_time_zones)
        :type timezone: :py:class:`str`
        :param say_callerid: [Required] Yes for Saying the Caller ID (Values: 'yes'/'no')
        :type say_callerid: :py:class:`str`
        :param play_instructions: [Required] Code for Play Instructions Setting (Values from voicemail.get_play_instructions)
        :type play_instructions: :py:class:`str`
        :param language: [Required] Code for Language (Values from general.get_languages)
        :type language: :py:class:`str`

        :param email: Client's e-mail address for receiving Messages
        :type email: :py:class:`str`
        :param email_attachment_format: Code for Email Attachment format (Values from voicemail.get_voicemail_attachment_formats)
        :type email_attachment_format: :py:class:`str`
        :param unavailable_message_recording: Recording for the Unavailable Message (values from dids.get_recordings)
        :type unavailable_message_recording: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "createVoicemail"

        if not isinstance(digits, int):
            raise ValueError("Digits used to create the voicemail needs to be an int (Example: 01) Minimum 1 digit, maximum 10 digits")
        elif len(str(digits)) > 10:
            raise ValueError("Digits used to create the voicemail can only have a maximum of 10 digits")

        if not isinstance(name, str):
            raise ValueError("Name for the Mailbox needs to be a str")

        if not isinstance(password, int):
            raise ValueError("Password for the Mailbox needs to be an int")

        if not isinstance(skip_password, bool):
            raise ValueError("True if Skipping Password needs to be a bool (True/False)")

        if not isinstance(attach_message, str):
            raise ValueError("Yes for Attaching WAV files to Message needs to be a str (Values: 'yes'/'no')")
        elif attach_message not in ("yes", "no"):
            raise ValueError("Attaching WAV files to Message only allows values: 'yes'/'no'")

        if not isinstance(delete_message, str):
            raise ValueError("Yes for Deleting Messages needs to be a str (Values: 'yes'/'no')")
        elif delete_message not in ("yes", "no"):
            raise ValueError("Deleting Messages only allows values: 'yes'/'no'")

        if not isinstance(say_time, str):
            raise ValueError("Yes for Saying Time Stamp needs to be a str (Values: 'yes'/'no')")
        elif say_time not in ("yes", "no"):
            raise ValueError("Saying Time Stamp only allows values: 'yes'/'no'")

        if not isinstance(timezone, str):
            raise ValueError("Time Zone for Mailbox needs to be a str (Values from voicemail.get_time_zones)")

        if not isinstance(say_callerid, str):
            raise ValueError("Yes for Saying the Caller ID needs to be a str (Values: 'yes'/'no')")
        elif say_callerid not in ("yes", "no"):
            raise ValueError("Saying the Caller ID only allows values: 'yes'/'no'")

        if not isinstance(play_instructions, str):
            raise ValueError("Code for Play Instructions Setting needs to be a str (Values from voicemail.get_play_instructions)")

        if not isinstance(language, str):
            raise ValueError("Code for Language needs to be a str (Values from general.get_languages)")

        parameters = {
            "digits": digits,
            "name": name,
            "password": password,
            "skip_password": convert_bool(skip_password),
            "attach_message": attach_message,
            "attach_message": attach_message,
            "delete_message": delete_message,
            "say_time": say_time,
            "timezone": timezone,
            "say_callerid": say_callerid,
            "play_instructions": play_instructions,
            "language": language,
        }

        if "email" in kwargs:
            email = kwargs.pop("email")
            if not isinstance(email, str):
                raise ValueError("Client's e-mail address for receiving Messages needs to be a str")
            elif not validate_email(email):
                raise ValueError("Client's e-mail address is not a correct email syntax")
            parameters["email"] = email

        if "email_attachment_format" in kwargs:
            if not isinstance(kwargs["email_attachment_format"], str):
                raise ValueError("Code for Email Attachment format needs to be a str (Values from voicemail.get_voicemail_attachment_formats)")
            parameters["email_attachment_format"] = kwargs.pop("email_attachment_format")

        if "unavailable_message_recording" in kwargs:
            if not isinstance(kwargs["unavailable_message_recording"], int):
                raise ValueError("Recording for the Unavailable Message needs to be an int (values from dids.get_recordings)")
            parameters["unavailable_message_recording"] = kwargs.pop("unavailable_message_recording")

        if len(kwargs) > 0:
            not_allowed_parameters = ""
            for key, value in kwargs.items():
                not_allowed_parameters += key + " "
            raise ValueError("Parameters not allowed: {}".format(not_allowed_parameters))

        return self._voipms_client._get(method, parameters)

    def del_messages(self, mailbox, **kwargs):
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

    def del_voicemail(self, mailbox):
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

    def get_play_instructions(self, play_instructions=None):
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

    def get_timezones(self, timezone=None):
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

    def get_voicemails(self, mailbox=None):
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

    def get_voicemail_folders(self, folder=None):
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

    def get_voicemail_message_file(self, mailbox, folder, message_num):
        """
        Retrieves a specific Voicemail Message File in Base64 format

        :param mailbox: [Required] ID for a specific Mailbox (Example: 1001)
        :type mailbox: :py:class:`int`
        :param folder: [required] Name for specific Folder (Required if message id is passed, Example: 'INBOX', values from: voicemail.get_voicemail_folders)
        :type folder: :py:class:`str`
        :param message_num: [required] ID for specific Voicemail Message (Required if folder is passed, Example: 1)
        :type message_num: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "getVoicemailMessageFile"

        if not isinstance(mailbox, int):
            raise ValueError("ID for a specific Mailbox needs to be an int (Example: 1001)")

        if not isinstance(folder, str):
            raise ValueError("Name for specific Folder needs to be a str (Required if message id is passed, Example: 'INBOX', values from: voicemail.get_voicemail_folders)")

        if not isinstance(message_num, int):
            raise ValueError("ID for specific Voicemail Message needs to be an int (Required if folder is passed, Example: 1)")

        parameters = {
            "mailbox": mailbox,
            "folder": folder,
            "message_num": message_num,
        }

        return self._voipms_client._get(method, parameters)

    def get_voicemail_messages(self, mailbox, **kwargs):
        """
        Retrieves a list of Voicemail Messages if mailbox parameter is provided

        - Retrieves a list of Voicemail Messages in a Folder if a folder is provided
        - Retrieves a list of Voicemail Messages in a date range if a from and to are provided

        :param mailbox: [Required] ID for a specific Mailbox (Example: 1001)
        :type mailbox: :py:class:`int`

        :param folder: Name for specific Folder (Required if message id is passed, Example: 'INBOX', values from: voicemail.get_voicemail_folders)
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
                raise ValueError("Name for specific Folder needs to be a str (Required if message id is passed, Example: 'INBOX', values from: voicemail.get_voicemail_folders)")
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

    def mark_listened_voicemail_message(self, mailbox, folder, message_num, listened):
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

    def mark_urgent_voicemail_message(self, mailbox, folder, message_num, urgent):
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

    def move_folder_voicemail_message(self, mailbox, folder, message_num, new_folder):
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

    def send_voicemail_email(self, mailbox, folder, message_num, email_address):
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

    def set_voicemail(self, mailbox, name, password, skip_password, attach_message, delete_message,
                      say_time, timezone, say_callerid, play_instructions, language, **kwargs):
        """
        Updates the information from a specific Voicemail

        :param mailbox: [Required] ID for a specific Mailbox (Example: 1001)
        :type mailbox: :py:class:`int`
        :param name: [Required] Name for the Mailbox
        :type name: :py:class:`str`
        :param password: [Required] Password for the Mailbox
        :type password: :py:class:`int`
        :param skip_password: [Required] True if Skipping Password (True/False)
        :type skip_password: :py:class:`bool`
        :param attach_message: [Required] Yes for Attaching WAV files to Message (Values: 'yes'/'no')
        :type attach_message: :py:class:`str`
        :param delete_message: [Required] Yes for Deleting Messages (Values: 'yes'/'no')
        :type delete_message: :py:class:`str`
        :param say_time: [Required] Yes for Saying Time Stamp (Values: 'yes'/'no')
        :type say_time: :py:class:`str`
        :param timezone: [Required] Time Zone for Mailbox (Values from voicemail.get_time_zones)
        :type timezone: :py:class:`str`
        :param say_callerid: [Required] Yes for Saying the Caller ID (Values: 'yes'/'no')
        :type say_callerid: :py:class:`str`
        :param play_instructions: [Required] Code for Play Instructions Setting (Values from voicemail.get_play_instructions)
        :type play_instructions: :py:class:`str`
        :param language: [Required] Code for Language (Values from general.get_languages)
        :type language: :py:class:`str`

        :param email: Client's e-mail address for receiving Messages
        :type email: :py:class:`str`
        :param email_attachment_format: Code for Email Attachment format (Values from voicemail.get_voicemail_attachment_formats)
        :type email_attachment_format: :py:class:`str`
        :param unavailable_message_recording: Recording for the Unavailable Message (values from dids.get_recordings)
        :type unavailable_message_recording: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "setVoicemail"

        if not isinstance(mailbox, int):
            raise ValueError("ID for a specific Mailbox needs to be an int (Example: 1001)")

        if not isinstance(name, str):
            raise ValueError("Name for the Mailbox needs to be a str")

        if not isinstance(password, int):
            raise ValueError("Password for the Mailbox needs to be an int")

        if not isinstance(skip_password, bool):
            raise ValueError("True if Skipping Password needs to be a bool (True/False)")

        if not isinstance(attach_message, str):
            raise ValueError("Yes for Attaching WAV files to Message needs to be a str (Values: 'yes'/'no')")
        elif attach_message not in ("yes", "no"):
            raise ValueError("Attaching WAV files to Message only allows values: 'yes'/'no'")

        if not isinstance(delete_message, str):
            raise ValueError("Yes for Deleting Messages needs to be a str (Values: 'yes'/'no')")
        elif delete_message not in ("yes", "no"):
            raise ValueError("Deleting Messages only allows values: 'yes'/'no'")

        if not isinstance(say_time, str):
            raise ValueError("Yes for Saying Time Stamp needs to be a str (Values: 'yes'/'no')")
        elif say_time not in ("yes", "no"):
            raise ValueError("Saying Time Stamp only allows values: 'yes'/'no'")

        if not isinstance(timezone, str):
            raise ValueError("Time Zone for Mailbox needs to be a str (Values from voicemail.get_time_zones)")

        if not isinstance(say_callerid, str):
            raise ValueError("Yes for Saying the Caller ID needs to be a str (Values: 'yes'/'no')")
        elif say_callerid not in ("yes", "no"):
            raise ValueError("Saying the Caller ID only allows values: 'yes'/'no'")

        if not isinstance(play_instructions, str):
            raise ValueError("Code for Play Instructions Setting needs to be a str (Values from voicemail.get_play_instructions)")

        if not isinstance(language, str):
            raise ValueError("Code for Language needs to be a str (Values from general.get_languages)")

        parameters = {
            "mailbox": mailbox,
            "name": name,
            "password": password,
            "skip_password": convert_bool(skip_password),
            "attach_message": attach_message,
            "attach_message": attach_message,
            "delete_message": delete_message,
            "say_time": say_time,
            "timezone": timezone,
            "say_callerid": say_callerid,
            "play_instructions": play_instructions,
            "language": language,
        }

        if "email" in kwargs:
            email = kwargs.pop("email")
            if not isinstance(email, str):
                raise ValueError("Client's e-mail address for receiving Messages needs to be a str")
            elif not validate_email(email):
                raise ValueError("Client's e-mail address is not a correct email syntax")
            parameters["email"] = email

        if "email_attachment_format" in kwargs:
            if not isinstance(kwargs["email_attachment_format"], str):
                raise ValueError("Code for Email Attachment format needs to be a str (Values from voicemail.get_voicemail_attachment_formats)")
            parameters["email_attachment_format"] = kwargs.pop("email_attachment_format")

        if "unavailable_message_recording" in kwargs:
            if not isinstance(kwargs["unavailable_message_recording"], int):
                raise ValueError("Recording for the Unavailable Message needs to be an int (values from dids.get_recordings)")
            parameters["unavailable_message_recording"] = kwargs.pop("unavailable_message_recording")

        if len(kwargs) > 0:
            not_allowed_parameters = ""
            for key, value in kwargs.items():
                not_allowed_parameters += key + " "
            raise ValueError("Parameters not allowed: {}".format(not_allowed_parameters))

        return self._voipms_client._get(method, parameters)
