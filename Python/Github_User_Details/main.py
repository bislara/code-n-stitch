#!/usr/bin/python
import argparse

from functions import get_user_details


DETAILS = [
    ('avatar_url', 'Avatar Url'),
    ('name', 'Name'),
    ('location', 'Location'),
    ('email', 'Email'),
    ('bio', 'Bio'),
    ('html_url', 'URL of the profile'),
    ('repos_url', 'Repos URL'),
    # GitHub Apps with the Plan user permission can get private_repos
    # ('private_repos', 'Number of private repos'),
    ('public_repos', 'Number of public repos'),
    ('followers', 'Number of followers'),
    ('following', 'Number of following'),
]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get github user details')
    parser.add_argument('-u', '--user', required=True)

    arguments = vars(parser.parse_args())

    print(f'Getting details of "{arguments["user"]}"')
    print()

    user = get_user_details(arguments['user'])
    if user:
        for key, label in DETAILS:
            print(f'{label}: {user[key]}')
    else:
        print('Invalid User')
