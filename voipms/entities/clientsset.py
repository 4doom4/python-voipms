# coding=utf-8
"""
The Clients API endpoint set

Documentation: https://voip.ms/m/apidocs.php
"""
from voipms.baseapi import BaseApi
from voipms.helpers import validate_email


class ClientsSet(BaseApi):
    """
    Set for the Clients endpoint.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(ClientsSet, self).__init__(*args, **kwargs)
        self.endpoint = 'clients'

    def client(self, client, email, password, firstname,
               lastname, phone_number, **kwargs):
        """
        Updates Reseller Client information

        :param client: [Required] ID for a specific Reseller Client (Example: 561115)
        :type client: :py:class:`int`
        :param email: [Required] Client's e-mail
        :type email: :py:class:`str`
        :param password: [Required] Client's Password
        :type password: :py:class:`str`
        :param firstname: [Required] Client's Firstname
        :type firstname: :py:class:`str`
        :param lastname: [Required] Client's Lastname
        :type lastname: :py:class:`str`
        :param phone_number: [Required] Client's Phone Number
        :type phone_number: :py:class:`str`
        :param **kwargs: All optional parameters
        :type **kwargs: :py:class:`dict`

        :param company: Client's Company
        :type company: :py:class:`str`
        :param address: Client's Address
        :type address: :py:class:`str`
        :param city: Client's City
        :type city: :py:class:`str`
        :param state: Client's State
        :type state: :py:class:`str`
        :param country: Client's Country (Values from general.get_countries)
        :type country: :py:class:`str`
        :param zip_code: Client's Zip Code
        :type zip_code: :py:class:`str`
        :param balance_management: Balance Management for Client (Values from clients.get_balance_management)
        :type balance_management: :py:class:`str`

        :returns: :py:class:`dict`
        """
        method = "setClient"

        if not isinstance(client, int):
            raise ValueError("ID for a specific Reseller Client needs to be in int (Example: 561115)")

        if not isinstance(email, str):
            raise ValueError("Client's e-mail needs to be a str")
        else:
            if not validate_email(email):
                raise ValueError("Client's e-mail is not a correct email syntax")

        if not isinstance(password, str):
            raise ValueError("Client's Password needs to be a str")

        if not isinstance(firstname, str):
            raise ValueError("Client's Firstname needs to be a str")

        if not isinstance(lastname, str):
            raise ValueError("Client's Lastname needs to be a str")

        if not isinstance(phone_number, str):
            raise ValueError("Client's Phone Number needs to be a str")

        parameters = {
            "client": client,
            "email": email,
            "password": password,
            "firstname": firstname,
            "lastname": lastname,
            "phone_number": phone_number,
        }

        if "company" in kwargs:
            if not isinstance(kwargs["company"], str):
                raise ValueError("Client's Company needs to be a str")
            parameters["company"] = kwargs.pop("company")

        if "address" in kwargs:
            if not isinstance(kwargs["address"], str):
                raise ValueError("Client's Address needs to be a str")
            parameters["address"] = kwargs.pop("address")

        if "city" in kwargs:
            if not isinstance(kwargs["city"], str):
                raise ValueError("Client's City needs to be a str")
            parameters["city"] = kwargs.pop("city")

        if "state" in kwargs:
            if not isinstance(kwargs["state"], str):
                raise ValueError("Client's State needs to be a str")
            parameters["state"] = kwargs.pop("state")

        if "country" in kwargs:
            if not isinstance(kwargs["country"], str):
                raise ValueError("Client's Country needs to be a str (Values from general.get_countries)")
            parameters["country"] = kwargs.pop("country")

        if "zip_code" in kwargs:
            if not isinstance(kwargs["zip_code"], str):
                raise ValueError("Client's Zip Code needs to be a str")
            parameters["zip"] = kwargs.pop("zip_code")

        if "balance_management" in kwargs:
            if not isinstance(kwargs["balance_management"], str):
                raise ValueError("Balance Management for Client (Values from clients.get_balance_management)")
            parameters["balance_management"] = kwargs.pop("balance_management")

        if len(kwargs) > 0:
            not_allowed_parameters = ""
            for key, value in kwargs.items():
                not_allowed_parameters += key + " "
            raise ValueError("Parameters not allowed: {}".format(not_allowed_parameters))

        return self._voipms_client._get(method, parameters)

    def client_threshold(self, client, threshold, email=None):
        """
        Update the Threshold Amount for a specific Reseller Client

        - Update the Threshold notification e-mail for a specific Reseller Client if the e-mail address is provided

        :param client: [Required] ID for a specific Reseller Client (Example: 561115)
        :type client: :py:class:`int`
        :param threshold: [Required] Threshold amount between 1 and 250 (Example: 10)
        :type threshold: :py:class:`int`
        :param email: Client's e-mail for balance threshold notification
        :type email: :py:class:`str`
        :returns: :py:class:`dict`
        """
        method = "setClientThreshold"

        if not isinstance(client, int):
            raise ValueError("ID for a specific Reseller Client needs to be an int (Example: 561115)")

        if not isinstance(threshold, int):
            raise ValueError("Threshold amount between 1 and 250 needs to be an int (Example: 10)")
        else:
            if not 1 <= threshold <= 250:
                raise ValueError("Threshold amount needs to be between 1 and 250")

        parameters = {
            "client": client,
            "threshold": threshold,
        }

        if email:
            if not isinstance(email, str):
                raise ValueError("Client's e-mail for balance threshold notification needs to be a str")
            else:
                if not validate_email(email):
                    raise ValueError("Client's e-mail is not a correct email syntax")
                else:
                    parameters["email"] = email

        return self._voipms_client._get(method, parameters)

    def conference(self, conference, name, description, max_members, **kwargs):
        """
        Updates a specific Conference if a conference code is provided

        - Adds a new Conference entry if no conference code is provided

        :param conference: [Required] ID for a specific Conference (Example: 5356)
        :type conference: :py:class:`int`
        :param name: [Required] Conference name
        :type name: :py:class:`str`
        :param description: [Required] Conference description
        :type description: :py:class:`str`
        :param members: Conference Members
        :type members: :py:class:`int`
        :param max_members: [Required] Members Max Value
        :type max_members: :py:class:`int`
        :param sound_join: The recording played when a user joins, typically some kind of beep sound (Values from getRecordings)
        :type sound_join: :py:class:`int`
        :param sound_leave: The recording played when a user leaves, typically some kind of beep sound (Values from getRecordings)
        :type sound_leave: :py:class:`int`
        :param sound_has_joined: The recording played as a user intro (Values from getRecordings)
        :type sound_has_joined: :py:class:`int`
        :param sound_has_left: The recording played as a user leaves the conference (Values from getRecordings)
        :type sound_has_left: :py:class:`int`
        :param sound_kicked: The recording played to a user who has been kicked from the conference (Values from getRecordings)
        :type sound_kicked: :py:class:`int`
        :param sound_muted: The recording played to a user when the mute option is toggled on (Values from getRecordings)
        :type sound_muted: :py:class:`int`
        :param sound_unmuted: The recording played to a user when the mute option is toggled off (Values from getRecordings)
        :type sound_unmuted: :py:class:`int`
        :param sound_only_person: The recording played when a user is the only person in the conference (Values from getRecordings)
        :type sound_only_person: :py:class:`int`
        :param sound_only_one: The recording played to a user when there is only one other person in the conference. (Values from getRecordings)
        :type sound_only_one: :py:class:`int`
        :param sound_there_are: The recording played when announcing how many users there are in a conference. (Values from getRecordings)
        :type sound_there_are: :py:class:`int`
        :param sound_other_in_party: The recording used in conjunction with the There are option, used like There are (number of participants) Other in party (Values from getRecordings)
        :type sound_other_in_party: :py:class:`int`
        :param sound_place_into_conference: The recording played when a user is placed into a conference that cannot start until a marked user enters (Values from getRecordings)
        :type sound_place_into_conference: :py:class:`int`
        :param sound_get_pin: The recording played when prompting for a conference PIN (Values from getRecordings)
        :type sound_get_pin: :py:class:`int`
        :param sound_invalid_pin: The recording played when an invalid PIN is entered too many (3) times (Values from getRecordings)
        :type sound_invalid_pin: :py:class:`int`
        :param sound_locked: The recording played to a user trying to join a locked conference (Values from getRecordings)
        :type sound_locked: :py:class:`int`
        :param sound_locked_now: The recording played to an Admin-level user after toggling the conference to locked mode (Values from getRecordings)
        :type sound_locked_now: :py:class:`int`
        :param sound_unlocked_now: The recording played to an Admin-level user after toggling the conference to unlocked mode (Values from getRecordings)
        :type sound_unlocked_now: :py:class:`int`
        :param sound_error_menu: The recording played when there is an error on the menu. (Values from getRecordings)
        :type sound_error_menu: :py:class:`int`
        :param sound_participants_muted: The recording played when all non-admin participants are muted. (Values from getRecordings)
        :type sound_participants_muted: :py:class:`int`
        :param sound_participants_unmuted: The recording played when all non-admin participants are unmuted. (Values from getRecordings)
        :type sound_participants_unmuted: :py:class:`int`
        :param language: Conference Language (Values from getLanguages)
        :type language: :py:class:`str`
        :returns: :py:class:`dict`
        """
        method = "setConference"

        parameters = {}

        if not isinstance(conference, int):
            raise ValueError("[Required] ID for a specific Conference (Example: 5356)")
        parameters["conference"] = conference

        if not isinstance(name, str):
            raise ValueError("[Required] Conference name")
        parameters["name"] = name

        if not isinstance(description, str):
            raise ValueError("[Required] Conference description")
        parameters["description"] = description

        if not isinstance(max_members, int):
            raise ValueError("[Required] Members Max Value")
        parameters["max_members"] = max_members

        if "members" in kwargs:
            if not isinstance(kwargs["members"], int):
                raise ValueError("Conference Members")
            parameters["members"] = kwargs.pop("members")

        if "sound_join" in kwargs:
            if not isinstance(kwargs["sound_join"], int):
                raise ValueError("The recording played when a user joins, typically some kind of beep sound (Values from getRecordings)")
            parameters["sound_join"] = kwargs.pop("sound_join")

        if "sound_leave" in kwargs:
            if not isinstance(kwargs["sound_leave"], int):
                raise ValueError("The recording played when a user leaves, typically some kind of beep sound (Values from getRecordings)")
            parameters["sound_leave"] = kwargs.pop("sound_leave")

        if "sound_has_joined" in kwargs:
            if not isinstance(kwargs["sound_has_joined"], int):
                raise ValueError("The recording played as a user intro (Values from getRecordings)")
            parameters["sound_has_joined"] = kwargs.pop("sound_has_joined")

        if "sound_has_left" in kwargs:
            if not isinstance(kwargs["sound_has_left"], int):
                raise ValueError("The recording played as a user leaves the conference (Values from getRecordings)")
            parameters["sound_has_left"] = kwargs.pop("sound_has_left")

        if "sound_kicked" in kwargs:
            if not isinstance(kwargs["sound_kicked"], int):
                raise ValueError("The recording played to a user who has been kicked from the conference (Values from getRecordings)")
            parameters["sound_kicked"] = kwargs.pop("sound_kicked")

        if "sound_muted" in kwargs:
            if not isinstance(kwargs["sound_muted"], int):
                raise ValueError("The recording played to a user when the mute option is toggled on (Values from getRecordings)")
            parameters["sound_muted"] = kwargs.pop("sound_muted")

        if "sound_unmuted" in kwargs:
            if not isinstance(kwargs["sound_unmuted"], int):
                raise ValueError("The recording played to a user when the mute option is toggled off (Values from getRecordings)")
            parameters["sound_unmuted"] = kwargs.pop("sound_unmuted")
        
        if "sound_only_person" in kwargs:
            if not isinstance(kwargs["sound_only_person"], int):
                raise ValueError("The recording played when a user is the only person in the conference (Values from getRecordings)")
            parameters["sound_only_person"] = kwargs.pop("sound_only_person")

        if "sound_only_one" in kwargs:
            if not isinstance(kwargs["sound_only_one"], int):
                raise ValueError("The recording played to a user when there is only one other person in the conference. (Values from getRecordings)")
            parameters["sound_only_one"] = kwargs.pop("sound_only_one")

        if "sound_there_are" in kwargs:
            if not isinstance(kwargs["sound_there_are"], int):
                raise ValueError("The recording played when announcing how many users there are in a conference. (Values from getRecordings)")
            parameters["sound_there_are"] = kwargs.pop("sound_there_are")

        if "sound_other_in_party" in kwargs:
            if not isinstance(kwargs["sound_other_in_party"], int):
                raise ValueError("The recording used in conjunction with the There are option, used like There are (number of participants) Other in party (Values from getRecordings)")
            parameters["sound_other_in_party"] = kwargs.pop("sound_other_in_party")

        if "sound_place_into_conference" in kwargs:
            if not isinstance(kwargs["sound_place_into_conference"], int):
                raise ValueError("The recording played when a user is placed into a conference that cannot start until a marked user enters (Values from getRecordings)")
            parameters["sound_place_into_conference"] = kwargs.pop("sound_place_into_conference")

        if "sound_get_pin" in kwargs:
            if not isinstance(kwargs["sound_get_pin"], int):
                raise ValueError("The recording played when prompting for a conference PIN (Values from getRecordings)")
            parameters["sound_get_pin"] = kwargs.pop("sound_get_pin")

        if "sound_invalid_pin" in kwargs:
            if not isinstance(kwargs["sound_invalid_pin"], int):
                raise ValueError("The recording played when an invalid PIN is entered too many (3) times (Values from getRecordings)")
            parameters["sound_invalid_pin"] = kwargs.pop("sound_invalid_pin")

        if "sound_locked" in kwargs:
            if not isinstance(kwargs["sound_locked"], int):
                raise ValueError("The recording played to a user trying to join a locked conference (Values from getRecordings)")
            parameters["sound_locked"] = kwargs.pop("sound_locked")

        if "sound_locked_now" in kwargs:
            if not isinstance(kwargs["sound_locked_now"], int):
                raise ValueError("The recording played to an Admin-level user after toggling the conference to locked mode (Values from getRecordings)")
            parameters["sound_locked_now"] = kwargs.pop("sound_locked_now")

        if "sound_unlocked_now" in kwargs:
            if not isinstance(kwargs["sound_unlocked_now"], int):
                raise ValueError("The recording played to an Admin-level user after toggling the conference to unlocked mode (Values from getRecordings)")
            parameters["sound_unlocked_now"] = kwargs.pop("sound_unlocked_now")

        if "sound_error_menu" in kwargs:
            if not isinstance(kwargs["sound_error_menu"], int):
                raise ValueError("The recording played when there is an error on the menu. (Values from getRecordings)")
            parameters["sound_error_menu"] = kwargs.pop("sound_error_menu")

        if "sound_participants_muted" in kwargs:
            if not isinstance(kwargs["sound_participants_muted"], int):
                raise ValueError("The recording played when all non-admin participants are muted. (Values from getRecordings)")
            parameters["sound_participants_muted"] = kwargs.pop("sound_participants_muted")

        if "sound_participants_unmuted" in kwargs:
            if not isinstance(kwargs["sound_participants_unmuted"], int):
                raise ValueError("The recording played when all non-admin participants are unmuted. (Values from getRecordings)")
            parameters["sound_participants_unmuted"] = kwargs.pop("sound_participants_unmuted")

        if "language" in kwargs:
            if not isinstance(kwargs["language"], str):
                raise ValueError("Conference Language (Values from getLanguages)")
            parameters["language"] = kwargs.pop("language")

        return self._voipms_client._get(method, parameters)

    def conference_member(self, conference, member, name, description, **kwargs):
        """
        Updates a specific Conference if a conference code is provided

        - Adds a new Conference entry if no conference code is provided

        :param conference: [Required] ID for a specific Conference (Example: 5356)
        :type conference: :py:class:`int`
        :param member: [Required] ID for a specific Member profile (Example: 5356)
        :type member: :py:class:`int`
        :param name: [Required] Member name
        :type name: :py:class:`str`
        :param description: [Required] Member description
        :type description: :py:class:`str`
        :param pin: Assigned PIN
        :type pin: :py:class:`int`
        :param announce_join_leave: Sets if the conference recording when a member joins or leaves will be played (yes/no)
        :type client: :py:class:`str`
        :param admin: Sets if the member is an admin or not (yes/no).
        :type admin: :py:class:`str`
        :param start_muted: Sets if the member should start out muted after entering the conference (yes/no).
        :type start_muted: :py:class:`str`
        :param announce_user_count: Sets if the number of members in the conference should be announced to the caller as he joins (yes/no).
        :type announce_user_count: :py:class:`str`
        :param announce_only_user: Sets if the "only user" announcement should be played when a caller enters an empty conference (yes/no).
        :type announce_only_user: :py:class:`str`
        :param moh_when_empty: Sets whether music on hold (MOH) should be played when only one person is in the conference (Values from getMusicOnHold).
        :type moh_when_empty: :py:class:`str`
        :param quiet: When set to "yes", enter/leave prompts and user introductions are not played (yes/no).
        :type quite: :py:class:`str`
        :param announcement: If set, this recording will be heard only by the user as he joins the conference (Values from getRecordings).
        :type announce: :py:class:`int`
        :param drop_silence: The system will drop what is detected as silence from entering into the conference (yes/no).
        :type drop_silence: :py:class:`str`
        :param talking_threshold: The time, in milliseconds, that a users needs to be sending sound or voice before the system can consider them to be talking (allowed values are 100, 120, 140, 160, 180, 200, 220, 240 or 250).
        :type talking_threshold: :py:class:`int`
        :param silence_threshold: The time, in milliseconds, that silence needs to be present in the user’s sound stream before the system can consider it to be in fact silent and close the audio (allowed values are 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900 or 3000).
        :type silence_threshold: :py:class:`int`
        :param talk_detection: If set to YES, the conference dashboard will display a notification when a participant starts and stops talking (yes/no).
        :type talk_detection: :py:class:`str`
        :param jitter_buffer: When set to YES, the system will place a jitter buffer on the caller's audio stream before any audio mixing is performed (yes/no).
        :type jitter_buffer: :py:class:`str`
        :returns: :py:class:`dict`
        """

        method = "setConferenceMember"

        parameters = {}

        if not isinstance(conference, int):
            raise ValueError("")
        parameters["conference"] = conference

        if not isinstance(member, int):
            raise ValueError("")
        parameters["member"] = member 

        if not isinstance(name, str):
            raise ValueError("[Required] Member name")
        parameters["name"] = name

        if not isinstance(description, str):
            raise ValueError("[Required] Member description")
        parameters["description"] = description

        if "admin" in kwargs:
            if not isinstance(kwargs["admin"], str):
                raise ValueError("Sets if the member is an admin or not (yes/no).")
            parameters["admin"] = kwargs.pop("admin")

        if "start_muted" in kwargs:
            if not isinstance(kwargs["start_muted"], str):
                raise ValueError("Sets if the member should start out muted after entering the conference (yes/no).")
            parameters["start_muted"] = kwargs.pop("start_muted")

        if "announce_user_count" in kwargs:
            if not isinstance(kwargs["announce_user_count"], str):
                raise ValueError("Sets if the number of members in the conference should be announced to the caller as he joins (yes/no).")
            parameters["announce_user_count"] = kwargs.pop("announce_user_count")

        if "announce_only_user" in kwargs:
            if not isinstance(kwargs["announce_only_user"], str):
                raise ValueError("Sets if the \"only user\" announcement should be played when a caller enters an empty conference (yes/no).")
            parameters["announce_only_user"] = kwargs.pop("announce_only_user")

        if "moh_when_empty" in kwargs:
            if not isinstance(kwargs["moh_when_empty"], str):
                raise ValueError("Sets whether music on hold (MOH) should be played when only one person is in the conference (Values from getMusicOnHold).")
            parameters["moh_when_empty"] = kwargs.pop("moh_when_empty")

        if "quiet" in kwargs:
            if not isinstance(kwargs["quiet"], str):
                raise ValueError("When set to \"yes\", enter/leave prompts and user introductions are not played (yes/no).")
            parameters["quiet"] = kwargs.pop("quiet")

        if "accouncement" in kwargs:
            if not isinstance(kwargs["accouncement"], int):
                raise ValueError("If set, this recording will be heard only by the user as he joins the conference (Values from getRecordings).")
            parameters["accouncement"] = kwargs.pop("accouncement")

        if "drop_silence" in kwargs:
            if not isinstance(kwargs["drop_silence"], str):
                raise ValueError("The system will drop what is detected as silence from entering into the conference (yes/no).")
            parameters["drop_silence"] = kwargs.pop("drop_silence")

        if "talking_threshold" in kwargs:
            if not isinstance(kwargs["talking_threshold"], int):
                raise ValueError("The time, in milliseconds, that a users needs to be sending sound or voice before the system can consider them to be talking (allowed values are 100, 120, 140, 160, 180, 200, 220, 240 or 250).")
            parameters["talking_threshold"] = kwargs.pop("talking_threshold")

        if "silence_threshold" in kwargs:
            if not isinstance(kwargs["silence_threshold"], int):
                raise ValueError("The time, in milliseconds, that silence needs to be present in the user’s sound stream before the system can consider it to be in fact silent and close the audio (allowed values are 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900 or 3000).")
            parameters["silence_threshold"] = kwargs.pop("silence_threshold")

        if "talk_detection" in kwargs:
            if not isinstance(kwargs["talk_detection"], str):
                raise ValueError("If set to YES, the conference dashboard will display a notification when a participant starts and stops talking (yes/no).")
            parameters["talk_detection"] = kwargs.pop("talk_detection")

        if "jitter_buffer" in kwargs:
            if not isinstance(kwargs["jitter_buffer"], str):
                raise ValueError("When set to YES, the system will place a jitter buffer on the caller's audio stream before any audio mixing is performed (yes/no).")
            parameters["jitter_buffer"] = kwargs.pop("jitter_buffer")

        return self._voipms_client._get(method, parameters)

    def sequences(self, sequence, name, steps, client=None):
        """
        Updates a specific Sequence if a Sequence ID is provided

        - Adds a new Sequence entry if no Sequence ID is provided

        :param sequence: [Required] ID for a specific Sequence (Example: 5356)
        :type sequence: :py:class:`int`
        :param name: [Required] Sequence name
        :type name: :py:class:`str`
        :param steps: [Required] Sequence steps (Example: "[
                {
                    "type": "rec",
                    "id": "1234"
                },
                {
                    "type": "dtmf",
                    "codes": "1234"
                },
                {
                    "type": "sms",
                    "from": "0123456789",
                    "to": "1234,
                    "msg": "This is a test."
                },
            ]")
        :type steps: :py:class:`list`
        :param client: [Optional] ID for a specific Reseller Client (Example: 561115)
        :type client: :py:class:`int`
        :returns: :py:class:`dict`
        """
        method = "setSequences"

        parameters = {}

        if not isinstance(sequence, int):
            raise ValueError("[Required] ID for a specific Sequence (Example: 5356)")
        parameters["sequence"] = sequence

        if not isinstance(name, str):
            raise ValueError("[Required] Sequence name")
        parameters["name"] = name

        if not isinstance(steps, list):
            raise ValueError("""[Required] Sequence steps (Example: "[
                {
                    "type": "rec",
                    "id": "1234"
                },
                {
                    "type": "dtmf",
                    "codes": "1234"
                },
                {
                    "type": "sms",
                    "from": "0123456789",
                    "to": "1234,
                    "msg": "This is a test."
                },
            ]")""")
        parameters["steps"] = steps

        if client:
            if not isinstance(client, int):
                raise ValueError("[Optional] ID for a specific Reseller Client (Example: 561115)")
            parameters["client"] = client

        return self._voipms_client._get(method, parameters)
