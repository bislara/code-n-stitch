import os
import pafy
import PIL.Image
import tkinter as tk
from pafy import *
from PIL import ImageTk
from tkinter import *
from tkinter import filedialog
from tkinter import ttk

root = Tk()
root.state('zoomed')

vid = []
vformats = []
vres = []

url = tk.StringVar()
sel_res = StringVar()
sel_format = StringVar()
sel_vid_typ = StringVar()
Location = StringVar()

#Function to download the video of selected type
def DownloadVideo():
    sel_vid = sel_vid_typ.get() + ":" + sel_format.get() + "@" + sel_res.get()
    for i in vid:
        temp = str(i)
        if(temp==sel_vid):
            stream = i
            break
    stream.download()


#Function to display 
def PathSelBtn():
    pathsel_btn = Button(main_frame, text = "Select Location" ,bg="#fff000",font=('Helvetica', 14),command=PathSelector)
    pathsel_btn.place(relx=0.21,rely=0.73,relwidth=0.18,relheight=0.06)

#Function to select the path to download the video
def PathSelector():
    dir = filedialog.askdirectory()
    Location.set(str(dir))
    Loc_label.config( text = Location.get() )
    os.chdir(dir)
    get_review = Button(main_frame, text = 'DOWNLOAD VIDEO!',bg="#ff0000",foreground="white",font=('Helvetica', 14, 'bold'),command=DownloadVideo)
    get_review.place(relx=0.375,rely=0.8,relwidth=0.25,relheight=0.08)

#Function to select the resolution of the video to be downloaded
def ResolSelector():
    sel_res.set("None")
    typ = sel_vid_typ.get()
    format = sel_format.get()
    prefix = typ + ":" + format + "@"
    for i in vid:
        temp = str(i)
        if(temp[:len(prefix)]==prefix and temp[len(prefix):] not in vres):
            vres.append(temp[len(prefix):])
    #Video type selector
    vid_res_label = Label(main_frame, text="Video Resol:", bg="#080808",foreground="white",font=('Helvetica', 16, 'bold'),anchor=W,justify=LEFT)
    vid_res_label.place(relx=0.2,rely=0.66,relwidth=0.5,relheight=0.06)
    res_drop = OptionMenu( main_frame , sel_res , *vres )
    res_drop.place(relx=0.4,rely=0.66,relwidth=0.1,relheight=0.06)
    confirm_btn = Button(main_frame, text = 'Confirm',bg="#66ff00",font=('Helvetica', 14),command=PathSelBtn)
    confirm_btn.place(relx=0.52,rely=0.66,relwidth=0.1,relheight=0.06)


#Function to select the format of video
def FormatSelector():
    typ = sel_vid_typ.get()
    for i in vid:
        tstr = ""
        temp = str(i)
        if(temp[:5]==typ):
            for j in temp[6:]:
                if(j=="@" and tstr not in vformats):
                    vformats.append(tstr)
                else:
                    tstr+=j
        elif(temp[:6]==typ):
            for j in temp[7:]:
                if(j=="@" and tstr not in vformats):
                    vformats.append(tstr)
                else:
                    tstr+=j
    #Video type selector
    vid_format_label = Label(main_frame, text="Video Format:", bg="#080808",foreground="white",font=('Helvetica', 16, 'bold'),anchor=W,justify=LEFT)
    vid_format_label.place(relx=0.2,rely=0.58,relwidth=0.5,relheight=0.06)
    format_drop = OptionMenu( main_frame , sel_format , *vformats )
    format_drop.place(relx=0.4,rely=0.58,relwidth=0.1,relheight=0.06)
    confirm_btn = Button(main_frame, text = 'Confirm',bg="#66ff00",font=('Helvetica', 14),command=ResolSelector)
    confirm_btn.place(relx=0.52,rely=0.58,relwidth=0.1,relheight=0.06)


