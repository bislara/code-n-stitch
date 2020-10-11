import requests
import hashlib
import sys
# import argparse
from pyfiglet import Figlet  # pip install pyfiglet
from termcolor import colored # pip install termcolor


usage = """
[*] usage: pswpwner.py [password ... [single password] or [multiple password] or [txt file]]
[*] Note: only txt files can be used
"""


def api_data_request(query):
    # query the api with the first5 of paswd hash
    url = 'https://api.pwnedpasswords.com/range/' + query
    try:
        response = requests.get(url)
    except requests.exceptions.ConnectionError as e:
        print(f"Error fetching from the internet! check your internet connection and try again\
                \n{e}")
        quit()
    if response.status_code != 200:
        raise RuntimeError(f'error fetching {query}: please check status code')
    return response


def get_psw_leak_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        # get the particular hash with tail matching hash-to-check
        if h == hash_to_check:
            return count
    return 0


def check_pwnage(password):
    # hash the provided password
    hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5, tail = hash[:5], hash[5:]
    # the api will return a list of pswds that has their hash starting with first5
    res = api_data_request(first5)
    return get_psw_leak_count(res, tail)


def main(args):
    for password in args:
        count = check_pwnage(password.rstrip())
        if count:
            print(colored(f'[x] {password} ->\t{count}', 'red'))
        else:
            print(colored(f'[+] {password} ->\tNo Leaks', 'green'))
    return 'done!'


def handle_arg(args):
    if len(args) == 2 and args[1].endswith('.txt'):
        sys.exit(main(open(sys.argv[1], 'r')))
    if len(args) > 1:
        sys.exit(main(args[1:]))
    else:
        print(usage)


if __name__ == '__main__':
    cli_fig = Figlet(font='slant')
    print(cli_fig.renderText("PSW-Leak"))
    handle_arg(sys.argv)