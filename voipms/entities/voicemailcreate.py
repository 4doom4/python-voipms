# coding=utf-8
"""
The Voicemail API endpoint create

Documentation: https://voip.ms/m/apidocs.php
"""
from voipms.baseapi import BaseApi
from voipms.helpers import validate_email, convert_bool


class VoicemailCreate(BaseApi):
    """
    Create for the Voicemail endpoint.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(VoicemailCreate, self).__init__(*args, **kwargs)
        self.endpoint = 'voicemail'

    def voicemail(self, digits, name, password, skip_password, attach_message, delete_message,
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
