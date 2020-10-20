from time import sleep
from instagram_private_api import Client
import argparse


def get_non_followers(username, password, my_max_following=1000):
    api = Client(username, password, timeout=30)
    print('Successfully Logged In.')
    my_account = api.username_info(username)['user']

    # Getting my following list
    my_following = api.user_following(my_account['pk'], api.generate_uuid())
    all_following = [*my_following['users']]
    print('Getting your followers...')
    sleep(2)  # mimicking the real user
    while len(my_following) < my_max_following and my_following['next_max_id']:
        next_list = api.user_following(my_account['pk'], api.generate_uuid(), max_id=my_following['next_max_id'])
        print(next_list['next_max_id'])
        all_following += next_list['users']
        sleep(2)  # mimicking the real user
        if not next_list['next_max_id']:
            break

    # Checking
    print('Checking...')
    not_following = 0
    for user in all_following:
        try:
            resp = api.user_following(user['pk'], api.generate_uuid(), query=username)
            if not resp['users']:
                print(f"@{user['username']} is not following you back")
                not_following += 1
        except:
            pass

    print(f'Total of {not_following} accounts do not follow you back')


if __name__ == '__main__':
    # Note: Remember don't use it repeatedly

    parser = argparse.ArgumentParser(
        description='Get all the accounts who do not follow you back')
    parser.add_argument('-u', '--username', required=True, help="Your username")
    parser.add_argument('-p', '--password', required=True, help="Your Password")
    parser.add_argument('-m', '--max-following-check', required=False,
                        help="Max number of account to check", type=int, default=1000)

    arguments = parser.parse_args()

    print('Starting...')
    get_non_followers(arguments.username, arguments.password, my_max_following=arguments.max_following_check)