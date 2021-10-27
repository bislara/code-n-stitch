from tkinter import *
from tkinter import messagebox
import tkinter.font as font
from PIL import ImageTk
from PIL import Image
import time
import random
import json


class Stack2048:

    def __init__(self, canvas, main2,main1):
        self.c = canvas
        self.root = main2
        self.main1=main1
        self.pegwidth = 50
        self.pegheight = 260                    #height of each stack
        self.pegdist = 100                      #distance between stacks
        self.pegstate = [[], [], [], []]        #current state of stacks
        self.peg_wise_blocks = [[], [], [], []]  #store shape of blocks in each stacks
        self.block = [0,0]                      #block picker state 0 means vacant
        self.block_picker = [0,0]               #stores shapes block in block picker peg
        self.score=0
        string= "SCORE : "+str(self.score)
        self.sc=self.c.create_text(600,10, fill='#000000', text=string , font=('Noto Sans CJK JP Black',16))
        self.color = {2:"#ff0000",4:"#00ff00",8:"#62a254",16:"#c0c620",32:"#36a8d5",64:"#ff00ff",128:"#800000",256:"#008080",512:"#008000",1024:"#000080",2048:"#808000"}
        
        with open("score.json") as f:
            data=json.load(f)
        
        string= "MAX SCORE : "+str(max(data))
        self.mxsc=self.c.create_text(100,10, fill='#000000', text=string , font=('Noto Sans CJK JP Black',16))
        
        
        
        
        
    def round_rectangle(self,x1,y1,x2,y2,r,**kwargs):
        points = (x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y1+r, x2, y2-r, x2, y2-r, x2, y2, x2-r, y2, x2-r, y2, x1+r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1)
        return self.c.create_polygon(points, **kwargs, outline="#000000", width=1, smooth=True)


    #function to merge the blocks
    def merge_blocks(self,i):
        l = len(self.pegstate[i])
        
        #check weather top to blocks are same or not if yes merge these two blocks
        if l!=1 and self.pegstate[i][l-1]==self.pegstate[i][l-2]:        
            b1 = self.peg_wise_blocks[i].pop()
            b2 = self.peg_wise_blocks[i].pop()
            cor = self.c.coords(b2[0])
            x = cor[0]-30
            y = cor[1]
            self.c.delete(b1[0])
            self.c.delete(b1[1])
            self.c.delete(b2[0])
            self.c.delete(b2[1])
            n = self.pegstate[i].pop()
            n += self.pegstate[i].pop()
            self.pegstate[i].append(n)
            c=self.color.get(n)
            p = self.round_rectangle(x, y, x+50, y+50, 30, fill=c)
            t = self.c.create_text(x+25,y+25, fill='#ffffff', text=n, font=('Noto Sans CJK JP Black',16))
            self.score+=n
            string="SCORE : "+str(self.score)
            self.c.itemconfig(self.sc,text=string)
            self.peg_wise_blocks[i].append([p,t])
            self.c.update()
            time.sleep(0.5)
            
            if n == 2048 :
                messagebox.showinfo("Popup Window","You Win")
                raiseframe(main1)
            self.merge_blocks(i)
            
        
    #function to move block from block picker to selected stack
    def onclickPeg(self, event, i):
        #if block is selected and stack contain less than 5 block then only move the block
        if self.block[0]!=0:
            cor_peg = self.c.coords(self.pegs[i])
            p,t = self.block[0],self.block[1]
            self.block[0]=0
            cor_block = self.c.coords(p)
            x = cor_peg[0]-cor_block[0]+15
            y=-95-len(self.pegstate[i])*50-50
            
            self.c.move(p,x,y)
            
            self.c.tag_unbind(p,'<ButtonPress-1>')
            n=self.c.itemcget(t,'text')
            self.c.delete(t)
            
            cor_block = self.c.coords(p)
            t = self.c.create_text(cor_block[0]-7.5,cor_block[1]+25, fill='white', text=n, font=('Noto Sans CJK JP Black',16))
            self.pegstate[i].append(int(n))
            self.peg_wise_blocks[i].append([p,t])
            self.c.update()
            time.sleep(0.5)
            self.merge_blocks(i)
            self.c.update()
            time.sleep(0.5)
            
            #vacant the space in block picker and create block
            if self.block_picker[0]==p:
                self.block_picker[0]=0
            else:
                self.block_picker[1]=0

            self.create_block()
            
        #if block is not selected show error
        elif self.block[0] == 0:
            messagebox.showerror("error","Select Block")
            
        
        #if stack is full the end the game
        if len(self.pegstate[0])==5 or len(self.pegstate[1])==5 or len(self.pegstate[2])==5 or len(self.pegstate[3])==5:
            messagebox.showwarning("End","GAME OVER")
    
            with open("score.json") as f:
                data=json.load(f)
            if(max(data)<self.score):
                data.append(self.score)
                messagebox.showinfo("Result","Your Score is "+str(self.score)+"\n\nYou Win")
            else:
                messagebox.showinfo("Result","Your Score is "+str(self.score)+"\n\nYou Lose")
            
            with open("score.json",'w') as f:
                json.dump(data,f)
                
            raiseframe(self.main1)


    #store selected block
    def onclickBlock(self,event,p,t):
        self.block[0]=p
        self.block[1]=t
        

    #create stacks in game
    def create_pegs(self):    
        width, height = self.root.getint(self.c['width']), self.root.getint(self.c['height'])
        
        x1, y1 = 175,50
        x2, y2 = x1+self.pegwidth, y1+self.pegheight

        self.pegs = []
        p = self.round_rectangle(x1, y1, x2, y2, 15, fill='#b6915e')
        self.c.tag_bind(p, '<ButtonPress-1>', lambda event: self.onclickPeg(event,0))
        self.pegs.append(p)
        
        x1, x2 = x1+self.pegdist, x2+self.pegdist
        p = self.round_rectangle(x1, y1, x2, y2, 15, fill='#b6915e')
        self.c.tag_bind(p, '<ButtonPress-1>', lambda event: self.onclickPeg(event,1))
        self.pegs.append(p)
        
        x1, x2 = x1+self.pegdist, x2+self.pegdist
        p = self.round_rectangle(x1, y1, x2, y2, 15, fill='#b6915e')
        self.c.tag_bind(p, '<ButtonPress-1>', lambda event: self.onclickPeg(event,2))
        self.pegs.append(p)
        
        x1, x2 = x1+self.pegdist, x2+self.pegdist
        p = self.round_rectangle(x1, y1, x2, y2, 15, fill="#b6915e")
        self.c.tag_bind(p, '<ButtonPress-1>', lambda event: self.onclickPeg(event,3))
        self.pegs.append(p)
        
        p = self.round_rectangle(275, 405, 420, 455, 15,fill='#b6915e')
        self.pegs.append(p)
        self.root.update()
        
        
    #function to create block in block picker
    def create_block(self):
        x1, y1 = 275,405
        f = 0
        if self.block_picker[0]!=0:
            x1 = x1+95
            self.block_picker[1]=1
        else:
            self.block_picker[0]=1
            
        x2, y2 = x1+50, y1+50
        a= []
        for i in range (0,4):
            if len(self.pegstate[i])==0:
                a.append(0)
            else:
                a.append(max(self.pegstate[i]))
            
        i = max(a)
        j = 0
        while 2**j<i:
        	j+=1
        n=0
        if j==1 or j==0 or j==2:
        	n=2
        else:
        	i=random.randint(1,j-1)
        	n=2**i
        	
        c=self.color.get(n)
        p = self.round_rectangle(x1, y1, x2, y2, 30, fill=c)
        t = self.c.create_text(x1+25,y1+25, fill="#ffffff", text=n, font=('Noto Sans CJK JP Black',16))
        self.c.tag_bind(p, '<ButtonPress-1>', lambda event: self.onclickBlock(event,p,t))
        self.c.tag_bind(t, '<ButtonPress-1>', lambda event: self.onclickBlock(event,p,t))
        if self.block_picker[0] == 1:
            self.block_picker[0]=p
        else :
            self.block_picker[1]=p
    

