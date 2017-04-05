# coding=utf-8
"""
The General API endpoint

Documentation: https://voip.ms/m/apidocs.php
"""
from voipms.baseapi import BaseApi
from voipms.entities.voicemailcreate import VoicemailCreate
from voipms.entities.voicemaildelete import VoicemailDelete
from voipms.entities.voicemailget import VoicemailGet
from voipms.entities.voicemailmark import VoicemailMark
from voipms.entities.voicemailmove import VoicemailMove
from voipms.entities.voicemailsend import VoicemailSend
from voipms.entities.voicemailset import VoicemailSet


class Voicemail(BaseApi):
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(Voicemail, self).__init__(*args, **kwargs)
        self.endoint = 'voicemail'
        self.create = VoicemailCreate(self)
        self.delete = VoicemailDelete(self)
        self.get = VoicemailGet(self)
        self.mark = VoicemailMark(self)
        self.move = VoicemailMove(self)
        self.send = VoicemailSend(self)
        self.set = VoicemailSet(self)
