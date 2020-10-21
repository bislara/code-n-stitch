import pafy 
  
# link of the file
url = "https://www.youtube.com/watch?v=CeCm3fI61bY"
video = pafy.new(url) 

# get the video types present  
streams = video.streams 
for i in streams: 
    print(i)

# print title 
print(video.title) 
  
# print rating 
print(video.rating) 
  
# print viewcount 
print(video.viewcount) 
  
# print author & video length 
print(video.author, video.length) 
  
# Best quality
best = video.getbest() 

#   Get the resolution and extension type of the best available video
print(best.resolution, best.extension) 
  

# get best resolution of a specific format 
# set format out of(mp4, webm, flv or 3gp) 
# best = video.getbest(preftype ="3gp") 

# Download the video 
# best.download() 

# this is causing an error of quota limit exceded
# ------------------------------------------------------
# print duration, likes, dislikes & description 
# print(video.duration, video.likes, video.dislikes, video.description) 
# ------------------------------------------------------

# Download a specific format audio.
audiostreams = video.audiostreams 
for i in audiostreams: 
    print(i.bitrate, i.extension, i.get_filesize()) 

# download the audio stream  
# audiostreams[3].download() 


# Download the bestaudio
# bestaudio = video.getbestaudio() 
# bestaudio.download() 


# References:
# https://pypi.org/project/pafy/