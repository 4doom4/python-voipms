# coding=utf-8
"""
The Accounts API endpoint delete

Documentation: https://voip.ms/m/apidocs.php
"""
from voipms.baseapi import BaseApi


class AccountsDelete(BaseApi):
    """
    Delete for the Accounts endpoint.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(AccountsDelete, self).__init__(*args, **kwargs)
        self.endpoint = 'accounts'

    def music_on_hold(self, music_on_hold):
        """
        Deletes a specific custom Music on Hold

        :param music_on_hold: [Required] Music on Hold Name (Values from getMusicOnHold)
        :type music_on_hold: :py:class:`str`
        :returns: :py:class:`dict`
        """
        method = "delMusicOnHold"

        parameters = {}
        if not isinstance(music_on_hold, str):
            raise ValueError("[Required] Music on Hold Name (Values from getMusicOnHold)")
        parameters["music_on_hold"] = music_on_hold
        return self._voipms_client._get(method, parameters)

    def sub_account(self, account_id):
        """
        Deletes a specific Sub Account from your Account

        :param account_id: [Required] ID for a specific Sub Account (Example: 99785)
        :type account_id: :py:class:`str`
        :returns: :py:class:`dict`
        """
        method = "delSubAccount"

        parameters = {}
        if not isinstance(account_id, int):
            raise ValueError("ID for a specific Sub Account as int (Example: 99785) ")
        parameters["id"] = account_id
        return self._voipms_client._get(method, parameters)
