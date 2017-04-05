import datetime
import re


def convert_bool(boolean):
    if not isinstance(boolean, bool):
        raise ValueError("Needs to be a bool")
    if boolean:
        return "1"
    else:
        return "0"


def validate_date(date_text):
    try:
        date_object = datetime.datetime.strptime(date_text, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")
    return date_object


def validate_email(email):
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)
    if match:
        return True
    else:
        return False


def order(**kwargs):

    parameters = {}

    international_fields = ("location_id", "quantity", "routing", "pop", "dialtime", "cnam")
    did_fields = ("did", "routing", "pop", "dialtime", "cnam", "billing_type")
    required_fields = {
        "backOrderDIDUSA": ("quantity", "state", "ratecenter", "routing", "pop", "dialtime", "cnam", "billing_type"),
        "backOrderDIDCAN": ("quantity", "province", "ratecenter", "routing", "pop", "dialtime", "cnam", "billing_type"),
        "orderDID": did_fields,
        "orderDIDInternationalGeographic": international_fields,
        "orderDIDInternationalNational": international_fields,
        "orderDIDInternationalTollFree": international_fields,
        "orderDIDVirtual": ("digits", "routing", "pop", "dialtime", "cnam", "billing_type"),
        "orderTollFree": did_fields,
        "orderVanity": ("did", "routing", "pop", "dialtime", "cnam", "billing_type", "carrier"),
    }

    # Minimize possibility of code injection
    if "method" in kwargs:
        if not isinstance(kwargs["method"], str):
            raise ValueError("method needs to be a str")
        else:
            if kwargs["method"] not in required_fields:
                raise ValueError("This method is not allowed")
        method = kwargs.pop("method")
    else:
        raise ValueError("A method needs to be specified")

    if "did" in kwargs:
        if not isinstance(kwargs["did"], int):
            raise ValueError("DID to be Ordered needs to be an int (Example: 5552223333)")
        parameters["did"] = kwargs.pop("did")

    if "digits" in kwargs:
        if not isinstance(kwargs["digits"], int):
            raise ValueError("Three Digits for the new Virtual DID needs to be an int (Example: 001)")
        parameters["digits"] = kwargs.pop("digits")

    if "location_id" in kwargs:
        if not isinstance(kwargs["location_id"], int):
            raise ValueError("ID for a specific International Location needs to be an int (Values from dids.get_dids_international_geographic)")
        parameters["location_id"] = kwargs.pop("location_id")

    if "quantity" in kwargs:
        if not isinstance(kwargs["quantity"], int):
            raise ValueError("Number of dids to be purchased needs to be an int (Example: 2)")
        parameters["quantity"] = kwargs.pop("quantity")

    if "state" in kwargs:
        if not isinstance(kwargs["state"], str):
            raise ValueError("USA State needs to be a str (values from dids.get_states)")
        parameters["state"] = kwargs.pop("state")

    if "province" in kwargs:
        if not isinstance(kwargs["province"], str):
            raise ValueError("Canadian Province needs to be a str (values from dids.get_provinces)")
        parameters["province"] = kwargs.pop("province")

    if "ratecenter" in kwargs:
        if not isinstance(kwargs["ratecenter"], str):
            if method == "backOrderDIDUSA":
                raise ValueError("USA Ratecenter needs to be a str (Values from dids.get_rate_centers_usa)")
            else:
                raise ValueError("Canada Ratecenter needs to be a str (Values from dids.get_rate_centers_can)")
        parameters["ratecenter"] = kwargs.pop("ratecenter")

    if "routing" in kwargs:
        if not isinstance(kwargs["routing"], str):
            raise ValueError("Main Routing for the DID needs to be an int (Values from accounts.get_routes)")
        parameters["routing"] = kwargs.pop("routing")

    if "failover_busy" in kwargs:
        if not isinstance(kwargs["failover_busy"], str):
            raise ValueError("Busy Routing for the DID needs to be a str")
        parameters["failover_busy"] = kwargs.pop("failover_busy")

    if "failover_unreachable" in kwargs:
        if not isinstance(kwargs["failover_unreachable"], str):
            raise ValueError("Unreachable Routing for the DID needs to be a str")
        parameters["failover_unreachable"] = kwargs.pop("failover_unreachable")

    if "failover_noanswer" in kwargs:
        if not isinstance(kwargs["failover_noanswer"], str):
            raise ValueError("NoAnswer Routing for the DID")
        parameters["failover_noanswer"] = kwargs.pop("failover_noanswer")

    if "voicemail" in kwargs:
        if not isinstance(kwargs["voicemail"], int):
            raise ValueError("Voicemail for the DID needs to be an int (Example: 101)")
        parameters["voicemail"] = kwargs.pop("voicemail")

    if "pop" in kwargs:
        if not isinstance(kwargs["pop"], int):
            raise ValueError("Point of pop for the DID needs to be an int (Example: 5)")
        parameters["pop"] = kwargs.pop("pop")

    if "dialtime" in kwargs:
        if not isinstance(kwargs["dialtime"], int):
            raise ValueError("Dial Time Out for the DID needs to be an int (Example: 60 -> in seconds)")
        parameters["dialtime"] = kwargs.pop("dialtime")

    if "cnam" in kwargs:
        if not isinstance(kwargs["cnam"], bool):
            raise ValueError("CNAM for the DID needs to be a bool (Boolean: True/False)")
        parameters["cnam"] = convert_bool(kwargs.pop("cnam"))

    if "carrier" in kwargs:
        if not isinstance(kwargs["carrier"], int):
            raise ValueError("Carrier for the DID needs to be a bool (Values from dids.get_carriers)")
        parameters["carrier"] = convert_bool(kwargs.pop("carrier"))

    if "callerid_prefix" in kwargs:
        if not isinstance(kwargs["callerid_prefix"], str):
            raise ValueError("Caller ID Prefix for the DID needs to be a str")
        parameters["callerid_prefix"] = kwargs.pop("callerid_prefix")

    if "note" in kwargs:
        if not isinstance(kwargs["note"], str):
            raise ValueError("Note for the DID needs to be a str")
        parameters["note"] = kwargs.pop("note")

    if "billing_type" in kwargs:
        if not isinstance(kwargs["billing_type"], int):
            raise ValueError("Billing type for the DID needs to be an int (1 = Per Minute, 2 = Flat)")
        parameters["billing_type"] = kwargs.pop("billing_type")

    if "account" in kwargs:
        if not isinstance(kwargs["account"], str):
            raise ValueError("Reseller Sub Account needs to be a str (Example: '100001_VoIP')")
        parameters["account"] = kwargs.pop("account")

    if "monthly" in kwargs:
        if not isinstance(kwargs["monthly"], float):
            raise ValueError("Montly Fee for Reseller Client needs to be a float (Example: 3.50)")
        parameters["monthly"] = kwargs.pop("monthly")

    if "setup" in kwargs:
        if not isinstance(kwargs["setup"], float):
            raise ValueError("Setup Fee for Reseller Client needs to be a float (Example: 1.99)")
        parameters["setup"] = kwargs.pop("setup")

    if "minute" in kwargs:
        if not isinstance(kwargs["minute"], float):
            raise ValueError("Minute Rate for Reseller Client needs to be a float (Example: 0.03)")
        parameters["minute"] = kwargs.pop("minute")

    if "test" in kwargs:
        if not isinstance(kwargs["test"], bool):
            raise ValueError("Test needs to be a bool (True/False)")
        parameters["test"] = convert_bool(kwargs.pop("test"))

    if len(kwargs) > 0:
        not_allowed_parameters = ""
        for key, value in kwargs.items():
            not_allowed_parameters += key + " "
        raise ValueError("Parameters not allowed: {}".format(not_allowed_parameters))

    # Verify again if all required fields present
    for field in required_fields[method]:
        if field not in parameters:
            raise ValueError("The parameter {} is required".format(field))

    return method, parameters


