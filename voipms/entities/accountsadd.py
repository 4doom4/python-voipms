# coding=utf-8
"""
The Accounts API endpoint add

Documentation: https://voip.ms/m/apidocs.php
"""
from voipms.baseapi import BaseApi


class AccountsAdd(BaseApi):
    """
    Add for the Accounts endpoint.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(AccountsAdd, self).__init__(*args, **kwargs)
        self.endpoint = 'accounts'

    def member_to_conference(self, member, conference):
        """
        Add member to a Conference

        :param music_on_hold: [Required] Specific Member ID (Example: 6547)
        :type music_on_hold: :py:class:`int`
        :param music_on_hold: [Required] Specific Conference ID (Example: 234)
        :type music_on_hold: :py:class:`int`
        :returns: :py:class:`dict`
        """
        method = "addMemberToConference"

        parameters = {}

        if not isinstance(member, str):
            raise ValueError("[Required] Specific Member ID (Example: 6547)")
        parameters["member"] = member

        if not isinstance(conference, str):
            raise ValueError("[Required] Specific Conference ID (Example: 234)")
        parameters["conference"] = conference

        return self._voipms_client._get(conference, parameters)
