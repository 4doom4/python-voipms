# coding=utf-8
"""
The Fax API endpoint mail

Documentation: https://voip.ms/m/apidocs.php
"""
from voipms.baseapi import BaseApi
from voipms.helpers import validate_email


class FaxMail(BaseApi):
    """
    Mail for the Fax endpoint.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(FaxMail, self).__init__(*args, **kwargs)
        self.endpoint = 'fax'

    def fax_message_pdf(self, fax_id, email):
        """
        Send a Fax Message attached as a PDF file to an email destination

        :param fax_id: [Required] ID of the Fax Message requested (Values from fax.get_fax_messages)
        :type fax_id: :py:class:`int`
        :param email: [Required] Destination email address (example: yourname@company.com)
        :type email: :py:class:`str`

        :returns: :py:class:`dict`
        """
        method = "mailFaxMessagePDF"

        if not isinstance(fax_id, int):
            raise ValueError("ID of the Fax Message requested needs to be an int (Values from fax.get_fax_messages)")

        if not isinstance(email, str):
            raise ValueError("Destination email address needs to be a str(example: yourname@company.com)")
        elif not validate_email(email):
                raise ValueError("Destination email address is not a correct email syntax")

        parameters = {
            "id": fax_id,
            "email": email,
        }

        return self._voipms_client._get(method, parameters)
