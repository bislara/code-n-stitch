from tkinter import*
import speedtest 

def report():
	speed_test = speedtest.Speedtest()
	#d = download
	#u = upload
	#p = ping
	d = round(speed_test.download()/1000000,2)
	u = round(speed_test.upload()/1000000,2)
	p = round(speed_test.results.ping,2)
	download_label.config(text= "Download Speed: "+ str(d)+" Mbps")
	upload_label.config(text= "Upload Speed: " + str(u) + " Mbps")
	ping_label.config(text= "ping : " + str(p) + " ms") 

root = Tk()
root.title("Internet Speed Test")
root.geometry('400x200')
bt = Button(root, text="Test speed",width=20,height=2, command=report)
bt.pack()
bt.place(x=100,y=10)
download_label = Label(root, text="")
download_label.pack()
download_label.place(x=100,y=100)
upload_label = Label(root, text="")
upload_label.pack()
upload_label.place(x=100,y=120)
ping_label = Label(root, text="")
ping_label.pack()
ping_label.place(x=100,y=140)

root.mainloop()

