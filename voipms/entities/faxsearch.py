# coding=utf-8
"""
The Fax API endpoint search

Documentation: https://voip.ms/m/apidocs.php
"""
from voipms.baseapi import BaseApi


class FaxSearch(BaseApi):
    """
    Search for the Fax endpoint.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(FaxSearch, self).__init__(*args, **kwargs)
        self.endpoint = 'fax'

    def fax_area_code_can(self, area_code):
        """
        Retrieves a list of Canadian Ratecenters searched by Area Code

        :param area_code: [Required] Area code number, as the initial of the Fax Number you looking for (values from fax.get_fax_rate_centers_can)
        :type area_code: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "searchFaxAreaCodeCAN"

        if not isinstance(area_code, int):
            raise ValueError("Area code number, as the initial of the Fax Number you looking for needs to be an int (values from fax.get_fax_rate_centers_can)")

        parameters = {
            "area_code": area_code,
        }

        return self._voipms_client._get(method, parameters)

    def fax_area_code_usa(self, area_code):
        """
        Retrieves a list of USA Ratecenters searched by Area Code

        :param area_code: [Required] Area code number, as the initial of the Fax Number you looking for (values from fax.get_fax_rate_centers_usa)
        :type area_code: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "searchFaxAreaCodeUSA"

        if not isinstance(area_code, int):
            raise ValueError("Area code number, as the initial of the Fax Number you looking for needs to be an int (values from fax.get_fax_rate_centers_usa)")

        parameters = {
            "area_code": area_code,
        }

        return self._voipms_client._get(method, parameters)
