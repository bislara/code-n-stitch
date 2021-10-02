import sys
from datetime import datetime

import requests
import requests_cache
import reusables

requests_cache.install_cache()


class Network:
    """
    Reddit's official API has some limitations, it can a better alternative if we need to scrape much more data
    """
    BASE_PATH = 'https://api.pushshift.io/reddit/search/submission/?'

    def __init__(self):
        self.last_page = None
        self.last_ts = None
        self.subreddit = ''

    def search(self):

        # It is payload for api, get the data descending in timestamp (ie newer to lower)
        payload = {
            'subreddit': self.subreddit,
            'sort': 'desc',
            "sort_type": "created_utc",
            # 'sort_type': 'score',
            'size': '1000',
        }

        # self.last_page is only None in start of the script
        if self.last_page is not None:
            if len(self.last_page) > 0:
                # resume from where we left off at the last page
                payload["before"] = self.last_page[-1]["created_utc"]
                # print(self.last_id)
            else:
                # the last page was empty, we are past the last page, so we stop
                return []

        # In case we have a inital time stamp, then we set minimum timestamp,
        # ie only post after that timestamp will be showed
        if self.last_page is None and self.last_ts is not None:
            payload['after'] = self.last_ts

        results = requests.get(self.BASE_PATH, params=payload)
        print(results.url)

        if not results.ok:
            # something wrong happened
            raise Exception("Server returned status code {}".format(results.status_code))

        return results.json()["data"]

    def crawler(self, subreddit_name, newer_than=None, max_submissions=1000):
        """
        Crawls the reddit for data

        :return: list of submissions
        :rtype: list
        :param subreddit_name: name of subreddit to search
        :param newer_than: scrape after this timestamp
        :param max_submissions:  max numbers of submissions required

        """
        self.subreddit = subreddit_name
        self.last_ts = newer_than
        self.last_page = None
        submissions = []

        date = lambda ts: datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S  ')

        while self.last_page != [] and len(submissions) < max_submissions:
            self.last_page = self.search()
            # print(len(self.last_page))
            submissions += self.last_page
            if len(self.last_page) != 0:
                self.last_ts = self.last_page[-1]["created_utc"]
            print(len(submissions))
            # time.sleep(1)

        return submissions[:max_submissions]


n = Network()

# Inputs
subreddit_name = sys.argv[1]  # 'oneliners'
max_submission = int(sys.argv[2])  # 200 # No of post to fetch, Note some post maybe deleted or not avaible

data = n.crawler(subreddit_name, max_submissions=max_submission)

# Save the file in subreddit_name.json
reusables.save_json(data, '{}.json'.format(subreddit_name), indent=2)
print('\nDone, file created as {}.json'.format(subreddit_name))

'''
Some info about json format

full_link : is the link to the original reddit page
title : title of the reddit page
selftext:  for text in the post
url: may contain image link or video link if it ends with jpg, jpeg, png, mp4  or may contains imgur, gfycat link too


'''
