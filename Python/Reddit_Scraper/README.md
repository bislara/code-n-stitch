# Description
It is reddit scraper than can be used to scrape the subreddits for some or all the post.
It saves the all the repsone json in a file named as subreddit_name.json

## Requirements
Python 3.x or higher


## Usage 
Recommended to choose subreddit name and number of submissions

```
python scraper.py oneliners 500 
```

```
https://api.pushshift.io/reddit/search/submission/?size=1000&sort=desc&sort_type=created_utc&subreddit=oneliners
100
https://api.pushshift.io/reddit/search/submission/?before=1603066327&size=1000&sort=desc&sort_type=created_utc&subreddit=oneliners
200
https://api.pushshift.io/reddit/search/submission/?before=1602679718&size=1000&sort=desc&sort_type=created_utc&subreddit=oneliners
300
https://api.pushshift.io/reddit/search/submission/?before=1602271406&size=1000&sort=desc&sort_type=created_utc&subreddit=oneliners
400
https://api.pushshift.io/reddit/search/submission/?before=1601992843&size=1000&sort=desc&sort_type=created_utc&subreddit=oneliners
500

Done, file created as oneliners.json

```