from selenium import webdriver
import requests
import os
import hashlib
from PIL import Image
import time
import io

def get_image_urls(wd:webdriver, search_url):
    def scroll_to_end(wd):
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")


    wd.get(search_url)
    time.sleep(2)
    image_urls = []
    count = 0
    time.sleep(15)
    scroll_to_end(wd)
    tmp = ['key']
    # scroll till there is load more button
    while(len(tmp)!=0):
        tmp = wd.find_elements_by_class_name("loadMore")
        time.sleep(15)
        thumbnail_results = wd.find_elements_by_class_name("image-placeholder")
        num_results = len(thumbnail_results)
        print(f"Found {num_results} search result. Getting source of {num_results}:..")
        
        for img in thumbnail_results:
            count += 1
            img_link = img.get_attribute('src')
            print(f"image: {img_link}")
            img_link = img_link[:img_link.index("_d")] + ".jpeg"
            if img_link not in image_urls:
                image_urls.append(img_link)
                print(f"{count+1}:{img.get_attribute('src')}")
        tmp = wd.find_elements_by_class_name("loadMore")
        if len(tmp)!=0:
            tmp[0].click()
        scroll_to_end(wd)
    return image_urls


def persist_image(folder_path, query, url, count):
    query="dfkaj"
    try:
        image_content = requests.get(url).content

    except Exception as e:
        print(f"ERROR - Could not download {url} - {e}")

    try:
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file).convert('RGB')
        # folder_path = os.path.join(folder_path)
        if os.path.exists(folder_path):
            file_path = os.path.join(folder_path,hashlib.sha1(image_content).hexdigest()[:10] + '.jpg')
        else:
            os.mkdir(folder_path)
            file_path = os.path.join(folder_path,hashlib.sha1(image_content).hexdigest()[:10] + '.jpg')
        with open(file_path, 'wb') as f:
            image.save(f, "JPEG", quality=85)
        print(f"SUCCESS - saved {url} - as {file_path}")
    except Exception as e:
        print(f"ERROR - Could not save {url} - {e}")
    except Exception as e:
        print(f"ERROR - Could not save {url} - {e}")



if __name__ == '__main__':
    # wd = webdriver.Chrome(executable_path='/chromedriver')
    query = input("Enter query to download...")
    # add your path to chrome webdriver here
    wd = webdriver.Chrome(executable_path="/usr/lib/chromium-browser/chromedriver")
    links = get_image_urls(wd, query)
    print(f"image ulrls: {links}")
    wd.quit()
    if not os.path.exists('pics/'):
        os.makedirs("pics")
    count = 0
    for img in links:
        count += 1
        persist_image("pics/", query, img, count)    
    wd.quit()