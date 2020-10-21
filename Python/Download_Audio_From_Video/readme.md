## How it works?

The application makes use of the Youtube Data API to search and list videos, gives the user an established number of options and the user can browse through them (using the UP and DOWN arrows, to choose use ENTER). After that, the Pafy library is used to download the audio of the chosen video in the highest quality and format.

## How to Setup

1) You must obtain an API key. This link has the step by step how to do this:
https://www.slickremix.com/docs/get-api-key-for-youtube/

2) With the API key in hands open the config.py file and replace the value of the DEVELOPER_KEY variable with your own key.

3) Please install the packages so you can use the application by using the command:
```bash
pip install -r requirements.txt
```
## How execute the script

```bash
python script.py 
```
<img src="https://raw.githubusercontent.com/gudeliauskaspam/code-n-stitch/1-download-audio-from-youtube-video/Python/Download_Audio_From_Video/images/1.png">

Arguments:

usage: script.py [-h] [--q Q] [--max-results MAX_RESULTS]

optional arguments:
  -h, --help            		show this help message and exit
  --q Q                 		What do you want to search? Ex:"music to relax" (Default = "Youtube")
  --max-results MAX_RESULTS		Max results (Default = 50)

<img src="https://raw.githubusercontent.com/gudeliauskaspam/code-n-stitch/1-download-audio-from-youtube-video/Python/Download_Audio_From_Video/images/2.png">

Tested in Python 3.6.9.
All code references that were used are in the start of script.py file.
