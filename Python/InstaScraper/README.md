# Instagram profile scraper
## Author : <a href="https://www.github.com/saisumanthkumar">sai sumanth kumar</a>

## Description :
Once you enter username and password , and the username of the person who's profile you need,This script creates a folder in `profile/<USERNAME>` and inside this folder there is 2 files
 - `<USERNAME>.png` - profile picture of the user
 - `<USERNAME>.txt` - User details

<pre>
#### Folder Structure :

        /Profiles
        │
        ├── /user1
        │    │
        │    ├── user1.png (profile picture)
        │    └── user1.txt (user details)
        │
        ├── /user2
        │    │
        │    ├── user2.png (profile picture)
        │    └── user2.txt (user details)
        .
        .
        .
</pre>

## Installation :
##### ` Note ` : deployed project is <a href="https://www.github.com/saisumanthkumar/InstaScraper">Here</a>
1. Fork this repo
2. change the current directory to working directory (In my case it is desktop)
``` bash
cd desktop
```
3. clone the project to our local machine
``` bash
git clone https://github.com/<YOUR USERNAME>InstaScraper.git
```
4. setup python environment
``` bash
python -m venv env
```
5. Install all requirements 
``` bash
pip install -r requirements.txt
```
6. That's it You have done, Now Let's check how to use 

`Note:Please make sure use you webdriver version of same with your chrome version`
 
## How to use :
-  Run the pyton file `python .\scraper.py` in terminal
 - Enter Your Username and password. And then creates a profile directory to store all the data
<img src="/images/1.png">

<ul>
<li>And then it shows the basic options,
<ul>
<li style="font-family:Monospace;font-weight:bold">option-1 : </li>
 -- Ask to enter a username, and then creates a folder with username and gets all the required data.
<img src="/images/2.png">

<li style="font-family:Monospace;font-weight:bold">option-2 : </li>
 -- Logout from account and stop's webdriver
<img src="/images/3.png">
</ul>
</li>
</ul>

<h2 style="font-family:Monospace;font-weight:bold">Tutorial : <p style="font-family:sansserif;font-weight:200;font-size:16px">Now let's get Cristiano Ronaldo Instagram details.</p></h2>

<img src='/images/4.png' />
<img src='/images/5.png' />
<img src='/images/6.png' />
<img src='/images/7.png' />