#function to show preview of video to be downloaded
def ShowPreview():
    temp = url_entry.get()
    video = pafy.new(temp)

    #Title of video
    title = str(video.title)
    vid_title = Label(main_frame, text="Title: "+title, bg="#080808",foreground="white",font=('Helvetica', 16, 'bold'),anchor=W,justify=LEFT)
    vid_title.place(relx=0.1,rely=0.3,relwidth=1,relheight=0.07)

    #Autor Name, Likes & Dislikes
    name = video.author
    likes = str(video.likes)
    dislikes = str(video.dislikes)
    vid_auth = Label(main_frame, text="Author: "+ name + "    Likes: " + likes + "    Dislikes: " + dislikes , bg="#080808",foreground="white",font=('Helvetica', 16, 'bold'),anchor=W,justify=LEFT)
    vid_auth.place(relx=0.1,rely=0.36,relwidth=1,relheight=0.07)

    #Rating and View Count of Video
    rating = str(video.rating)
    view_count = str(video.viewcount)
    length = str(video.duration)
    vid_rating = Label(main_frame, text="Rating: "+rating[:3]+"    View Count: "+view_count+"   Duration: "+length, bg="#080808",foreground="white",font=('Helvetica', 16, 'bold'),anchor=W,justify=LEFT)
    vid_rating.place(relx=0.1,rely=0.42,relwidth=1,relheight=0.07)

    video = pafy.new(url_entry.get())
    stream = video.allstreams
    for i in stream:
        temp = str(i)
        if(temp[:5]=="video" or temp[:6]=="normal"):
            vid.append(i)
    
    vid_typ = ["video","normal"]
    sel_vid_typ.set("None")

    #Video type selector
    vid_typ_label = Label(main_frame, text="Video Type:", bg="#080808",foreground="white",font=('Helvetica', 16, 'bold'),anchor=W,justify=LEFT)
    vid_typ_label.place(relx=0.2,rely=0.5,relwidth=0.2,relheight=0.06)
    typ_drop = OptionMenu( main_frame , sel_vid_typ , *vid_typ )
    typ_drop.place(relx=0.4,rely=0.5,relwidth=0.1,relheight=0.06)
    confirm_btn = Button(main_frame, text = 'Confirm',bg="#66ff00",font=('Helvetica', 14),command=FormatSelector)
    confirm_btn.place(relx=0.52,rely=0.5,relwidth=0.1,relheight=0.06)

    sel_format.set("None")
    

if __name__  == "__main__":

    root.state()
    root.title("YouTube Video Downloader")
    root.minsize(750,500)

    width= root.winfo_screenwidth() 
    height= root.winfo_screenheight()

    #Main Window
    main = Frame(root,width=width,height=height,bg='#000000')
    main.place(x=0,y=0)

    #Main Window bg
    my_img = ImageTk.PhotoImage(PIL.Image.open("bg-img.jpg").resize((width,height)))
    mylabel = Label(main , image=my_img)
    mylabel.place(x=0,y=0,relheight=1,relwidth=1)

    #Main frame
    main_frame = Frame(root,bg="#080808")
    main_frame.place(relx=0.25,rely=0.25,relheight=0.6,relwidth=0.5)


    #Frame Title
    main_frame_title = Label(main_frame, text="YOUTUBE VIDEO DOWNLOADER",bg="#ff0000",foreground="white",font=('Helvetica', 17, 'bold'),pady=0.5)
    main_frame_title.place(relx=0,rely=0,relwidth=1,relheight=0.1)

    #URL Label
    URL_label = Label(main_frame, text="Enter URL:",bg="#080808",foreground="white",font=('Helvetica', 16, 'bold'),pady=0.5)
    URL_label.place(relx=-0.325,rely=0.125,relwidth=1,relheight=0.1)

    #URL Entry
    url_entry = ttk.Entry(main_frame, textvariable=url,font=('Calibri', 13))
    url_entry.place(relx=0.275,rely=0.135,relwidth=0.5,relheight=0.07)
    url_entry.focus()

    #Preview button
    get_review = Button(main_frame, text = 'Get preview',bg="#66ff00",font=('Helvetica', 14),command=ShowPreview)
    get_review.place(relx=0.4,rely=0.22,relwidth=0.2,relheight=0.08)

    Loc_label = Label(main_frame, text=" ", bg="#080808",foreground="white",font=('Helvetica', 15),anchor=W,justify=LEFT)
    Loc_label.place(relx=0.4,rely=0.73,relwidth=1,relheight=0.06)

    #Get video details
    root.mainloop()