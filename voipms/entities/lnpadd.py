# coding=utf-8
"""
The Local Number Portability (LNP) API endpoint add

Documentation: https://voip.ms/m/apidocs.php
"""
from voipms.baseapi import BaseApi


class LNPAdd(BaseApi):
    """
    Add for the Local Number Portability (LNP) endpoint.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(LNPAdd, self).__init__(*args, **kwargs)
        self.endpoint = 'lnp'

    def port(self, numbers, portType, imei, btn, services, tfType, statementName, firstName,
             lastName, address1, city, zip_code, state, country, providerName, providerAccount,
             isPartial=None, locationType=None, isMobile=None, snn=None, pin=None, address2=None,
             notes=None):
        """
        Add one or more numbers to start a portability process

        :param numbers: [Required] DID(s) to port into VoIP.ms network (Example: 5552341234,5552341233). If you are porting more than one number, please separate them with commas.
        :type numbers: :py:class:`str`
        :param portType: [Required] Digits from 1 to 4:
                            1: United States Local numbers
                            2: Canadian Local Numbers
                            3: US/CA Toll Free Numbers
                            4: United States Fax numbers
                            5: Canadian Fax Numbers
        :type portType: :py:class:`int`
        :param isPartial: If you have more then 1 number with your current carrier and not porting them all, choose yes. If you are porting all the numbers, choose no. Please note that you still need to include all numbers you want to port. If you have 2 numbers and want to port both, you need to include both numbers in the list of numbers to port. - (Values: 1 = true, 0 = false) - Default: 0
        :type isPartial: :py:class:`int`
        :param locationType: - (Values: 1 = Business, 0 = Residential) - Default: 0
        :type locationType: :py:class:`int`
        :param isMobile: - (Values: 1 = All the numbers are mobile numbers, 0 = false) - Default: 0
        :type isMobile: :py:class:`int`
        :param snn: - 4 Digits of the SNN, required if port type is 1 (USA Local) or 4 (USA Fax)
        :type snn: :py:class:`int`
        :param pin: PIN Number
        :type pin: :py:class:`int`
        :param imei: [Required If portType = 2 or portType = 5] If you are porting your mobile number(s), please provide the IMEI*. To get the IMEI* of your phone, you can dial *#06#
        :type imei: :py:class:`int`
        :param btn: [Required If isMobile = 1] BTN: It is the phone number to which all the other numbers of the customer are charged, in a consolidated telephone bill (instead of showing separate charges for each number you own). Please try to find the BTN on your invoice, and if you are unable to do so please contact the current provider to obtain it.
        :type btn: :py:class:`int`
        :param services: [Required If isMobile = 1] Please be specific and describe ALL remaining services with the current carrier. This includes DSL/Data services, Hunt Group services, etc. Any services NOT listed below may be disconnected upon completion of this port order.
        :type services: :py:class:`str`
        :param tfType: [Required If portType = 3] Values: 1 - American Carrier, American Callers Only, 2 - American Carrier, American and Canadian Callers allowed, 3 - Canadian Carrier
        :type tfType: :py:class:`str`
        :param statementName: [Required] This is for Business numbers only. Please type your Company Name if applicable, otherwise leave it blank.
        :type statementName: :py:class:`str`
        :param firstName: [Required] This is the "Customer First Name" as it appears on  the CSR (Customer Service Record) of the losing carrier. Please Enter the first name of the owner of the number or the autorized contact. No company name must be entered in the field.
        :type firstName: :py:class:`str`
        :param lastName: [Required] This is the "Customer Last Name" as it appears on  the CSR (Customer Service Record) of the losing carrier. Please Enter the last name of the owner of the number or the autorized contact. No company name must be entered in the field
        :type lastName: :py:class:`str`
        :param address1: [Required] This is the "Customer Address" as it appears on the CSR (Customer Service Record) of the losing carrier.
        :type address1: :py:class:`str`
        :param address2: Optional Address information (e.g: Suite 343)
        :type address2: :py:class:`str`
        :param city: [Required] This is the "City" as it appears on the CSR (Customer Service Record) of the losing carrier.
        :type city: :py:class:`str`
        :param zip_code: [Required] This is the "ZIP or Postal Code" as it appears on the CSR (Customer Service Record) of the losing carrier.
        :type zip_code: :py:class:`str`
        :param state: [Required] This is the "State or Province" as it appears on the CSR (Customer Service Record) of the losing carrier.
        :type state: :py:class:`str`
        :param country: [Required] This is the "Country" as it appears on the CSR (Customer Service Record) of the losing carrier.
        :type country: :py:class:`str`
        :param providerName: [Required] The name of your current service provider.
        :type providerName: :py:class:`str`
        :param providerAccount: [Required] Your Account with your current service provider.
        :type providerAccount: :py:class:`str`
        :param notes: - If you would like to include additional information regarding this port, you can use this parameter.
        :type notes: :py:class:`str`
        :returns: :py:class:`dict`
        """
        method = "addLNPPort"

        parameters = {}

        if not isinstance(numbers, str):
            raise ValueError("[Required] DID(s) to port into VoIP.ms network (Example: 5552341234,5552341233). If you are porting more than one number, please separate them with commas.")

        if not isinstance(portType, str):
            raise ValueError("""[Required] Digits from 1 to 4:
                            1: United States Local numbers
                            2: Canadian Local Numbers
                            3: US/CA Toll Free Numbers
                            4: United States Fax numbers
                            5: Canadian Fax Numbers""")

        if not isinstance(imei, str):
            raise ValueError("[Required If portType = 2 or portType = 5] If you are porting your mobile number(s), please provide the IMEI*. To get the IMEI* of your phone, you can dial *#06#")

        if not isinstance(btn, str):
            raise ValueError("[Required If isMobile = 1] BTN: It is the phone number to which all the other numbers of the customer are charged, in a consolidated telephone bill (instead of showing separate charges for each number you own). Please try to find the BTN on your invoice, and if you are unable to do so please contact the current provider to obtain it.")

        if not isinstance(services, str):
            raise ValueError("[Required If isMobile = 1] Please be specific and describe ALL remaining services with the current carrier. This includes DSL/Data services, Hunt Group services, etc. Any services NOT listed below may be disconnected upon completion of this port order.")

        if not isinstance(tfType, str):
            raise ValueError("[Required If portType = 3] Values: 1 - American Carrier, American Callers Only, 2 - American Carrier, American and Canadian Callers allowed, 3 - Canadian Carrier")

        if not isinstance(statementName, str):
            raise ValueError("[Required] This is for Business numbers only. Please type your Company Name if applicable, otherwise leave it blank.")

        if not isinstance(firstName, str):
            raise ValueError("[Required] This is the \"Customer First Name\" as it appears on  the CSR (Customer Service Record) of the losing carrier. Please Enter the first name of the owner of the number or the autorized contact. No company name must be entered in the field.")

        if not isinstance(lastName, str):
            raise ValueError("[Required] This is the \"Customer Last Name\" as it appears on  the CSR (Customer Service Record) of the losing carrier. Please Enter the last name of the owner of the number or the autorized contact. No company name must be entered in the field")

        if not isinstance(address1, str):
            raise ValueError("[Required] This is the \"Customer Address\" as it appears on the CSR (Customer Service Record) of the losing carrier.")

        if not isinstance(city, str):
            raise ValueError("[Required] This is the \"City\" as it appears on the CSR (Customer Service Record) of the losing carrier.")

        if not isinstance(zip_code, str):
            raise ValueError("[Required] This is the \"ZIP or Postal Code\" as it appears on the CSR (Customer Service Record) of the losing carrier.")

        if not isinstance(state, str):
            raise ValueError("[Required] This is the \"State or Province\" as it appears on the CSR (Customer Service Record) of the losing carrier.")

        if not isinstance(country, str):
            raise ValueError("[Required] This is the \"Country\" as it appears on the CSR (Customer Service Record) of the losing carrier.")

        if not isinstance(providerName, str):
            raise ValueError("[Required] The name of your current service provider.")

        if not isinstance(providerAccount, str):
            raise ValueError("[Required] Your Account with your current service provider.")

        parameters = {
            "numbers": numbers,
            "portType": portType,
            "imei": imei,
            "btn": btn,
            "services": services,
            "tfType": tfType,
            "statementName": statementName,
            "firstName": firstName,
            "lastName": lastName,
            "address1": address1,
            "city": lastName,
            "zip": zip_code,
            "state": state,
            "country": country,
            "providerName": providerName,
            "providerAccount": providerAccount
        }

        if isPartial:
            if not isinstance(isPartial, str):
                raise ValueError("If you have more then 1 number with your current carrier and not porting them all, choose yes. If you are porting all the numbers, choose no. Please note that you still need to include all numbers you want to port. If you have 2 numbers and want to port both, you need to include both numbers in the list of numbers to port. - (Values: 1 = true, 0 = false) - Default: 0")
            parameters["isPartial"] = isPartial

        if locationType:
            if not isinstance(locationType, str):
                raise ValueError("- (Values: 1 = Business, 0 = Residential) - Default: 0")
            parameters["locationType"] = locationType

        if isMobile:
            if not isinstance(isMobile, str):
                raise ValueError("- (Values: 1 = All the numbers are mobile numbers, 0 = false) - Default: 0")
            parameters["isMobile"] = isMobile

        if snn:
            if not isinstance(snn, str):
                raise ValueError("- 4 Digits of the SNN, required if port type is 1 (USA Local) or 4 (USA Fax)")
            parameters["snn"] = snn

        if pin:
            if not isinstance(pin, str):
                raise ValueError("PIN Number")
            parameters["pin"] = pin

        if address2:
            if not isinstance(address2, str):
                raise ValueError("Optional Address information (e.g: Suite 343)")
            parameters["address2"] = address2

        if notes:
            if not isinstance(notes, str):
                raise ValueError("- If you would like to include additional information regarding this port, you can use this parameter.")
            parameters["notes"] = notes

        return self._voipms_client._get(conference, parameters)

    def file(self, member, conference):
        """
        Add one or more numbers to start a portability process

        :param providerAccount: [Required] Your Account with your current service provider.
        :type providerAccount: :py:class:`str`
        :param portid: [Required] ID of the port previously created.
        :param file: [Required] Base 64 code of the file to be attached
        :returns: :py:class:`dict`
        """
        method = "addLNPFile"

        if not isinstance(providerAccount, str):
            raise ValueError("[Required] Your Account with your current service provider.")

        if not isinstance(portid, str):
            raise ValueError("[Required] ID of the port previously created.")

        if not isinstance(file, str):
            raise ValueError("[Required] Base 64 code of the file to be attached")

        parameters = {
            "providerAccount": providerAccount,
            "portid": portid,
            "file": file
        }

        return self._voipms_client._post(conference, parameters)
