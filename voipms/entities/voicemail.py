from voipms.baseapi import BaseApi


class Voicemail(BaseApi):
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(Voicemail, self).__init__(*args, **kwargs)
        self.endoint = 'voicemail'
