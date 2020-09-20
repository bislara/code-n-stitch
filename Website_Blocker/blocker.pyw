import time 
from datetime import datetime as dt 
  
# change hosts path according to your OS 
hosts_path = "C:\Windows\System32\drivers\etc\hosts"

# localhost's IP 
redirect = "127.0.0.1"
  
# websites That the company want to block 
website_list = ["www.facebook.com","facebook.com", 
      "instagram.com","www.instagram.com", 
      "web.whatsapp.com","twitter.com","www.twitter.com"] 
  
while True: 
  
    # time of your work 
    if dt(dt.now().year, dt.now().month, dt.now().day,8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,16): 
       	print("Restricted time..Try after your office hours.")

        with open(hosts_path, 'r+') as file: 
            content = file.read()
             # check for the website lists
            for website in website_list: 
                if website in content: 
                    pass
                else: 
                    # mapping hostnames to your localhost IP address 
                    file.write(redirect + " " + website + "\n") 
    else: 
    	# if not working hours
        print("After office hours..Enjoy") 
        with open(hosts_path, 'r+') as file: 
            content=file.readlines() 
            file.seek(0) 
            for line in content: 
                if not any(website in line for website in website_list): 
                    file.write(line) 
  
            # removing hostnmes from host file 
            file.truncate() 
  
    time.sleep(5) 