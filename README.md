![MIT license](https://img.shields.io/badge/licence-MIT-blue.svg)
![Stable](https://img.shields.io/badge/status-stable-green.svg)

# python-voipms

Python client for v1 of voip.ms REST API using requests >=
2.7.0.

## Getting Started

### Installation

This client is hosted at PyPi under the name `voipms`, to install
it, simply run

`pip install voipms`

### History

Up to date with features listed thru 2/20/2017.

### Initialization

Go to your the voip.ms customer portal go to the API config page (Main Menu > SOAP and REST/JSON API)
- `YOUR_USERNAME` is your voip.ms username
- Set `YOUR_PASSWORD`
- Activate the API
- Set the IP address of your development server

    from voipms import VoipMs

    client = VoipMs('YOUR_USERNAME', 'YOUR_PASSWORD')


### Examples

    # return allowed IPs
    client.general.get_ip()

    # returns a specific allowed codec
    client.accounts.get_allowed_codecs(codec="ulaw")

## API Structure

All endpoints follow the structure listed in the official voip.ms API
v1 documentation. The structure will be listed below and then the
individual methods available after.

    VoipMs
    +- General
    |   +- Get
    +- Accounts
    |   +- Create
    |   +- Delete
    |   +- Get
    |   +- Set
    +- Calls
    |   +- Get
    +- Clients
    |   +- Add
    |   +- Get
    |   +- Set

### General

#### Get

    client.general.get.balance(advanced=False)
    client.general.get.countries(country=None)
    client.general.get.ip()
    client.general.get.languages(language=None)
    client.general.get.servers_info(server_pop=None)
    client.general.get.transaction_history(date_from, date_to)

### Accounts

#### Create
    
    client.accounts.create.sub_account(username, password, protocol, auth_type, device_type,
                                       lock_international, international_route, music_on_hold,
                                       allowed_codecs, dtmf_mode, nat, **kwargs)

#### Delete

    client.accounts.delete.sub_account(account_id)

#### Get

    client.accounts.get.allowed_codecs(codec=None)
    client.accounts.get.auth_types(auth_type=None)
    client.accounts.get.device_types(device_type=None)
    client.accounts.get.dtmf_modes(dtmf_mode=None)
    client.accounts.get.lock_international(lock_international=None)
    client.accounts.get.music_on_hold(music_on_hold=None)
    client.accounts.get.nat(nat=None)
    client.accounts.get.protocols(protocol=None)
    client.accounts.get.registration_status(account)
    client.accounts.get.report_estimated_hold_time(time_type=None)
    client.accounts.get.routes(route=None)
    client.accounts.get.sub_accounts(account=None)

#### Set

    client.accounts.set.sub_account(account_id, password, auth_type, device_type,
                                    lock_international, international_route, music_on_hold,
                                    allowed_codecs, dtmf_mode, nat, **kwargs)

### Calls

#### Get

    client.calls.get.call_accounts(client=None)
    client.calls.get.call_billing(self)
    client.calls.get.call_types(client=None)
    client.calls.get.cdr(date_from, date_to, timezone,
                         answered=False, noanswer=False, busy=False,
                         failed=False, **kwargs)
    client.calls.get.rates(package, query)
    client.calls.get.termination_rates(route, query)
    client.calls.get.reseller_cdr(date_from, date_to, client, timezone,
                                  answered=False, noanswer=False, busy=False,
                                  failed=False, **kwargs)

### Clients

#### Add

    client.clients.add.charge(client, charge, description=None, test=False)
    client.clients.add.client(firstname, lastname, address, city, state, country,
                              zip_code, phone_number, email, confirm_email, password,
                              confirm_password, **kwargs)
    client.clients.add.payment(client, payment, description=None, test=False)

#### Get

    client.clients.get.balance_management(balance_management=None)
    client.clients.get.charges(client)
    client.clients.get.client_packages(client)
    client.clients.get.clients(client=None)
    client.clients.get.client_threshold(client)
    client.clients.get.deposits(client)
    client.clients.get.packages(package=None)
    client.clients.get.reseller_balance(client)

#### Set

    client.clients.set.client(client, email, password, firstname,
                              lastname, phone_number, **kwargs)
    client.clients.set.client_threshold(client, threshold, email=None)


### Dids

    client.dids.back_order_did_can(quantity, province, ratecenter, routing, 
                                   pop, dialtime, cnam, billing_type, **kwargs)
    client.dids.back_order_did_usa(quantity, state, ratecenter, routing, pop, 
                                   dialtime, cnam, billing_type, **kwargs)
    client.dids.cancel_did(did, **kwargs)
    client.dids.connect_did(did, account, monthly, setup, minute, **kwargs)
    client.dids.del_callback(callback)
    client.dids.del_caller_id_filtering(filtering)
    client.dids.del_client(client)
    client.dids.del_disa(disa)
    client.dids.delete_sms(sms_id)
    client.dids.del_forwarding(forwarding)
    client.dids.del_ivr(ivr)
    client.dids.del_phonebook(phonebook)
    client.dids.del_queue(queue)
    client.dids.del_recording(recording)
    client.dids.del_ring_group(ringgroup)
    client.dids.del_sip_uri(sipuri)
    client.dids.del_static_member(member, queue)
    client.dids.del_time_condition(timecondition)
    client.dids.get_callbacks(callback=None)
    client.dids.get_caller_id_filtering(filtering=None)
    client.dids.get_did_countries(international_type, country_id=None)
    client.dids.get_carriers(carrier=None)
    client.dids.get_dids_can(province, ratecenter=None)
    client.dids.get_dids_info(client=None, did=None)
    client.dids.get_dids_international_geographic(country_id)
    client.dids.get_dids_international_national(country_id)
    client.dids.get_dids_international_toll_free(country_id)
    client.dids.get_dids_usa(state, ratecenter=None)
    client.dids.get_disas(disa=None)
    client.dids.get_forwardings(forwarding=None)
    client.dids.get_international_types(international_type=None)
    client.dids.get_ivrs(ivr=None)
    client.dids.get_join_when_empty_types(join_type=None)
    client.dids.get_phonebook(phonebook=None, name=None)
    client.dids.get_portability(did)
    client.dids.get_provinces()
    client.dids.get_queues(queue=None)
    client.dids.get_rate_centers_can(province)
    client.dids.get_rate_centers_usa(state)
    client.dids.get_recordings(recording=None)
    client.dids.get_recording_file(recording)
    client.dids.get_ring_groups(ringgroup=None)
    client.dids.get_ring_strategies(strategy=None)
    client.dids.get_sip_uris(sipuri=None)
    client.dids.get_sms(**kwargs)
    client.dids.get_states()
    client.dids.get_static_members(queue, member=None)
    client.dids.get_time_conditions(timecondition=None)
    client.dids.get_voicemail_setups(voicemailsetup=None)
    client.dids.get_voicemail_attachment_formats(email_attachment_format=None)
    client.dids.order_did(did, routing, pop, dialtime, cnam, billing_type, **kwargs)
    client.dids.order_did_international_geographic(location_id, quantity, routing,
                                                   pop, dialtime, cnam, billing_type, **kwargs)
    client.dids.order_did_international_national(location_id, quantity, routing,
                                                 pop, dialtime, cnam, billing_type, **kwargs)
    client.dids.order_did_international_toll_free(location_id, quantity, routing, pop,
                                                  dialtime, cnam, billing_type, **kwargs)
    client.dids.order_did_virtual(digits, routing, pop, dialtime, cnam, billing_type, **kwargs)
    client.dids.order_toll_free(did, routing, pop, dialtime, cnam, billing_type, **kwargs)
    client.dids.order_vanity(did, routing, pop, dialtime, cnam, billing_type, carrier, **kwargs)
    client.dids.search_dids_can(search_type, query, province=None)
    client.dids.search_dids_usa(search_type, query, state=None)
    client.dids.search_toll_free_can_us(search_type=None, query=None)
    client.dids.search_toll_free_usa(search_type=None, query=None)
    client.dids.search_vanity(search_type, query)
    client.dids.send_sms(did, dst, message)
    client.dids.set_callback(description, number, delay_before, response_timeout, digit_timeout, **kwargs)
    client.dids.set_caller_id_filtering(callerid, did, routing, **kwargs)
    client.dids.set_did_billing_type(did, billing_type)
    client.dids.set_did_info(did, routing, pop, dialtime, cnam, billing_type, **kwargs)
    client.dids.set_did_pop(did, pop)
    client.dids.set_did_routing(did, routing)
    client.dids.set_did_voicemail(did, voicemail=None)
    client.dids.set_disa(name, pin, digit_timeout, **kwargs)
    client.dids.set_forwarding(phone_number, **kwargs)
    client.dids.set_ivr(name, recording, timeout, language, voicemailsetup, choices, ivr=None)
    client.dids.set_phonebook(name, number, **kwargs)
    client.dids.set_queue(queue_name, queue_number, queue_language, priority_weight, report_hold_time_agent,
                          join_when_empty, leave_when_empty, ring_strategy, ring_inuse, **kwargs)
    client.dids.set_recording(file, name, recording=None)
    client.dids.set_ring_group(name, members, voicemail, **kwargs)
    client.dids.set_sip_uri(uri, **kwargs)
    client.dids.set_sms(did, enable, **kwargs)
    client.dids.set_static_member(queue, member_name, priority, **kwargs)
    client.dids.set_time_condition(name, routing_match, routing_nomatch, starthour, startminute,
                                   endhour, endminute, weekdaystart, weekdayend, timecondition=None)
    client.dids.unconnect_did(did)

### Fax

    client.fax.cancel_fax_number(fax_id, test=None)
    client.fax.delete_fax_message(fax_id, test=None)
    client.fax.del_email_to_fax(fax_id, test=None)
    client.fax.del_fax_folder(folder_id, test=None)
    client.fax.get_fax_provinces(province=None)
    client.fax.get_fax_states(state=None)
    client.fax.get_fax_rate_centers_can(province)
    client.fax.get_fax_rate_centers_usa(state)
    client.fax.get_fax_numbers_info(did=None)
    client.fax.get_fax_numbers_portability(did)
    client.fax.get_fax_messages(**kwargs)
    client.fax.get_fax_message_pdf(fax_id)
    client.fax.get_fax_folders()
    client.fax.get_email_to_fax(fax_id=None)
    client.fax.mail_fax_message_pdf(fax_id, email)
    client.fax.move_fax_message(fax_id, folder_id, test=None)
    client.fax.order_fax_number(location, quantity, **kwargs)
    client.fax.set_fax_folder(name, **kwargs)
    client.fax.set_email_to_fax(auth_email, from_number_id, security_code, **kwargs)
    client.fax.search_fax_area_code_can(area_code)
    client.fax.search_fax_area_code_usa(area_code)
    client.fax.set_fax_number_info(did, **kwargs)
    client.fax.set_fax_number_email(did, **kwargs)
    client.fax.set_fax_number_url_callback(did, **kwargs)
    client.fax.send_fax_message(to_number, from_name, from_number, file, **kwargs)

### Voicemail
    
    client.voicemail.create_voicemail(digits, name, password, skip_password, attach_message, delete_message,
                                      say_time, timezone, say_callerid, play_instructions, language, **kwargs)
    client.voicemail.del_messages(mailbox, **kwargs)
    client.voicemail.del_voicemail(mailbox)
    client.voicemail.get_play_instructions(play_instructions=None)
    client.voicemail.get_timezones(timezone=None)
    client.voicemail.get_voicemails(mailbox=None)
    client.voicemail.get_voicemail_folders(folder=None)
    client.voicemail.get_voicemail_message_file(mailbox, folder, message_num)
    client.voicemail.get_voicemail_messages(mailbox, **kwargs)
    client.voicemail.mark_listened_voicemail_message(mailbox, folder, message_num, listened)
    client.voicemail.mark_urgent_voicemail_message(mailbox, folder, message_num, urgent)
    client.voicemail.move_folder_voicemail_message(mailbox, folder, message_num, new_folder)
    client.voicemail.send_voicemail_email(mailbox, folder, message_num, email_address)
    client.voicemail.set_voicemail(mailbox, name, password, skip_password, attach_message, delete_message,
                                   say_time, timezone, say_callerid, play_instructions, language, **kwargs)

## Support

If you are having issues, please let us know or submit a pull request.

## License

The project is licensed under the MIT License.

## Special Thanks

I was highly inspired by the mailchim3 API at https://github.com/charlesthk/python-mailchimp/.
Thanks for your nice code layout!
