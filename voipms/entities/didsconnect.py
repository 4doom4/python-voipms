# coding=utf-8
"""
The Dids API endpoint connect

Documentation: https://voip.ms/m/apidocs.php
"""
from voipms.baseapi import BaseApi
from voipms.helpers import validate_date, convert_bool


class DidsConnect(BaseApi):
    """
    Connect for the Dids endpoint.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(DidsConnect, self).__init__(*args, **kwargs)
        self.endpoint = 'dids'

    def connect_did(self, did, account, monthly, setup, minute, **kwargs):
        """
        Connects a specific DID to a specific Reseller Client Sub Account

        :param did: [Required] DID to be canceled and deleted (Example: 5551234567)
        :type did: :py:class:`str` or `int`
        :param account: [Required] Reseller Sub Account (Example: '100001_VoIP')
        :type account: :py:class:`str`
        :param monthly: [Required] Montly Fee for Reseller Client (Example: 3.50)
        :type monthly: :py:class:`float`
        :param setup: [Required] Setup Fee for Reseller Client (Example: 1.99)
        :type setup: :py:class:`float`
        :param minute: [Required] Minute Rate for Reseller Client (Example: 0.03)
        :type minute: :py:class:`float`
        :param **kwargs: All optional parameters
        :type **kwargs: :py:class:`dict`

        :param next_billing: Next billing date (Example: '2014-03-30')
        :type next_billing: :py:class:`str`
        :param dont_charge_setup: If set to true, the setup value will not be charged after Connect
        :type dont_charge_setup: :py:class:`bool`
        :param dont_charge_monthly: If set to true, the monthly value will not be charged after Connect
        :type dont_charge_monthly: :py:class:`bool`

        :returns: :py:class:`dict`
        """
        method = "connectDID"

        if isinstance(did, str):
            did = did.replace('.', '')
            try:
                did = int(did)
            except:
                raise ValueError("DID to be canceled and deleted needs to be an int or str of numbers (Example: 555.123.4567 or 5551234567)")
        if not isinstance(did, int):
            raise ValueError("DID to be canceled and deleted needs to be an int (Example: 5551234567)")

        if not isinstance(account, str):
            raise ValueError("Reseller Sub Account needs to be a str (Example: '100001_VoIP')")

        if not isinstance(monthly, float):
            raise ValueError("Montly Fee for Reseller Client needs to be a float (Example: 3.50)")

        if not isinstance(setup, float):
            raise ValueError("Setup Fee for Reseller Client needs to be a float (Example: 1.99)")

        if not isinstance(minute, float):
            raise ValueError("Minute Rate for Reseller Client needs to be a float (Example: 0.03)")

        parameters = {
            "did": did,
            "account": account,
            "monthly": monthly,
            "setup": setup,
            "minute": minute,
        }

        if "next_billing" in kwargs:
            if not isinstance(kwargs["next_billing"], str):
                raise ValueError("Next billing date needs to be a str (Example: '2014-03-30')")
            validate_date(kwargs["next_billing"])
            parameters["next_billing"] = kwargs.pop("next_billing")

        if "dont_charge_setup" in kwargs:
            if not isinstance(kwargs["dont_charge_setup"], bool):
                raise ValueError("If set to True, the setup value will not be charged after Connect (needs to be bool)")
            parameters["dont_charge_setup"] = convert_bool(kwargs.pop("dont_charge_setup"))

        if "dont_charge_monthly" in kwargs:
            if not isinstance(kwargs["dont_charge_monthly"], bool):
                raise ValueError("If set to True, the monthly value will not be charged after Connect (needs to be bool)")
            parameters["dont_charge_monthly"] = convert_bool(kwargs.pop("dont_charge_monthly"))

        if len(kwargs) > 0:
            not_allowed_parameters = ""
            for key, value in kwargs.items():
                not_allowed_parameters += key + " "
            raise ValueError("Parameters not allowed: {}".format(not_allowed_parameters))

        return self._voipms_client._get(method, parameters)
