'''
To run this program firts install requirements.txt : pip intall -r requirements.txt

'''
from tkinter import *
from tkinter import filedialog
import PyPDF2
import pyttsx3

 


def extract_text():
  '''To extract text from chosen PDF file'''
  file = filedialog.askopenfile(parent=root, mode='rb', title='Choose a PDF file')
  if file != None:
    pdfReader = PyPDF2.PdfFileReader(file)
    global mytext
    mytext = ""
    for pageNum in range(pdfReader.numPages):
      pageObj = pdfReader.getPage(pageNum)
      mytext += pageObj.extractText()
    file.close()


def stop_speaking(): 
  '''To stop the TTS engine on Stop click button'''
  engine.stop()


def speak_text():
  '''Function to invoke TTS engine to speak the pdf text'''
  global rate
  global male
  global female
  rate = int(rate.get())                  #getting value from rate entry widget
  engine.setProperty('rate', rate)        #setting inputted rate     
  male = int(male.get())
  female = int(female.get())
  all_voices = engine.getProperty('voices')         #extracting all voices from engine
  maleVoice = all_voices[0].id                      #for male voice
  femaleVoice = all_voices[1].id                    #for female voice
  if (male == 0 and female == 0) or (male == 1 and female == 1):       #default voice-> male
    engine.setProperty('voice', maleVoice)          
  elif male == 0 and female == 1:
    engine.setProperty('voice', femaleVoice)
  else:
    engine.setProperty('voice', maleVoice)

  engine.say(mytext)
  engine.runAndWait()



def Application(root):
  '''Whole gui app'''
  root.geometry('{}x{}'.format(600, 500))       #for fixed size window
  root.resizable(width=False, height=False)
  root.title("PDF Reader")
  root.configure(background="#e0ffff")
  global rate, male, female

  frame1 = Frame(root, width=500, height=200, bg="#8a2be2")  #frame 1 for project name and desc.
  frame2 = Frame(root, width=500, height=450, bg="#e0ffff")   #frame 2 for rest part
  frame1.pack(side="top", fill="both")
  frame2.pack(side="top", fill="y")

  #frame 1 widgets
  name1 = Label(frame1, text="Audio Book", fg="white", bg="#8a2be2", font="Arial 28 bold")
  name1.pack()
  name2 = Label(frame1, text="Have patience loading of PDF take some time", fg="white",
                bg="#8a2be2", font="Calibri 15")
  name2.pack()

  #frame 2 widgets
  btn = Button(frame2, text='Select PDF file', command=extract_text, activeforeground="red", 
                padx="70", pady="10", fg="white", bg="black", font="Arial 12")
  btn.grid(row=0, pady=20, columnspan=2)

  rate_text = Label(frame2, text="Enter Rate of Speech:", fg="black",bg="#e0ffff",
                   font="Arial 12")
  rate_text.grid(row=1, column=0, pady=15, padx=0, sticky=E)
  rate = Entry(frame2, text="200", fg="black",bg="white", font="Arial 12")
  rate.grid(row=1, column=1, padx=30, pady=15,sticky=W)
  # rate.focus_set()

  voice_text = Label(frame2, text="Voice:", fg="black",bg="#e0ffff", font="Arial 12")
  voice_text.grid(row=2, column=0, pady=15, padx=0, sticky=E)
  male = IntVar()                        #to store male voice option value
  maleOpt = Checkbutton(frame2,text="Male",bg="#e0ffff",
              variable=male,
              onvalue=1,
              offvalue=0)
  maleOpt.grid(row=2, column=1, pady=0, padx=30, sticky=W)
  female = IntVar()                      #to store female voice option value
  femaleOpt = Checkbutton(frame2,text="Female",bg="#e0ffff",
              variable=female,
              onvalue=1,
              offvalue=0)
  femaleOpt.grid(row=3, column=1, pady=0, padx=30, sticky=W)

  submitBtn = Button(frame2, text='Play PDF file', command=speak_text, activeforeground="red",
               padx="60", pady="10", fg="white", bg="black", font="Arial 12")
  submitBtn.grid(row=4,column=0, pady=65)

  #stop button
  stopBtn = Button(frame2, text='Stop playing', command=stop_speaking,activeforeground="red",
             padx="60", pady="10", fg="white", bg="black", font="Arial 12")
  stopBtn.grid(row=4, column=1, pady=65)





if __name__ == "__main__":
  mytext, rate, male, female = "", 100, 0, 0         
  engine = pyttsx3.init()
  root = Tk()
  Application(root)
  root.mainloop()