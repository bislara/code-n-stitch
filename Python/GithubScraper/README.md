# Github profile scraper
## Author : <a href="https://www.github.com/saisumanthkumar">sai sumanth kumar</a>

## Description :
On sending the username as a parameter in terminal this program scrap the details of that github user.And If needed deatils can be saved to a file.
<br>
<img src="/assets/1.png" alt="Image of scraped data" />

<pre>
#### Folder Structure :

        /Profiles
        │
        ├── /user1
        │    │
        │    └── user1.txt (user details)
        │
        ├── /user2
        │    │
        │    └── user2.txt (user details)
        .
        .
        .
</pre>

## Installation :

1. Fork this repo
2. change the current directory to working directory (In my case it is desktop)
``` bash
cd desktop
```
3. clone the project to our local machine
``` bash
git clone https://github.com/<YOUR USERNAME>GithubScraper.git
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
 
## How to use :

1.  On completeing the above installation, Now open Your terminal and type

``` bash
python .\scraper.py <USERNAME>
```
2. <p style="font-family:sansserif">It shows all details of that user in terminal.</p>
<img src="/assets/5.png" />

3. <p> Also asks, whether are you wishing to save the file</p>
<img src="/assets/2.png" />

4. <p>Folder structure</p>
<img src="/assets/3.png" />

5. The saved text file 
<img src="/assets/4.png" />
