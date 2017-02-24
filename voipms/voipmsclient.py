import requests

# Handle library reorganisation Python 2 > Python 3.
try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode

from .helpers import ERROR_CODES


class VoipMsClient(object):
    """
    Voip.ms class to communicate with the v1 REST API
    """
    def __init__(self, voip_user, voip_api_password):
        """
        Initialize the class with you voip_user and voip_api_password.

        :param voip_user: voip.ms user id (email)
        :type voip_user: :py:class:`str`
        :param voip_api_password: voip.ms API Password
        :type voip_api_password: :py:class:`str`
        """
        super(VoipMsClient, self).__init__()
        self.base_url = 'https://voip.ms/api/v1/rest.php?api_username={}&api_password={}&'.format(voip_user, voip_api_password)

    def _error_code(self, status):
        """
        Verify if query responded with error

        :param status: status from the voip.ms API
        :type voip_user: :py:class:`str`
        :returns: True
        """
        if status in ERROR_CODES:
            raise TypeError(ERROR_CODES[status])
        return None

    def _get(self, method, parameters=None):
        """
        Handle authenticated GET requests

        :param method: The method call for the API
        :type method: :py:class:`str`
        :param parameters: The query string parameters
        :type parameters: :py:class:`str`
        :returns: The JSON output from the API
        """
        query_set = {
            "method": method
        }
        if parameters:
            query_set.update(parameters)
        url = self.base_url + urlencode(query_set)

        try:
            r = requests.get(url)
        except requests.exceptions.RequestException as e:
            raise e
        else:
            r.raise_for_status()
            if r.status_code == 204:
                return None
            r_json = r.json()
            status = r_json["status"]
            if status != "success":
                self._error_code(status)
            return r_json
