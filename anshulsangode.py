import pygame
from pygame import mixer
from tkinter import *
import os


def playsong():
    currentsong=playlist.get(ACTIVE)
    print(currentsong)
    mixer.music.load(currentsong)
    songstatus.set("Playing")
    mixer.music.play()


def pausesong():
    songstatus.set("Paused")
    mixer.music.pause()


def stopsong():
    songstatus.set("Stopped")
    mixer.music.stop()


def forwardsong():
    songstatus.set("Forwarding")
    mixer.music.forward()

    
def rewindsong():
    songstatus.set("Rewinding")
    mixer.music.rewind()    


root=Tk()
root.title('Mp3 player by Anshul')


mixer.init()
songstatus=StringVar()
songstatus.set("choosing")


#playlist---------------


playlist=Listbox(root,selectmode=SINGLE,bg="DodgerBlue2",fg="black",font=('arial',15),width=50)
playlist.grid(columnspan=5)


os.chdir(r'C:\Users\Admin\Music\Music player')
songs=os.listdir()
for s in songs:
    playlist.insert(END,s)


playbtn=Button(root,text="play",command=playsong)
playbtn.config(font=('arial',20),bg="black",fg="white",padx=7,pady=7)
playbtn.grid(row=1,column=0)


pausebtn=Button(root,text="Pause",command=pausesong)
pausebtn.config(font=('arial',20),bg="black",fg="white",padx=7,pady=7)
pausebtn.grid(row=1,column=1)


stopbtn=Button(root,text="Stop",command=stopsong)
stopbtn.config(font=('arial',20),bg="black",fg="white",padx=7,pady=7)
stopbtn.grid(row=1,column=2)


Forwardbtn=Button(root,text="Forward",command=forwardsong)
Forwardbtn.config(font=('arial',20),bg="black",fg="white",padx=7,pady=7)
Forwardbtn.grid(row=1,column=3)

Rewindbtn=Button(root,text="Rewind",command=rewindsong)
Rewindbtn.config(font=('arial',20),bg="black",fg="white",padx=7,pady=7)
Rewindbtn.grid(row=1,column=4)


mainloop()



