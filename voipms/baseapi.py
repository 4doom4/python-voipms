class BaseApi(object):
    """
    Simple class to buid path for entities
    """
    def __init__(self, voipms_client):
        """
        Initialize the class with your voip_user and voip_api_password

        :param mc_client: The mailchimp client connection
        :type mc_client: :mod:`voipms.voipmsclient.VoipMsClient`
        """
        super(BaseApi, self).__init__()
        self._voipms_client = voipms_client
