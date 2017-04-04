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

    def sub_account(self, account_id):
        """
        Retrieves a list of Allowed Codecs if no additional parameter is provided

        - Retrieves a specific Allowed Codec if a codec code is provided

        :param auth_type: Code for a specific Codec (Example: 'ulaw;g729;gsm')
        :type auth_type: :py:class:`str`
        :returns: :py:class:`dict`
        """
        method = "delSubAccount"

        parameters = {}
        if account_id:
            if not isinstance(account_id, int):
                raise ValueError("ID for a specific Sub Account as int (Example: 99785) ")
            parameters["id"] = account_id
        return self._voipms_client._get(method, parameters)
