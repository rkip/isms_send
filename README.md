send_sms
========

One module and two scripts for sending and querying SMS messages 
through a MutltiTech SMS gateway. This is my way of learning 
python while trying to do something useful.

send_sms.py
-----------

Send a SMS message through the HTTP API.


Usage: send_sms.py [options]

Options:
  -h, --help            show this help message and exit
  -m MESSAGE, --message=MESSAGE
                        message to text
  -p PHONE, --phone=PHONE
                        phone number to text message to
  -H HOST, --Host=HOST  IP address of SMS Gateway
  -P PORT, --Port=PORT  Port number of SMS Gateway's HTTP API
  -U USER, --User=USER  Username for SMS Gateway
  -C CREDENTIAL, --Credential=CREDENTIAL
                        Password for SMS Gateway

query_sms_id.py
---------------

Once you send a SMS message you can query the returned ID to 
learn its status.


Usage: query_sms_id.py [options]

Options:
  -h, --help            show this help message and exit
  -i ID, --id=ID        message ID to query
  -H HOST, --Host=HOST  IP address of SMS Gateway
  -P PORT, --Port=PORT  Port number of SMS Gateway's HTTP API
  -U USER, --User=USER  Username for SMS Gateway
  -C CREDENTIAL, --Credential=CREDENTIAL
                        Password for SMS Gateway
