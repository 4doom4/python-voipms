# coding=utf-8
"""
The Dids API endpoint delete

Documentation: https://voip.ms/m/apidocs.php
"""
from voipms.baseapi import BaseApi


class DidsDelete(BaseApi):
    """
    Delete for the Dids endpoint.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(DidsDelete, self).__init__(*args, **kwargs)
        self.endpoint = 'dids'

    def callback(self, callback):
        """
        Deletes a specific Callback from your Account

        :param callback: [Required] ID for a specific Callback (Example: 19183)
        :type callback: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "delCallback"

        if not isinstance(callback, int):
            raise ValueError("ID for a specific Callback needs to be an int (Example: 19183)")
        parameters = {
            "callback": callback
        }

        return self._voipms_client._get(method, parameters)

    def caller_id_filtering(self, filtering):
        """
        Deletes a specific CallerID Filtering from your Account

        :param filtering: [Required] ID for a specific CallerID Filtering (Example: 19183)
        :type filtering: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "delCallerIDFiltering"

        if not isinstance(filtering, str):
            raise ValueError("ID for a specific CallerID Filtering needs to be an int (Example: 19183)")
        parameters = {
            "filtering": filtering
        }

        return self._voipms_client._get(method, parameters)

    def call_hunting(self, callhunting):
        """
        Deletes a specific Caller Hunting from your Account

        :param callhunting: [Required] ID for a specific Call Hunting (Example: 323)
        :type callhunting: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "delCallHunting"

        if not isinstance(callhunting, str):
            raise ValueError("[Required] ID for a specific Call Hunting (Example: 323)")
        parameters = {
            "callhunting": callhunting
        }

        return self._voipms_client._get(method, parameters)

    def conference(self, conference):
        """
        Deletes a specific Conference from your Account

        :param conference: [Required] ID for a specific Conference (Example: 737)
        :type conference: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "delConference"

        if not isinstance(conference, str):
            raise ValueError("[Required] ID for a specific Conference (Example: 737)")
        parameters = {
            "conference": conference
        }

        return self._voipms_client._get(method, parameters)

    def conference_member(self, member):
        """
        Deletes a specific Member profile from your Account

        :param member: [Required] ID for a specific Member Profile (Example: 737)
        :type member: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "delConferenceMember"

        if not isinstance(member, str):
            raise ValueError("[Required] ID for a specific Member Profile (Example: 737)")
        parameters = {
            "member": member
        }

        return self._voipms_client._get(method, parameters)

    def client(self, client):
        """
        Deletes a specific reseller client from your Account

        :param client: [Required] ID for a specific Reseller Client (Example: 1998)
        :type client: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "delClient"

        if not isinstance(client, int):
            raise ValueError("ID for a specific Reseller Client needs to be an int (Example: 1998)")
        parameters = {
            "client": client
        }

        return self._voipms_client._get(method, parameters)

    def disa(self, disa):
        """
        Deletes a specific DISA from your Account

        :param disa: [Required] ID for a specific DISA (Example: 19183)
        :type disa: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "delDISA"

        if not isinstance(disa, int):
            raise ValueError("ID for a specific DISA needs to be an int (Example: 19183)")
        parameters = {
            "disa": disa
        }

        return self._voipms_client._get(method, parameters)

    def forwarding(self, forwarding):
        """
        Deletes a specific Forwarding from your Account

        :param forwarding: [Required] ID for a specific Forwarding (Example: 19183)
        :type forwarding: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "delForwarding"

        if not isinstance(forwarding, int):
            raise ValueError("ID for a specific Forwarding needs to be an int (Example: 19183)")
        parameters = {
            "forwarding": forwarding
        }

        return self._voipms_client._get(method, parameters)

    def ivr(self, ivr):
        """
        Deletes a specific IVR from your Account

        :param ivr: [Required] ID for a specific IVR (Example: 19183)
        :type ivr: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "delIVR"

        if not isinstance(ivr, int):
            raise ValueError("ID for a specific IVR needs to be an int (Example: 19183)")
        parameters = {
            "ivr": ivr
        }

        return self._voipms_client._get(method, parameters)

    def mms(self, mms_id):
        """
        Deletes a specific MMS from your Account

        :param mms_id: [Required] ID for a specific MMS (Example: 1918)
        :type mms_id: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "deleteMMS"

        if not isinstance(mms_id, int):
            raise ValueError("ID for a specific MMS needs to be an int (Example: 1918)")
        parameters = {
            "id": mms_id
        }

        return self._voipms_client._get(method, parameters)

    def phonebook(self, phonebook):
        """
        Deletes a specific Phonebook from your Account

        :param phonebook: [Required] ID for a specific Phonebook (Example: 19183)
        :type phonebook: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "delPhonebook"

        if not isinstance(phonebook, int):
            raise ValueError("ID for a specific Phonebook needs to be an int (Example: 19183)")
        parameters = {
            "phonebook": phonebook
        }

        return self._voipms_client._get(method, parameters)

    def phonebook_group(self, group):
        """
        Deletes a specific Phonebook group from your Account

        :param group: [Required] ID for a specific Phonebook group
        :type group: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "delPhonebookGroup"

        if not isinstance(group, int):
            raise ValueError("[Required] ID for a specific Phonebook group")
        parameters = {
            "group": group
        }

        return self._voipms_client._get(method, parameters)

    def queue(self, queue):
        """
        Deletes a specific Queue from your Account

        :param queue: [Required] ID for a specific Queue (Example: 13183)
        :type queue: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "delQueue"

        if not isinstance(queue, int):
            raise ValueError("ID for a specific Queue needs to be an int (Example: 13183)")
        parameters = {
            "queue": queue
        }

        return self._voipms_client._get(method, parameters)

    def recording(self, recording):
        """
        Deletes a specific Recording from your Account

        :param recording: [Required] ID for a specific Recording (Example: 19183)
        :type recording: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "delRecording"

        if not isinstance(recording, int):
            raise ValueError("ID for a specific Recording needs to be an int (Example: 19183)")
        parameters = {
            "recording": recording
        }

        return self._voipms_client._get(method, parameters)

    def ring_group(self, ringgroup):
        """
        Deletes a specific Ring Group from your Account

        :param ringgroup: [Required] ID for a specific Ring Group (Example: 19183)
        :type ringgroup: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "delRingGroup"

        if not isinstance(ringgroup, int):
            raise ValueError("ID for a specific Ring Group needs to be an int (Example: 19183)")
        parameters = {
            "ringgroup": ringgroup
        }

        return self._voipms_client._get(method, parameters)

    def sequences(self, sequence, client=None):
        """
        Deletes a specific Sequence from your Account

        :param sequence: [Required] ID for a specific Sequence (Example: 5356)
        :type sequence: :py:class:`int`
        :param client: [Optional] ID for a specific Reseller Client (Example: 561115)
        :type client: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "delSequences"

        parameters = {}
        if not isinstance(sequence, str):
            raise ValueError("[Required] ID for a specific Sequence (Example: 737)")
        parameters["sequence"] = sequence

        if client:
            if not isinstance(sequence, str):
                raise ValueError("[Required] ID for a specific Sequence (Example: 737)")
            parameters["client"] = client

        return self._voipms_client._get(method, parameters)

    def sip_uri(self, sipuri):
        """
        Deletes a specific SIP URI from your Account

        :param sipuri: [Required] ID for a specific SIP URI (Example: 19183)
        :type sipuri: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "delSIPURI"

        if not isinstance(sipuri, int):
            raise ValueError("ID for a specific SIP URI needs to be an int (Example: 19183)")
        parameters = {
            "sipuri": sipuri
        }

        return self._voipms_client._get(method, parameters)

    def sms(self, sms_id):
        """
        Deletes a specific SMS from your Account

        :param sms_id: [Required] ID for a specific SMS (Example: 1918)
        :type sms_id: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "deleteSMS"

        if not isinstance(sms_id, int):
            raise ValueError("ID for a specific SMS needs to be an int (Example: 1918)")
        parameters = {
            "id": sms_id
        }

        return self._voipms_client._get(method, parameters)

    def static_member(self, member, queue):
        """
        Deletes a specific Static Member from Queue

        :param member: [Required] ID for a specific Member Queue (Example: 1918)
        :type member: :py:class:`int`
        :param queue: [Required] ID for a specific Queue (Example: 27183)
        :type queue: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "delStaticMember"

        if not isinstance(member, int):
            raise ValueError("ID for a specific Member Queue needs to be an int (Example: 19183)")

        if not isinstance(queue, int):
            raise ValueError("ID for a specific Queue needs to be an int (Example: 19183)")

        parameters = {
            "member": member,
            "queue": queue,
        }

        return self._voipms_client._get(method, parameters)

    def time_condition(self, timecondition):
        """
        Deletes a specific Time Condition from your Account

        :param timecondition: [Required] ID for a specific Time Condition (Example: 19183)
        :type timecondition: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "delTimeCondition"

        if not isinstance(timecondition, int):
            raise ValueError("ID for a specific Time Condition needs to be an int (Example: 19183)")
        parameters = {
            "timecondition": timecondition
        }

        return self._voipms_client._get(method, parameters)
