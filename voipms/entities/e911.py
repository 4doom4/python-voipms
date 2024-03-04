# coding=utf-8
"""
The e911 API endpoint

Documentation: https://voip.ms/m/apidocs.php
"""
from voipms.baseapi import BaseApi


class E911(BaseApi):
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(E911, self).__init__(*args, **kwargs)
        self.endoint = 'e911'

    def address_types(self, address_type=None):
        """
     	Retrieves a list of e911 Address Types if no additional parameter is provided.

        - Retrieves a specific e911 Address Type if an Address code is provided.

        :param address_type: Code for a specific Address Type (Example: Apartment)
        :type address_type: :py:class:`str`

        :returns: :py:class:`dict`
        """
        method = "e911AddressTypes"

        parameters = {
        }

        if address_type:
            if not isinstance(address_type, str):
                raise ValueError("Code for a specific Address Type (Example: Apartment)")
            else:
                parameters["address_type"] = address_type

        return self._voipms_client._get(method, parameters)

    def cancel(self, did):
        """
        Cancel the e911 Service from a specific DID

        :param did: [Required] DID to be canceled
        :type did: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "e911Cancel"

        parameters = {
        }

        if not isinstance(did, str):
            raise ValueError("[Required] DID to be canceled")
        else:
            parameters["did"] = did

        return self._voipms_client._get(method, parameters)

    def info(self, did):
        """
        Retrieves the e911 information from a specific DID

        :param did: [Required] DID with e911 enabled / in process
        :type did: :py:class:`int`

        :returns: :py:class:`dict`
        """
        method = "e911Info"

        parameters = {
        }

        if not isinstance(did, str):
            raise ValueError("[Required] DID with e911 enabled / in process")
        else:
            parameters["did"] = did

        return self._voipms_client._get(method, parameters)

    def provision(self, did, full_name, street_number, street_name, city, state, country, zip_code, language, email, address_type=None, address_number=None, other_info=None):
        """
        Subscribes your DID to the e911 Emergency Services

        :param did: [Required] DID that will be sent to the e911 service.
        :type did: :py:class:`str`
        :param full_name: [Required] Full Name that will be sent to the e911 service.
        :type full_name: :py:class:`str`
        :param street_number: [Required] Street Number that will be sent to the e911 service.
        :param street_name: [Required] Street Name that will be sent to the e911 service.
        :type street_number: :py:class:`str`
        :type street_name: :py:class:`str`
        :param address_type: Address Type that will be sent to the e911 service (Values from e911AddressTypes).
        :type address_type: :py:class:`str`
        :param address_number: Address Number that will be sent to the e911 service.
        :type address_number: :py:class:`str`
        :param city: [Required] City that will be sent to the e911 service.
        :type city: :py:class:`str`
        :param state: [Required] State / Province that will be sent to the e911 service.
        :type state: :py:class:`str`
        :param country: [Required] Country that will be sent to the e911 service. Value can be US (United states) or CA (Canada).
        :type country: :py:class:`str`
        :param zip_code: [Required] Zip / Postal code that will be sent to the e911 service.
        :type zip_code: :py:class:`str`
        :param language: [Required] Language that will be sent to the e911 service. Only available for addresses from Canada. Value can be EN (English) or FR (French).
        :type language: :py:class:`str`
        :param email: [Required] Email that will be sent to the e911 service.
        :type email: :py:class:`str`
        :param other_info: Additional Address Information that will be sent to the e911 service. Only available for addresses from Canada.
        :type other_info: :py:class:`str`

        :returns: :py:class:`dict`
        """
        method = "e911Provision"

        if not isinstance(did, str):
            raise ValueError("[Required] DID that will be sent to the e911 service.")

        if not isinstance(full_name, str):
            raise ValueError("[Required] Full Name that will be sent to the e911 service.")

        if not isinstance(street_number, str):
            raise ValueError("[Required] Street Number that will be sent to the e911 service.")

        if not isinstance(street_name, str):
            raise ValueError("[Required] Street Name that will be sent to the e911 service.")

        if not isinstance(city, str):
            raise ValueError("[Required] City that will be sent to the e911 service.")

        if not isinstance(state, str):
            raise ValueError("[Required] State / Province that will be sent to the e911 service.")

        if not isinstance(country, str):
            raise ValueError("[Required] Country that will be sent to the e911 service. Value can be US (United states) or CA (Canada).")

        if not isinstance(zip_code, str):
            raise ValueError("[Required] Zip / Postal code that will be sent to the e911 service.")

        if not isinstance(language, str):
            raise ValueError("[Required] Language that will be sent to the e911 service. Only available for addresses from Canada. Value can be EN (English) or FR (French).")

        if not isinstance(email, str):
            raise ValueError("[Required] Email that will be sent to the e911 service.")

        parameters = {
            "did": did,
            "full_name": full_name,
            "street_number": street_number,
            "street_name": street_name,
            "city": city,
            "state": state,
            "country": country,
            "zip_code": zip_code,
            "language": language,
            "email": email,
        }

        if address_type:
            if not isinstance(address_type, str):
                raise ValueError("Address Type that will be sent to the e911 service (Values from e911AddressTypes).")
            parameters["address_type"] = address_type

        if address_number:
            if not isinstance(address_number, str):
                raise ValueError("Address Number that will be sent to the e911 service.")
            parameters["address_number"] = address_number

        if other_info:
            if not isinstance(other_info, str):
                raise ValueError("Additional Address Information that will be sent to the e911 service. Only available for addresses from Canada.")
            parameters["other_info"] = other_info

        return self._voipms_client._get(method, parameters)

    def provision_manually(self, did, full_name, street_number, street_name, city, state, country, zip_code, language, email, address_type=None, address_number=None, other_info=None):
        """
        Subscribes your DID to the e911 Emergency Services

        - All e911 information will be validated by the VoIP.ms staff

        :param did: [Required] DID that will be sent to the e911 service.
        :type did: :py:class:`str`
        :param full_name: [Required] Full Name that will be sent to the e911 service.
        :type full_name: :py:class:`str`
        :param street_number: [Required] Street Number that will be sent to the e911 service.
        :param street_name: [Required] Street Name that will be sent to the e911 service.
        :type street_number: :py:class:`str`
        :type street_name: :py:class:`str`
        :param address_type: Address Type that will be sent to the e911 service (Values from e911AddressTypes).
        :type address_type: :py:class:`str`
        :param address_number: Address Number that will be sent to the e911 service.
        :type address_number: :py:class:`str`
        :param city: [Required] City that will be sent to the e911 service.
        :type city: :py:class:`str`
        :param state: [Required] State / Province that will be sent to the e911 service.
        :type state: :py:class:`str`
        :param country: [Required] Country that will be sent to the e911 service. Value can be US (United states) or CA (Canada).
        :type country: :py:class:`str`
        :param zip_code: [Required] Zip / Postal code that will be sent to the e911 service.
        :type zip_code: :py:class:`str`
        :param language: [Required] Language that will be sent to the e911 service. Only available for addresses from Canada. Value can be EN (English) or FR (French).
        :type language: :py:class:`str`
        :param email: [Required] Email that will be sent to the e911 service.
        :type email: :py:class:`str`
        :param other_info: Additional Address Information that will be sent to the e911 service. Only available for addresses from Canada.
        :type other_info: :py:class:`str`

        :returns: :py:class:`dict`
        """
        method = "e911ProvisionManually"

        if not isinstance(did, str):
            raise ValueError("[Required] DID that will be sent to the e911 service.")

        if not isinstance(full_name, str):
            raise ValueError("[Required] Full Name that will be sent to the e911 service.")

        if not isinstance(street_number, str):
            raise ValueError("[Required] Street Number that will be sent to the e911 service.")

        if not isinstance(street_name, str):
            raise ValueError("[Required] Street Name that will be sent to the e911 service.")

        if not isinstance(city, str):
            raise ValueError("[Required] City that will be sent to the e911 service.")

        if not isinstance(state, str):
            raise ValueError("[Required] State / Province that will be sent to the e911 service.")

        if not isinstance(country, str):
            raise ValueError("[Required] Country that will be sent to the e911 service. Value can be US (United states) or CA (Canada).")

        if not isinstance(zip_code, str):
            raise ValueError("[Required] Zip / Postal code that will be sent to the e911 service.")

        if not isinstance(language, str):
            raise ValueError("[Required] Language that will be sent to the e911 service. Only available for addresses from Canada. Value can be EN (English) or FR (French).")

        if not isinstance(email, str):
            raise ValueError("[Required] Email that will be sent to the e911 service.")

        parameters = {
            "did": did,
            "full_name": full_name,
            "street_number": street_number,
            "street_name": street_name,
            "city": city,
            "state": state,
            "country": country,
            "zip_code": zip_code,
            "language": language,
            "email": email,
        }

        if address_type:
            if not isinstance(address_type, str):
                raise ValueError("Address Type that will be sent to the e911 service (Values from e911AddressTypes).")
            parameters["address_type"] = address_type

        if address_number:
            if not isinstance(address_number, str):
                raise ValueError("Address Number that will be sent to the e911 service.")
            parameters["address_number"] = address_number

        if other_info:
            if not isinstance(other_info, str):
                raise ValueError("Additional Address Information that will be sent to the e911 service. Only available for addresses from Canada.")
            parameters["other_info"] = other_info

        return self._voipms_client._get(method, parameters)

    def update(self, did, full_name, street_number, street_name, city, state, country, zip_code, language, email, address_type=None, address_number=None, other_info=None):
        """
        Updates the information from your e911 Emergency Services Subscription

        :param did: [Required] DID that will be sent to the e911 service.
        :type did: :py:class:`str`
        :param full_name: [Required] Full Name that will be sent to the e911 service.
        :type full_name: :py:class:`str`
        :param street_number: [Required] Street Number that will be sent to the e911 service.
        :param street_name: [Required] Street Name that will be sent to the e911 service.
        :type street_number: :py:class:`str`
        :type street_name: :py:class:`str`
        :param address_type: Address Type that will be sent to the e911 service (Values from e911AddressTypes).
        :type address_type: :py:class:`str`
        :param address_number: Address Number that will be sent to the e911 service.
        :type address_number: :py:class:`str`
        :param city: [Required] City that will be sent to the e911 service.
        :type city: :py:class:`str`
        :param state: [Required] State / Province that will be sent to the e911 service.
        :type state: :py:class:`str`
        :param country: [Required] Country that will be sent to the e911 service. Value can be US (United states) or CA (Canada).
        :type country: :py:class:`str`
        :param zip_code: [Required] Zip / Postal code that will be sent to the e911 service.
        :type zip_code: :py:class:`str`
        :param language: [Required] Language that will be sent to the e911 service. Only available for addresses from Canada. Value can be EN (English) or FR (French).
        :type language: :py:class:`str`
        :param email: [Required] Email that will be sent to the e911 service.
        :type email: :py:class:`str`
        :param other_info: Additional Address Information that will be sent to the e911 service. Only available for addresses from Canada.
        :type other_info: :py:class:`str`

        :returns: :py:class:`dict`
        """
        method = "e911Update"

        if not isinstance(did, str):
            raise ValueError("[Required] DID that will be sent to the e911 service.")

        if not isinstance(full_name, str):
            raise ValueError("[Required] Full Name that will be sent to the e911 service.")

        if not isinstance(street_number, str):
            raise ValueError("[Required] Street Number that will be sent to the e911 service.")

        if not isinstance(street_name, str):
            raise ValueError("[Required] Street Name that will be sent to the e911 service.")

        if not isinstance(city, str):
            raise ValueError("[Required] City that will be sent to the e911 service.")

        if not isinstance(state, str):
            raise ValueError("[Required] State / Province that will be sent to the e911 service.")

        if not isinstance(country, str):
            raise ValueError("[Required] Country that will be sent to the e911 service. Value can be US (United states) or CA (Canada).")

        if not isinstance(zip_code, str):
            raise ValueError("[Required] Zip / Postal code that will be sent to the e911 service.")

        if not isinstance(language, str):
            raise ValueError("[Required] Language that will be sent to the e911 service. Only available for addresses from Canada. Value can be EN (English) or FR (French).")

        if not isinstance(email, str):
            raise ValueError("[Required] Email that will be sent to the e911 service.")

        parameters = {
            "did": did,
            "full_name": full_name,
            "street_number": street_number,
            "street_name": street_name,
            "city": city,
            "state": state,
            "country": country,
            "zip_code": zip_code,
            "language": language,
            "email": email,
        }

        if address_type:
            if not isinstance(address_type, str):
                raise ValueError("Address Type that will be sent to the e911 service (Values from e911AddressTypes).")
            parameters["address_type"] = address_type

        if address_number:
            if not isinstance(address_number, str):
                raise ValueError("Address Number that will be sent to the e911 service.")
            parameters["address_number"] = address_number

        if other_info:
            if not isinstance(other_info, str):
                raise ValueError("Additional Address Information that will be sent to the e911 service. Only available for addresses from Canada.")
            parameters["other_info"] = other_info

        return self._voipms_client._get(method, parameters)

    def validate(self, did, full_name, street_number, street_name, city, state, country, zip_code, language, email, address_type=None, address_number=None, other_info=None):
        """
        Validates your e911 information in order to start your e911 Emergency Services Subscription.

        :param did: [Required] DID that will be sent to the e911 service.
        :type did: :py:class:`str`
        :param full_name: [Required] Full Name that will be sent to the e911 service.
        :type full_name: :py:class:`str`
        :param street_number: [Required] Street Number that will be sent to the e911 service.
        :param street_name: [Required] Street Name that will be sent to the e911 service.
        :type street_number: :py:class:`str`
        :type street_name: :py:class:`str`
        :param address_type: Address Type that will be sent to the e911 service (Values from e911AddressTypes).
        :type address_type: :py:class:`str`
        :param address_number: Address Number that will be sent to the e911 service.
        :type address_number: :py:class:`str`
        :param city: [Required] City that will be sent to the e911 service.
        :type city: :py:class:`str`
        :param state: [Required] State / Province that will be sent to the e911 service.
        :type state: :py:class:`str`
        :param country: [Required] Country that will be sent to the e911 service. Value can be US (United states) or CA (Canada).
        :type country: :py:class:`str`
        :param zip_code: [Required] Zip / Postal code that will be sent to the e911 service.
        :type zip_code: :py:class:`str`
        :param language: [Required] Language that will be sent to the e911 service. Only available for addresses from Canada. Value can be EN (English) or FR (French).
        :type language: :py:class:`str`
        :param email: [Required] Email that will be sent to the e911 service.
        :type email: :py:class:`str`
        :param other_info: Additional Address Information that will be sent to the e911 service. Only available for addresses from Canada.
        :type other_info: :py:class:`str`

        :returns: :py:class:`dict`
        """
        method = "e911Validate"

        if not isinstance(did, str):
            raise ValueError("[Required] DID that will be sent to the e911 service.")

        if not isinstance(full_name, str):
            raise ValueError("[Required] Full Name that will be sent to the e911 service.")

        if not isinstance(street_number, str):
            raise ValueError("[Required] Street Number that will be sent to the e911 service.")

        if not isinstance(street_name, str):
            raise ValueError("[Required] Street Name that will be sent to the e911 service.")

        if not isinstance(city, str):
            raise ValueError("[Required] City that will be sent to the e911 service.")

        if not isinstance(state, str):
            raise ValueError("[Required] State / Province that will be sent to the e911 service.")

        if not isinstance(country, str):
            raise ValueError("[Required] Country that will be sent to the e911 service. Value can be US (United states) or CA (Canada).")

        if not isinstance(zip_code, str):
            raise ValueError("[Required] Zip / Postal code that will be sent to the e911 service.")

        if not isinstance(language, str):
            raise ValueError("[Required] Language that will be sent to the e911 service. Only available for addresses from Canada. Value can be EN (English) or FR (French).")

        if not isinstance(email, str):
            raise ValueError("[Required] Email that will be sent to the e911 service.")

        parameters = {
            "did": did,
            "full_name": full_name,
            "street_number": street_number,
            "street_name": street_name,
            "city": city,
            "state": state,
            "country": country,
            "zip_code": zip_code,
            "language": language,
            "email": email,
        }

        if address_type:
            if not isinstance(address_type, str):
                raise ValueError("Address Type that will be sent to the e911 service (Values from e911AddressTypes).")
            parameters["address_type"] = address_type

        if address_number:
            if not isinstance(address_number, str):
                raise ValueError("Address Number that will be sent to the e911 service.")
            parameters["address_number"] = address_number

        if other_info:
            if not isinstance(other_info, str):
                raise ValueError("Additional Address Information that will be sent to the e911 service. Only available for addresses from Canada.")
            parameters["other_info"] = other_info

        return self._voipms_client._get(method, parameters)