ERROR_CODES = {
    "account_with_dids": "The Account has DIDs assigned to it.",
    "api_not_enabled": "API has not been enabled or has been disabled",
    "cancel_failed": "The cancellation wasn't completed.",
    "did_in_use": "DID Number is already in use",
    "error_deleting_msg": "Error when deleting message",
    "error_moving_msg": "Error when move the voicemail message to folder",
    "existing_did": "You can't set a callback to an existing VoIP.ms DID number",
    "exceeds_file_size": "The file exceeds the limite size allowed.",
    "forwards_exceeded": "Your account is limited to 4 forward entries",
    "invalid_account": "This is not a valid account",
    "invalid_agent_ring_timeout": "This is not a valid Agent ring time out value",
    "invalid_allowedcodecs": "One of the codecs provided is invalid Format and Values: ulaw;g729;gsm;all",
    "invalid_announce_position_frequency": "This is nota a valid Announce position frequency",
    "invalid_announce_round_seconds": "This is nota a valid Announce round seconds",
    "invalid_attachmessage": "This is not a valid AttachMessage Should be: yes/no",
    "invalid_area_code": "This is not a valid Area Code.",
    "invalid_authtype": "This is not a valid Auth Type",
    "invalid_authtype_h323": "You must select IP Auth to use H.323",
    "invalid_authtype_iax2": "You must use User/Password Authentication for IAX2",
    "invalid_balancemanagement": "This is not a valid BalanceManagement",
    "invalid_base_recording": "This is not a valid recording path",
    "invalid_billingtype": "This is not a valid Billing Type Allowed values: 1 = PerMinute, 2 = Flat",
    "invalid_callback": "This is not a valid Callback",
    "invalid_callback_enable": "This is not a valid Callback enable value",
    "invalid_callback_retry": "This is not a valid Callback retry",
    "invalid_callerid": "This is not a valid CallerID",
    "invalid_calleridprefix": "This is not a valid CID Prefix, lenght should be less than 20 chars",
    "invalid_callerid_override": "This is not a valid CallerID Override",
    "invalid_canada_routing": "This is not a valid Canada Route",
    "invalid_carrier": "This is not a valid Carrier",
    "invalid_charge": "This is not a valid Charge",
    "invalid_client": "This is not a valid Client",
    "invalid_cnam": "This is not a valid CNAM Should be: 1/0",
    "invalid_codec": "This is not a valid Codec",
    "invalid_contact": "This is not a valid Contact Number",
    "invalid_country": "This is not a valid country Examples: US / CA",
    "invalid_countryid": "This is not a valid Country ID",
    "invalid_credentials": "Username or Password is incorrect",
    "invalid_date": "This is not a valid date Format is: yyyy-mm-dd",
    "invalid_daterange": "Date Range should be 92 days or less",
    "invalid_dayrange": "This is not a valid Day Range",
    "invalid_delay_before": "This is not a valid DelayBefore",
    "invalid_deletemessage": "This is not a valid DeleteMessage Should be: yes/no",
    "invalid_description": "This is not a valid Description",
    "invalid_devicetype": "This is not a valid Device Type",
    "invalid_dialtime": "This is not a valid Dialtime",
    "invalid_did": "This is not a valid DID",
    "invalid_digits": "These are not valid Digits OrderDIDVirtual: Digits must be 3 numbers",
    "invalid_digit_timeout": "This is not a valid DigitTimeOut",
    "invalid_disa": "This is not a valid DISA",
    "invalid_destination_folder": "This is not a valid Destination Folder",
    "invalid_dst": "This is not a valid Destination Number",
    "invalid_dtmf_digits": "This is no a valid DTMF digit",
    "invalid_dtmfmode": "This is no a valid DTMF Mode",
    "invalid_email": "This is not a valid email or email is already in database",
    "invalid_email_attachment_format": "This is not a valid format value",
    "invalid_email_enable": "This is not a valid email enable value",
    "invalid_endhour": "This is not a valid End Hour",
    "invalid_endminute": "This is not a valid End Minute",
    "invalid_extension": "This is not a valid extension Extension can only contain digits",
    "invalid_failover_header": "This is not a valid failover header Should be: account/vm/fwd/none",
    "invalid_fax_id": "This is not a valid Fax Message ID",
    "invalid_file": "This is not a valid File",
    "invalid_filter": "This is not a valid Filter",
    "invalid_folder": "This is not a valid Folder",
    "invalid_folder_id": "This is not a valid Fax Folder ID",
    "invalid_forward_enable": "This is not a valid forward enable value",
    "invalid_forwarding": "This is not a valid forwarding",
    "invalid_forwarding_did": "Forwarding to the same did is not allowed",
    "invalid_frequency_announcement": "This is not a valid Frequency announce",
    "invalid_from_number": "This is not a valid sender number.",
    "invalid_id": "This is not a valid ID",
    "invalid_if_announce_position_enabled_report_estimated_hold_time": "This is not a Report estimated hold time type",
    "invalid_internaldialtime": "This is not a valid Internal Dialtime Should be: 1 to 60",
    "invalid_internalvoicemail": "This is not a valid Internal Voicemail",
    "invalid_internationalroute": "This is not a valid International Route",
    "invalid_ip": "This is an invalid IP",
    "invalid_ip_auth": "Do not provide an IP address for User/Pass Authentication",
    "invalid_ip_iax2": "Do not provide an IP address for IAX2",
    "invalid_ivr": "This is not a valid IVR",
    "invalid_join_empty_type": "This is not a valid 'JoinWhenEmpty' Type for a Queue",
    "invalid_join_announcement": "This is not a valid 'Join Announcement' Type for a Queue",
    "invalid_language": "This is not a valid Language Should be: es/en/fr",
    "invalid_listened": "This is not a valid Listened value",
    "invalid_location": "This is not a valid Location",
    "invalid_lockinternational": "This is not a valid Lock International",
    "invalid_mailbox": "This is not a valid mailbox",
    "invalid_maximum_callers": "This is not a valid maximum callers value",
    "invalid_maximum_wait_time": "This is not a valid maximum wait time value",
    "invalid_method": "This is not a valid Method",
    "invalid_member": "This is not a valid Member",
    "invalid_member_delay": "This is not a valid Member Delay",
    "invalid_message_num": "This is not a valid Voicemail Message Number",
    "invalid_minute": "This is not a valid Minute Rate",
    "invalid_monthly": "This is not a valid Montly Fee",
    "invalid_musiconhold": "This is not a valid Music on Hold",
    "invalid_name": "This is not a valid name, Alphanumeric Only",
    "invalid_nat": "This is not a valid NAT",
    "invalid_note": "This is not a valid Note, lenght should be less than 50 chars",
    "invalid_number": "This is not a valid Number",
    "invalid_package": "This is not a valid Package",
    "invalid_password": "This is not a valid password Voicemail: Must be 4 Digits SubAccounts: More than 6 chars, Must Contain Alphanumeric and !#$%&/()=?*[]_:.,{}+-",
    "invalid_password_auth": "Do not provide a Password for IP Authentication",
    "invalid_password_lessthan_8characters_long": "This is not a valid password (Less than 8 characters long)",
    "invalid_password_missing_uppercase": "This is not a valid password (Missing upper case character)",
    "invalid_password_missing_lowercase": "This is not a valid password (Missing lower case character)",
    "invalid_password_ilegal_characters": "This is not a valid password (Allowed characters: Alphanumeric and ! # $ % & / ( ) = ? * [ ] _ : . , { } + -)",
    "invalid_password_missing_number": "This is not a valid password (Missing a number)",
    "invalid_pause": "This is not a valid Pause",
    "invalid_payment": "This is not a valid Payment",
    "invalid_phonebook": "This is not a valid Phonebook",
    "invalid_phonenumber": "This is not a valid Phone Number",
    "invalid_pin": "This is not a valid PIN",
    "invalid_playinstructions": "This is not a valid PlayInstructions Should be: u/su",
    "invalid_priority": "This is not a valid Priority",
    "invalid_protocol": "This is not a valid Protocol",
    "invalid_province": "This is not a valid Province",
    "invalid_quantity": "This is not a valid quantity",
    "invalid_query": "This is not a valid Query",
    "invalid_queue": "This is not a valid Queue",
    "invalid_recording": "This is not a valid recording",
    "invalid_report_hold_time_agent": "This is not a valid Report hold time agent",
    "invalid_resellerclient": "This is not a valid Reseller Client",
    "invalid_resellernextbilling": "This is not a valid Reseller Next Billing date, date should not be set in the past.",
    "invalid_resellerpackage": "This is not a valid Reseller Package",
    "invalid_response_timeout": "This is not a valid ResponseTimeOut",
    "invalid_retry_timer": "This is not a valid Retry timer",
    "invalid_ringgroup": "This is not a valid Ring group",
    "invalid_ring_inuse": "This is not a valid Ring in use value",
    "invalid_route": "This is not a valid Route",
    "invalid_routing_header": "This is not a valid Routing header Should be: account/vm/fwd",
    "invalid_saycallerid": "This is not a valid SayCallerID Should be: yes/no",
    "invalid_saytime": "This is not a valid SayTime Should be: yes/no",
    "invalid_security_code": "This is not a valid Security Code. Should be alphanumeric.",
    "invalid_serverpop": "This is not a valid Server POP",
    "invalid_setup": "This is not a valid Setup Fee",
    "invalid_sipuri": "This is not a valid SIPURI",
    "invalid_sms": "This is not a valid SMS",
    "invalid_sms_forward": "This is not a valid SMS forward",
    "invalid_skippassword": "This is not a valid skippassword Should be: 1/0 - or - yes/no",
    "invalid_speed_dial": "This is not a valid Speed Dial",
    "invalid_starthour": "This is not a valid Start Hour",
    "invalid_startminute": "This is not a valid Start Minute",
    "invalid_state": "This is not a valid State",
    "invalid_strategy": "This is not a valid Ring Strategy",
    "invalid_thankyou_for_your_patience": "This is not a valid Thankyou for your patience value",
    "Invalid_threshold": "This is not a valid Threshold Amount. The Threshold Amount should be between 1 and 250",
    "invalid_timecondition": "This is not a valid Time Condition",
    "invalid_timeout": "This is not a valid timeout",
    "invalid_timerange": "This is not a valid Timer Range",
    "invalid_timezone": "This is not a valid Timezone CDR and resellerCDR: Must be numeric Voicemail: Values from getTimezone",
    "invalid_type": "This is not a valid Type",
    "invalid_to_number": "This is not a valid destination number",
    "invalid_username": "This is not a valid Username",
    "invalid_voice_announcement": "This is not a valid Voice announce",
    "invalid_voicemailsetup": "This is not a valid voicemail",
    "invalid_wrapup_time": "This is not a valid Wrapup time",
    "invalid_weekdayend": "This is not a valid Week End",
    "invalid_weekdaystart": "This is not a valid Week Start",
    "invalid_priority_weight": "This is not valid weight/priority value",
    "invalid_urgent": "This is not valid urgent value",
    "ip_not_enabled": "This IP is not enabled for API use",
    "limit_reached": "You have reached the maximum number of messages allowed per day. - SMS limit using the API. - Fax limit applies using any method.",
    "max_phonebook": "Your account is limited to 8 SIP, IAX or SIP URI members",
    "members_exceeded": "You have reached the maximum allowed entries for the Phonebook",
    "message_not_found": "The voicemail message was not found",
    "method_maintenance": "This API method is under maintenance",
    "mismatch_email_confirm": "e-mail confirm does not match with e-mail",
    "mismatch_password_confirm": "Pasword confirm does not match with Password",
    "missing_account": "Account was not provided",
    "missing_address": "Address was not provided",
    "missing_agent_ring_timeout": "Agent ring time out was not provided",
    "missing_allowedcodecs": "Allowed Codecs were not provided",
    "missing_attachmessage": "AttachMessage was not provided",
    "missing_authtype": "Auth Type was not provided",
    "missing_balancemanagement": "BalanceManagemente was not provided",
    "missing_billingtype": "Billing Type was not provided",
    "missing_callback": "Callback was not provided",
    "missing_callerid": "CallerID was not provided",
    "missing_carrier": "Carrier was not provided",
    "missing_charge": "Charge was not provided.",
    "missing_choices": "Choices was not provided",
    "missing_city": "City was not provided",
    "missing_client": "Client was not provided",
    "missing_cnam": "CNAM was not provided",
    "missing_codec": "Codec was not provided",
    "missing_country": "Country was not provided",
    "missing_countryid": "Country ID was not provided",
    "missing_credentials": "Username or Password was not provided",
    "missing_delay_before": "DelayBefore was not provided",
    "missing_deletemessage": "DeleteMessage was not provided",
    "missing_description": "Description was not provided",
    "missing_devicetype": "Device Type was not provided",
    "missing_dialtime": "Dialtime was not provided",
    "missing_did": "DID was not provided",
    "missing_digits": "Digits were not provided",
    "missing_digit_timeout": "DigitTimeOut was not provided",
    "missing_disa": "DISA was not provided",
    "missing_dtmfmode": "DTMF Mode was not provided",
    "missing_email": "e-mail was not provided",
    "missing_email_confirm": "e-mail confirm was not provided",
    "missing_enable": "Enable was not provided",
    "missing_endhour": "End Hour was not provided",
    "missing_endminute": "End Minute was not provided",
    "missing_failover_busy": "Failover Busy was not provided",
    "missing_failover_noanswer": "Failover NoAnswer was not provided",
    "missing_failover_unreachable": "Failover Unreachable was not provided",
    "missing_file": "File was not provided",
    "missing_filter": "Filter was not provided",
    "missing_firstname": "Firstname was not provided",
    "missing_folder": "Folder was not provided",
    "missing_forwarding": "Forwarding was not provided",
    "missing_id": "ID was not provided",
    "missing_if_announce_position_enabled_report_estimated_hold_time": "If announce position enabled report estimated hold time type was not provided",
    "missing_internationalroute": "International Route was not provided",
    "missing_ip": "You need to provide an IP if you select IP Authentication Method",
    "missing_ip_h323": "You must enter an IP Address for H.323",
    "missing_ivr": "IVR was not provided",
    "missing_join_when_empty": "JoinWhenEmpty type was not provided",
    "missing_language": "Language was not provided",
    "missing_lastname": "Lastname was not provided",
    "missing_leave_when_empty": "LeaveWhenEmpty type was not provided",
    "missing_listened": "Listened code was not provided",
    "missing_location": "Location was not provided",
    "missing_lockinternational": "Lock International was not provided",
    "missing_mailbox": "Mailbox was not provided",
    "missing_members": "You need at least 1 member to create a ring group",
    "missing_member": "Member was not provided",
    "missing_message_num": "Voicemail message number was not provided",
    "missing_method": "Method must be provided when using the REST/JSON API",
    "missing_minute": "Minute Rate was not provided",
    "missing_monthly": "Monthly Fee was not provided",
    "missing_musiconhold": "Music on Hold was not provided",
    "missing_name": "Name was not provided",
    "missing_nat": "NAT was not provided",
    "missing_number": "Number was not provided",
    "missing_params": "Required parameters were not provided",
    "missing_package": "Package was not provided",
    "missing_password": "Password was not provided",
    "missing_password_confirm": "Password Confirm was not provided",
    "missing_payment": "Payment was not provided.",
    "missing_phonebook": "Phonebook was not provided",
    "missing_phonenumber": "Phone Number was not provided",
    "missing_pin": "PIN was not provided",
    "missing_playinstructions": "PlayInstructions was not provided",
    "missing_priority": "Priority was not provided",
    "missing_protocol": "Protocol was not provided",
    "missing_province": "Province was not provided",
    "missing_query": "Query was not provided",
    "missing_recording": "Recording was not provided",
    "missing_report_hold_time_agent": "Report hold time agent was not provided",
    "missing_resellerclient": "Provide a Reseller Client or don't provide a Reseller Package",
    "missing_resellerpackage": "Provide a Reseller Package or don't provide a Reseller Client",
    "missing_response_timeout": "ResponseTimeOut was not provided",
    "missing_ringgroup": "Ring group was not provided",
    "missing_ring_inuse": "Ring in use was not provided",
    "missing_ring_strategy": "Ring strategy was not provided",
    "missing_route": "Route was not provided",
    "missing_routing": "Routing was not provided",
    "missing_saycallerid": "SayCallerID was not provided",
    "missing_saytime": "SayTime was not provided",
    "missing_serverpop": "Server POP was not provided",
    "missing_setup": "Setup Fee was not provided",
    "missing_sipuri": "SIPURI was not provided",
    "missing_sms": "SMS was not provided",
    "missing_skippassword": "SkipPassword was not provided",
    "missing_speed_dial": "Speed Dial was not provided",
    "missing_starthour": "Start Hour was not provided",
    "missing_startminute": "Start Minute was not provided",
    "missing_state": "State was not provided",
    "missing_thankyou_for_your_patience": "Thankyou for your patience was not provided",
    "missing_timecondition": "Time Condition was not provided",
    "missing_timeout": "Timeout was not provided",
    "missing_timezone": "Timezone was not provided",
    "missing_type": "Type was not provided",
    "missing_urgent": "Urgent code was not provided",
    "missing_uri": "URI was not provided",
    "missing_username": "Username was not provided",
    "missing_voicemailsetup": "Voice mail setup was not provided",
    "missing_weekdayend": "Week End was not provide",
    "missing_weekdaystart": "Week Start was not provided",
    "missing_priority_weight": "Priority/Weight was not provided",
    "missing_zip": "Zip Code was not provided",
    "moving_fail": "The Fax Message was not moved",
    "non_sufficient_funds": "Your account does not have sufficient funds to proceed",
    "no_account": "There are no accounts",
    "no_base64file": "File not encoded in base64",
    "no_callback": "There are not Callbacks",
    "no_callstatus": "No Call Status was provided. One of the following parameters needs to be set to 1: answered, noanswer, busy, failed",
    "no_cdr": "There are no CDR entries for the filter",
    "no_change_billingtype": "Imposible change DID billing plan",
    "no_client": "There are no Clients",
    "no_did": "There are no DIDs",
    "no_disa": "There are no DISAs",
    "no_filter": "There are no Filters",
    "no_forwarding": "There was no Forwarding",
    "no_ivr": "There are no ivr",
    "no_mailbox": "There are no Mailboxes",
    "no_message": "There are no Fax Message(s)",
    "no_messages": "There are no Voicemail Message(s)",
    "no_member": "There are no Static Members",
    "no_numbers": "There are no Fax Numbers",
    "no_package": "There are no Packages",
    "no_phonebook": "There are no Phonebook entries",
    "no_queue": "There are no Queue entries",
    "no_rate": "There are no Rates",
    "no_recording": "There are no recordings",
    "no_ringgroup": "There are no Ring groups",
    "no_sipuri": "There are no SIP URIs",
    "no_sms": "There are no SMS messages",
    "no_timecondition": "There are no Time Conditions",
    "order_failed": "The order wasn't completed.",
    "provider_outofservice": "One of our providers is out of service",
    "recording_in_use_did": "You have a DID using this Recording",
    "recording_in_use_queue": "You have a Calling Queue using this Recording",
    "recording_in_use_ivr": "You have an IVR using this Recording",
    "recording_in_use_caller_id_filtering": "You have a Caller ID Filtering using this Recording",
    "recording_in_use_caller_timecondition": "You have a Time Condition using this Recording",
    "repeated_ip": "You already have a Subaccount using this IP and Protocol",
    "reserved_ip": "This is a reserved IP used by VoIP.ms or other Companies",
    "same_did_billingtype": "The Billing Type provided and DID billing type are the same",
    "sipuri_in_phonebook": "This SIPURI can't be deleted, it is mapped in the phonebook",
    "sent_fail": "The Fax Message it wasn't send.",
    "sms_toolong": "The SMS message exceeds 160 characters",
    "sms_failed": "The SMS message was not sent",
    "tls_error": "Theres was a TLS error, please try later.",
    "Unable_to_purchase": "Unable to purchase DIDs",
    "unavailable_info": "The information you requested is unavailable at this moment",
    "unsifficient_stock": "Theres no sufficient stock to complete the order.",
    "used_description": "You already have a record with this Description",
    "used_extension": "You already have a subaccount using this extension",
    "used_filter": "You already have a record with this Filter",
    "used_ip": "There is already another customer using this IP Address",
    "used_name": "You already have an entry using this name",
    "used_number": "You already have a record with this Number",
    "used_speed_dial": "You have an entry with this Speed Dial",
    "used_username": "You already have a subaccount using this Username.",
    "weak_password": "This Password is too weak or too common",
}
