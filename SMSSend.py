#!/usr/bin/python

import re
import httplib
import urllib

isms_status_codes = {   '0' : 'Done',
                        '1' : 'Done with error',
                        '2' : 'In progress',
                        '3' : 'Request received',
                        '4' : 'Error',
                        '5' : 'Message ID not found',
                        '6' : 'Distributed to slave',
                        '7' : 'Distribution resulted in error',
                        '8' : 'Distributed among many slaves',
                        '9' : 'API is canceled'}

isms_error_codes = {'601' : 'Authentication failed',
                    '602' : 'Parse error',
                    '603' : 'Invalid Category',
                    '604' : 'SMS message size is greater then 160 chars',
                    '605' : 'Recipient overflow',
                    '606' : 'Invalid recipient',
                    '607' : 'No recipient',
                    '608' : 'Multimodem iSMS is busy, cannot accept this request',
                    '609' : 'Timeout waiting for TCP API request',
                    '610' : 'Unknown action trigger',
                    '611' : 'Error in broadcast trigger',
                    '612' : 'System error - memory allocation failure',
                    '613' : 'Invalid modem index',
                    '614' : 'Invalid device model number',
                    '615' : 'Invalid encoding type',
                    '616' : 'Invalid time/date input',
                    '617' : 'Invalid count input',
                    '618' : 'Service not available',
                    '619' : 'Invalid addressee',
                    '620' : 'Invalid priority value',
                    '621' : 'Invalid SMS text'}
                
def send_msg(host, port, user, password, phone_number, message):
    url = '/sendmsg?user=' + user + '&passwd=' + password + '&cat=1&to="' + phone_number + '"&text=' + message
    query_result = send_html_request(host, port, url)
    m = re.match(r"ID: (?P<id>\d+)", query_result)
    return m.group('id')

def query_msg_status(host, port, user, password, message_id):
    url = '/querymsg?user=' + user + '&passwd=' + password + '&apimsgid=' + message_id
    query_result = send_html_request(host, port, url)
    m = re.match(r"ID:\s+(?P<id>\d+)\s+(?P<result>\D+):\s+(?P<result_code>\d+)", query_result)
    if m.group('result') == 'Status':
        print 'ID: ' + message_id + ': ' + isms_status_codes[m.group('result_code')]
    elif m.group('result') == 'Err':
        print 'ID: ' + message_id + ': ' + isms_error_codes[m.group('result_code')]
    else:
        print 'could not parse result: ' + query_result

def send_html_request(host, port, url):
    try:
        conn = httplib.HTTPConnection(host, port, timeout=5)
        conn.request('GET', urllib.quote(url))
        response = conn.getresponse()
    except Exception as e:
        raise Exception('Connection Error: %s' % e)
    finally:
        conn.close()

    if response.status != 200:
        raise ValueError("problem : the query returned %s because %s" % (res.status, res.reason))

    return response.read()