#start game
def play(main2,main1):
    main2.tkraise()
    canvas = Canvas(main2,width=700,height=500,bd=0, highlightthickness=0,bg='#fffaf1')
    canvas.place(x=0,y=150)
    s = Stack2048(canvas,main2,main1)
    s.create_pegs()
    s.create_block()
    s.create_block()    
       
def raiseframe(frame):
    frame.tkraise()
    
            
if __name__  == "__main__":

    tk = Tk()
    tk.title('2048')
    tk.geometry('700x700')
    tk.resizable(0,0)
    main1 = Frame(tk,height=700,width=700,bg='#fffaf1')     #main window
    main2 = Frame(tk,height=700,width=700,bg='#fffaf1')     #game window
    main1.place(x=0,y=0)        
    main2.place(x=0,y=0)
    
    #create main window        
    my_img1=ImageTk.PhotoImage(Image.open("images/fullbg.jpg").resize((700,700)))
    mylabel=Label(main1 , image=my_img1)
    mylabel.place(x=0,y=0,relheight=1,relwidth=1)
    
    #start game button
    stimg=ImageTk.PhotoImage(Image.open("images/Startbt.jpg").resize((200,70)))
    startb = Button(main1, text='START GAME',relief=FLAT,image=stimg, command = lambda : play(main2,main1))
    startb.place(x=75,y=400)
    
    #exit game button
    eximg=ImageTk.PhotoImage(Image.open("images/eximt.jpg").resize((200,70)))
    exit = Button(main1, text='EXIT',image=eximg, relief=FLAT, command=tk.destroy)
    exit.place(x=425,y=400)
    
    #create game window
    eximg1=ImageTk.PhotoImage(Image.open("images/eximt.jpg").resize((150,50)))
    logo=ImageTk.PhotoImage(Image.open("images/Logo_2.jpg").resize((200,100)))
    mylabel2=Label(main2 , image=logo,bd=0, highlightthickness=0)
    mylabel2.place(x=300,y=10)
    back = Button(main2, text='Back',relief=FLAT, image=eximg1, command = lambda : raiseframe(main1))
    back.place(x=50,y=20)
    
    main1.tkraise()
    
    
    tk.mainloop()
    
    
