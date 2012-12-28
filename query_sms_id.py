#!/usr/bin/python

import sys
import SMSSend
from optparse import OptionParser

def main():
    parser = OptionParser("usage: %prog [options]")
    parser.add_option("-i", "--id", action="store", type="string", dest="id", help="message ID to query")
    parser.add_option("-H", "--Host", action="store", type="string", dest="host", help="IP address of SMS Gateway")
    parser.add_option("-P", "--Port", action="store", default="81", type="int", dest="port", help="Port number of SMS Gateway's HTTP API")
    parser.add_option("-U", "--User", action="store", type="string", dest="user", help="Username for SMS Gateway")
    parser.add_option("-C", "--Credential", action="store", type="string", dest="credential", help="Password for SMS Gateway")
    (options, args) = parser.parse_args()

    SMSSend.query_msg_status(options.host, options.port, options.user, options.credential, options.id)
    

if __name__ == '__main__':
    main()
