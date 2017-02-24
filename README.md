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
    +- Accounts

### General

    client.general.get_balance(advanced=False)
    client.general.get_countries(country=None)
    client.general.get_ip()
    client.general.get_languages(language=None)
    client.general.get_servers_info(server_pop=None)
    client.general.get_transaction_history(date_from, date_to)

### Accounts
    
    client.accounts.create_sub_account(username, password, protocol, auth_type, device_type,
                                       lock_international, international_route, music_on_hold,
                                       allowed_codecs, dtmf_mode, nat, **kwargs):
    client.accounts.del_sub_account(account_id)
    client.accounts.get_allowed_codecs(codec=None)
    client.accounts.get_auth_types(auth_type=None)
    client.accounts.get_device_types(device_type=None)
    client.accounts.get_dtmf_modes(dtmf_mode=None)
    client.accounts.get_lock_international(lock_international=None)
    client.accounts.get_music_on_hold(music_on_hold=None)
    client.accounts.get_nat(nat=None)
    client.accounts.get_protocols(protocol=None)
    client.accounts.get_registration_status(account)
    client.accounts.get_report_estimated_hold_time(time_type=None)
    client.accounts.get_routes(route=None)
    client.accounts.get_sub_accounts(account=None)
    client.accounts.set_sub_account(account_id, password, auth_type, device_type,
                                    lock_international, international_route, music_on_hold,
                                    allowed_codecs, dtmf_mode, nat, **kwargs)

### Calls

    client.calls.get_call_accounts(client=None)
    client.calls.get_call_billing(self)
    client.calls.get_call_types(client=None)
    client.calls.get_cdr(date_from, date_to, timezone,
                         answered=False, noanswer=False, busy=False,
                         failed=False, **kwargs)
    client.calls.get_rates(package, query)
    client.calls.get_termination_rates(route, query)
    client.calls.get_reseller_cdr(date_from, date_to, client, timezone,
                                  answered=False, noanswer=False, busy=False,
                                  failed=False, **kwargs)

### Clients

    client.clients.add_charge(client, charge, description=None, test=False)
    client.clients.add_payment(client, payment, description=None, test=False)
    client.clients.get_balance_management(balance_management=None)
    client.clients.get_charges(client)
    client.clients.get_client_packages(client)
    client.clients.get_clients(client=None)
    client.clients.get_client_threshold(client)
    client.clients.get_deposits(client)
    client.clients.get_packages(package=None)
    client.clients.get_reseller_balance(client)
    client.clients.set_client(client, email, password, firstname,
                              lastname, phone_number, **kwargs)
    client.clients.set_client_threshold(client, threshold, email=None)
    client.clients.signup_client(firstname, lastname, address, city, state, country,
                                 zip_code, phone_number, email, confirm_email, password,
                                 confirm_password, **kwargs)

## Support

If you are having issues, please let us know or submit a pull request.

## License

The project is licensed under the MIT License.

## Special Thanks

I was highly inspired by the mailchim3 API at https://github.com/charlesthk/python-mailchimp/.
Thanks for your nice code layout!
