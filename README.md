![MIT license](https://img.shields.io/badge/licence-MIT-blue.svg)
![Version](https://img.shields.io/badge/version-0.2-orange.svg)
![Unstable](https://img.shields.io/badge/status-unstable-red.svg)

# python-voipms

Python client for v1 of voip.ms REST API using requests >=
2.7.0.

## Getting Started

### Installation

This client is hosted at PyPi under the name `voipms`, to install
it, simply run

`pip install voipms`

### History

- Version 0.2.3 from 05.04.2017
    - First alpha version of this API 
    - Up to date with features listed through 20.02.2017
    - TODO:
        - Code cleanup
        - Cleanup of inner references to functions
        - Testing all functions
        - More validations of input and streamlining how to input dids (only digits or also dids with seperators)

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
    client.general.get.ip()

    # returns a specific allowed codec
    client.accounts.get.allowed_codecs(codec="ulaw")

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
    +- Dids
    |   +- Back_order
    |   +- Cancel
    |   +- Connect
    |   +- Delete
    |   +- Get
    |   +- Order
    |   +- Search
    |   +- Send
    |   +- Set
    |   +- Unconnect
    +- Fax
    |   +- Cancel
    |   +- Delete
    |   +- Get
    |   +- Mail
    |   +- Move
    |   +- Order
    |   +- Search
    |   +- Send
    |   +- Set
    +- Voicemail
    |   +- Create
    |   +- Delete
    |   +- Get
    |   +- Mark
    |   +- Move
    |   +- Send
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

#### Back_order

    client.dids.back_order.did_can(quantity, province, ratecenter, routing, 
                                   pop, dialtime, cnam, billing_type, **kwargs)
    client.dids.back_order.did_usa(quantity, state, ratecenter, routing, pop, 
                                   dialtime, cnam, billing_type, **kwargs)

#### Cancel

    client.dids.cancel.did(did, **kwargs)

#### Connect

    client.dids.connect.did(did, account, monthly, setup, minute, **kwargs)

#### Delete

    client.dids.delete.callback(callback)
    client.dids.delete.caller_id_filtering(filtering)
    client.dids.delete.client(client)
    client.dids.delete.disa(disa)
    client.dids.delete_sms(sms_id)
    client.dids.delete.forwarding(forwarding)
    client.dids.delete.ivr(ivr)
    client.dids.delete.phonebook(phonebook)
    client.dids.delete.queue(queue)
    client.dids.delete.recording(recording)
    client.dids.delete.ring_group(ringgroup)
    client.dids.delete.sip_uri(sipuri)
    client.dids.delete.static_member(member, queue)
    client.dids.delete.time_condition(timecondition)

#### Get

    client.dids.get.callbacks(callback=None)
    client.dids.get.caller_id_filtering(filtering=None)
    client.dids.get.did_countries(international_type, country_id=None)
    client.dids.get.carriers(carrier=None)
    client.dids.get.dids_can(province, ratecenter=None)
    client.dids.get.dids_info(client=None, did=None)
    client.dids.get.dids_international_geographic(country_id)
    client.dids.get.dids_international_national(country_id)
    client.dids.get.dids_international_toll_free(country_id)
    client.dids.get.dids_usa(state, ratecenter=None)
    client.dids.get.disas(disa=None)
    client.dids.get.forwardings(forwarding=None)
    client.dids.get.international_types(international_type=None)
    client.dids.get.ivrs(ivr=None)
    client.dids.get.join_when_empty_types(join_type=None)
    client.dids.get.phonebook(phonebook=None, name=None)
    client.dids.get.portability(did)
    client.dids.get.provinces()
    client.dids.get.queues(queue=None)
    client.dids.get.rate_centers_can(province)
    client.dids.get.rate_centers_usa(state)
    client.dids.get.recordings(recording=None)
    client.dids.get.recording_file(recording)
    client.dids.get.ring_groups(ringgroup=None)
    client.dids.get.ring_strategies(strategy=None)
    client.dids.get.sip_uris(sipuri=None)
    client.dids.get.sms(**kwargs)
    client.dids.get.states()
    client.dids.get.static_members(queue, member=None)
    client.dids.get.time_conditions(timecondition=None)
    client.dids.get.voicemail_setups(voicemailsetup=None)
    client.dids.get.voicemail_attachment_formats(email_attachment_format=None)

#### Order

    client.dids.order.did(did, routing, pop, dialtime, cnam, billing_type, **kwargs)
    client.dids.order.did_international_geographic(location_id, quantity, routing,
                                                   pop, dialtime, cnam, billing_type, **kwargs)
    client.dids.order.did_international_national(location_id, quantity, routing,
                                                 pop, dialtime, cnam, billing_type, **kwargs)
    client.dids.order.did_international_toll_free(location_id, quantity, routing, pop,
                                                  dialtime, cnam, billing_type, **kwargs)
    client.dids.order.did_virtual(digits, routing, pop, dialtime, cnam, billing_type, **kwargs)
    client.dids.order.toll_free(did, routing, pop, dialtime, cnam, billing_type, **kwargs)
    client.dids.order.vanity(did, routing, pop, dialtime, cnam, billing_type, carrier, **kwargs)

#### Search

    client.dids.search.dids_can(search_type, query, province=None)
    client.dids.search.dids_usa(search_type, query, state=None)
    client.dids.search.toll_free_can_us(search_type=None, query=None)
    client.dids.search.toll_free_usa(search_type=None, query=None)
    client.dids.search.vanity(search_type, query)

#### Send

    client.dids.send.sms(did, dst, message)

#### Set
 
    client.dids.set.callback(description, number, delay_before, response_timeout, digit_timeout, **kwargs)
    client.dids.set.caller_id_filtering(callerid, did, routing, **kwargs)
    client.dids.set.did_billing_type(did, billing_type)
    client.dids.set.did_info(did, routing, pop, dialtime, cnam, billing_type, **kwargs)
    client.dids.set.did_pop(did, pop)
    client.dids.set.did_routing(did, routing)
    client.dids.set.did_voicemail(did, voicemail=None)
    client.dids.set.disa(name, pin, digit_timeout, **kwargs)
    client.dids.set.forwarding(phone_number, **kwargs)
    client.dids.set.ivr(name, recording, timeout, language, voicemailsetup, choices, ivr=None)
    client.dids.set.phonebook(name, number, **kwargs)
    client.dids.set.queue(queue_name, queue_number, queue_language, priority_weight, report_hold_time_agent,
                          join_when_empty, leave_when_empty, ring_strategy, ring_inuse, **kwargs)
    client.dids.set.recording(file, name, recording=None)
    client.dids.set.ring_group(name, members, voicemail, **kwargs)
    client.dids.set.sip_uri(uri, **kwargs)
    client.dids.set.sms(did, enable, **kwargs)
    client.dids.set.static_member(queue, member_name, priority, **kwargs)
    client.dids.set.time_condition(name, routing_match, routing_nomatch, starthour, startminute,
                                   endhour, endminute, weekdaystart, weekdayend, timecondition=None)

#### Unconnect

    client.dids.unconnect.did(did)

### Fax

#### Cancel

    client.fax.cancel.fax_number(fax_id, test=None)

#### Delete

    client.fax.delete.fax_message(fax_id, test=None)
    client.fax.delete.email_to_fax(fax_id, test=None)
    client.fax.delete.fax_folder(folder_id, test=None)

#### Get

    client.fax.get.fax_provinces(province=None)
    client.fax.get.fax_states(state=None)
    client.fax.get.fax_rate_centers_can(province)
    client.fax.get.fax_rate_centers_usa(state)
    client.fax.get.fax_numbers_info(did=None)
    client.fax.get.fax_numbers_portability(did)
    client.fax.get.fax_messages(**kwargs)
    client.fax.get.fax_message_pdf(fax_id)
    client.fax.get.fax_folders()
    client.fax.get.email_to_fax(fax_id=None)

#### Mail

    client.fax.mail.fax_message_pdf(fax_id, email)

#### Move

    client.fax.move_fax_message(fax_id, folder_id, test=None)

#### Order

    client.fax.order.fax_number(location, quantity, **kwargs)

#### Set

    client.fax.search.fax_area_code_can(area_code)
    client.fax.search.fax_area_code_usa(area_code)

#### Send

    client.fax.send.fax_message(to_number, from_name, from_number, file, **kwargs)

#### Set

    client.fax.set.fax_folder(name, **kwargs)
    client.fax.set.email_to_fax(auth_email, from_number_id, security_code, **kwargs)
    client.fax.set.fax_number_info(did, **kwargs)
    client.fax.set.fax_number_email(did, **kwargs)
    client.fax.set.fax_number_url_callback(did, **kwargs)

### Voicemail

#### Create
    
    client.voicemail.create.voicemail(digits, name, password, skip_password, attach_message, delete_message,
                                      say_time, timezone, say_callerid, play_instructions, language, **kwargs)

#### Delete

    client.voicemail.delete.messages(mailbox, **kwargs)
    client.voicemail.delete.voicemail(mailbox)

#### Get

    client.voicemail.get.play_instructions(play_instructions=None)
    client.voicemail.get.timezones(timezone=None)
    client.voicemail.get.voicemails(mailbox=None)
    client.voicemail.get.voicemail_folders(folder=None)
    client.voicemail.get.voicemail_message_file(mailbox, folder, message_num)
    client.voicemail.get.voicemail_messages(mailbox, **kwargs)

#### Mark

    client.voicemail.mark.listened_voicemail_message(mailbox, folder, message_num, listened)
    client.voicemail.mark.urgent_voicemail_message(mailbox, folder, message_num, urgent)

#### Move

    client.voicemail.move.folder_voicemail_message(mailbox, folder, message_num, new_folder)

#### Send

    client.voicemail.send.voicemail_email(mailbox, folder, message_num, email_address)

#### Set

    client.voicemail.set.voicemail(mailbox, name, password, skip_password, attach_message, delete_message,
                                   say_time, timezone, say_callerid, play_instructions, language, **kwargs)

## Support

If you are having issues, please let us know or submit a pull request.

## License

The project is licensed under the MIT License.

## Special Thanks

I was highly inspired by the mailchim3 API at https://github.com/charlesthk/python-mailchimp/.
Thanks for your nice code layout!
