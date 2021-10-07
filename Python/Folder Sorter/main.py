#!/usr/bin/env python3

import os
import sys
from shutil import move


PATH = os.getcwd()
#add particular file type of file format here
folders = {"Docs":['pdf','odt', 'odf', 'doc', 'docx', 'pptx' ,'txt'],
        "Torrents":["torrent"],
        "Songs":['mp3', 'wav'],
        "Videos":["mp4",'avi','gif', 'webm', 'mkv', 'wmv'],
        "Pictures":['png', 'jpg', 'jpeg'],
        "ISO":['iso', 'ova'],
        "Zips":['gz', 'zip'],
        "Packages":['deb']}


# print(os.listdir(PATH))
files = [i for i in os.listdir(PATH) if os.path.isfile(i)]


for i in range(len(files)):
    idx = files[i].rfind('.')
    file, extension = files[i][:idx], files[i][idx+1:]
    # print(extension)
    key = ""
    #finding if extension exists in dict
    if extension in [i for v in folders.values() for i in v]:
        for tmpkey, extension1 in folders.items():
            if extension in extension1:
               key = tmpkey
            #    print(key)
               break 
            
        # move to resp folders
        if not os.path.exists(key):
            os.mkdir(key)
            move(files[i], key + "/" + files[i])
            print(f"moving file: {files[i]} to {key}")
        else:
            move(files[i], key + "/" + files[i])
            print(f"moving file: {files[i]} to {key}")