# Ref: https://github.com/youtube/api-samples/blob/master/python/search.py
# Ref: https://gist.github.com/slowkow/7a7f61f495e3dbb7e3d767f97bd7304b
# Ref: https://www.geeksforgeeks.org/youtube-mediaaudio-download-using-python-pafy/

import os
import re
import sys
import pafy
import config
import argparse
from termcolor import colored
from simple_term_menu import TerminalMenu
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


def remove_emoji(string):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002500-\U00002BEF"  # chinese char
                               u"\U00002702-\U000027B0"
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               u"\U0001f926-\U0001f937"
                               u"\U00010000-\U0010ffff"
                               u"\u2640-\u2642"
                               u"\u2600-\u2B55"
                               u"\u200d"
                               u"\u23cf"
                               u"\u23e9"
                               u"\u231a"
                               u"\ufe0f"  # dingbats
                               u"\u3030"
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)


def search_video_yt(options):
    youtube = build(config.YT_API_SERVICE_NAME,
                    config.YT_API_VERSION,
                    developerKey=config.DEVELOPER_KEY)

    search_response = youtube.search().list(q=options.q,
                                            part='id, snippet',
                                            maxResults=int(options.max_results) + 1)\
                                      .execute()
    videos = []
    videos_id = []

    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            videos.append(search_result["snippet"]["title"])
            videos_id.append(search_result["id"]["videoId"])

    video_titles_without_emojis = []

    for video in videos:
        removing_emoji = remove_emoji(video)
        video_titles_without_emojis.append(removing_emoji)

    print(colored("Choose your video:", 'grey', 'on_white'))

    terminal_menu = TerminalMenu(video_titles_without_emojis)
    menu_entry_index = terminal_menu.show()

    return videos_id[menu_entry_index]


def download_video(video_id):
    myvid = pafy.new(config.LINK + video_id)
    print("Downloading audio from video...")
    bestaudio = myvid.getbestaudio()
    bestaudio.download()
    print("File downloaded successfully.")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--q', help='What do you want to search? \
                        Ex:"music to relax"',
                        default='Youtube')
    parser.add_argument('--max-results', help='Max results',
                        default=config.MAX_RESULTS)
    args = parser.parse_args()

    try:
        download_video(search_video_yt(args))
    except HttpError as e:
        print('An HTTP error %d occurred:\n%s' % (e.resp.status, e.content))
