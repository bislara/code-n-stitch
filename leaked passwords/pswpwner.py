import requests
import hashlib
import sys
import re
import argparse
from pathlib import Path
from pprint import pprint


def api_data_request(query):
    url = 'https://api.pwnedpasswords.com/range/' + query
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(f'error fetching {query}: please check status code')
    return response


def get_psw_leak_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def check_pwnage(password):
    hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5, tail = hash[:5], hash[5:]
    res = api_data_request(first5)
    return get_psw_leak_count(res, tail)


def main(args):
    for password in args:
        count = check_pwnage(password)
        if count:
            print(f'it seems your password {password} has been pawned {count} times')
        else:
            print(f'{password} not found, carry on!')
    return 'done!'

if __name__ == '__main__':
    sys.exit(main(open(sys.argv[1], 'r')))

# create command line args and flags
# to check single password
# to check single email
# to check  multiple passwords
# to check multiple emails
# to check a list of psw's or emails
# a helper function
# better error handling
# using argsparser
# to check passwords or email or combination of passwords/ emails in a file or multiple files
# using regex, argspaser, file I/O, pathlib, pyfiglet, pprint, askpass.