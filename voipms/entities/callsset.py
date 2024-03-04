# coding=utf-8
"""
The Calls API endpoint set

Documentation: https://voip.ms/m/apidocs.php
"""
from datetime import datetime

from voipms.baseapi import BaseApi
from voipms.helpers import validate_date, convert_bool


class CallsSet(BaseApi):
    """
    Set for the Calls endpoint.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(CallsSet, self).__init__(*args, **kwargs)
        self.endpoint = 'calls'

    def call_parking(self, name, timeout, music, failover, language, destination, delay,
                     blf_lamps, callparking=None):
        """
        Updates a specific Call Parking entry if a Call Parking ID is provided

        - Adds a new Call Parking entry if no Call Parking ID is provided

        :param callparking: ID for a specific Call Parking (Example: 235 / Leave empty to create a new one)
        :type callparking: :py:class:`int`
        :param name: [Required] Name for the Call Parking
        :type name: :py:class:`str`
        :param timeout: [Required] The number of seconds a call will stay parked before it is forwarded to the Failover Destination
        :type timeout: :py:class:`int`
        :param music: [Required] Music on Hold Code (Values from getMusicOnHold)  
        :type music: :py:class:`int`
        :param failover: [Required] Final destination where the call will be forwarded if it isn’t answered. (Values: callback, system:hangup, vm:mailbox)
        :type failover: :py:class:`str`
        :param language: [Required] Language for the Call Parking (values from getLanguages)
        :type language: :py:class:`str`
        :param destination: [Required] The system will make an automatic call to this destination to announce the extension of the parked call. (Values: parker, main account or sub-accounts)
        :type destination: :py:class:`str`
        :param delay: [Required] The number of seconds before the Announce Destination receives an automatic call from the system to announce the extension of the parked call
        :type delay: :py:class:`int`
        :param blf_lamps: [Required] You can enable BLF for your Parking Lot and select the amount of BLF Lamps that you require. (Values: 0 to 10)
        :type blf_lamps: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "setCallParking"

        if not isinstance(name, str):
            raise ValueError("ID for a specific Call Parking (Example: 235 / Leave empty to create a new one)")

        if not isinstance(timeout, int):
            raise ValueError("[Required] The number of seconds a call will stay parked before it is forwarded to the Failover Destination")

        if not isinstance(music, int):
            raise ValueError("[Required] Music on Hold Code (Values from getMusicOnHold)  ")

        if not isinstance(failover, str):
            raise ValueError("[Required] Final destination where the call will be forwarded if it isn’t answered. (Values: callback, system:hangup, vm:mailbox)")

        if not isinstance(language, str):
            raise ValueError("[Required] Language for the Call Parking (values from getLanguages)")

        if not isinstance(destination, str):
            raise ValueError("[Required] The system will make an automatic call to this destination to announce the extension of the parked call. (Values: parker, main account or sub-accounts)")

        if not isinstance(delay, int):
            raise ValueError("[Required] The number of seconds before the Announce Destination receives an automatic call from the system to announce the extension of the parked call")

        if not isinstance(blf_lamps, int):
            raise ValueError("[Required] You can enable BLF for your Parking Lot and select the amount of BLF Lamps that you require. (Values: 0 to 10)")

        parameters = {
            "name": name,
            "timeout": timeout,
            "music": music,
            "failover": failover,
            "language": language,
            "destination": destination,
            "delay": delay,
            "blf_lamp": blf_lamp,
        }

        if callparking:
            if not isinstance(callparking, int):
                raise ValueError("ID for a specific Call Parking (Example: 235 / Leave empty to create a new one)")
            parameters["callparking"] = callparking

        return self._voipms_client._get(method, parameters)
