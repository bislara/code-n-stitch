How it works?

The application makes use of the Youtube Data API to search and list videos, gives the user an established number of options and the user can browse through them (using the UP and DOWN arrows, to choose use ENTER). After that, the Pafy library is used to download the audio of the chosen video in the highest quality and format.

How to use?

First, you must obtain an API key. This link has the step by step how to do this:
https://www.slickremix.com/docs/get-api-key-for-youtube/

With the API key in hands open the config.py file and replace the value of the DEVELOPER_KEY variable with your own key.

usage: script.py [-h] [--q Q] [--max-results MAX_RESULTS]

optional arguments:
  -h, --help            		show this help message and exit
  --q Q                 		What do you want to search? Ex:"music to relax"
  --max-results MAX_RESULTS		Max results


Please install the following packages so you can use the application:

simple-term-menu (https://github.com/IngoMeyer441/simple-term-menu)
pafy (https://github.com/mps-youtube/pafy)
google-api-python-client (https://github.com/googleapis/google-api-python-client)
youtube_dl (https://github.com/ytdl-org/youtube-dl)
colorama (https://github.com/tartley/colorama)
termcolor (https://github.com/hfeeki/termcolor)

Tested in Python 3.6.9.

All code references that were used are in the start of script.py file.