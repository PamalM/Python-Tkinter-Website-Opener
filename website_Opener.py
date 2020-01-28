#Project Name : Website Opener
#Written by : Pamal Mangat
#Start date : Friday ,July 24th, 2015.

from tkinter import *
from PIL import ImageTk, Image
import webbrowser

def openYoutube():
    url = 'http://www.youtube.com'
    webbrowser.open(url)

def openGoogle():
    url = 'http://www.google.com'
    webbrowser.open(url)

def quitApp():
    quit()
    exit()
    
root = Tk()
root.title('Websie Opener')

title = Label(root, text='WEBSITE OPENER', bg='black', font='Bizon 22 bold', fg='white')
title.pack(side=TOP)

youtubeButton = Button(root, width=22, height=3, command=lambda:openYoutube(), text='Youtube', font='Bizon 8 bold')
youtubeButton.place(x=90, y=70)

googleButton = Button(root, width='22', height='3', command=lambda:openGoogle(), text='Google', font='Bizon 8 bold')
googleButton.place(x=90, y=150)

quitButton = Button(root,text='Quit!', height=1, width=9, command=lambda:quitApp())
quitButton.place(x=262, y=215)

inform = Label(root, text='A project by Pamal Mangat!', bg='black', fg='white',font='Helvetica 6 bold')
inform.place(x=2, y=235)

#Locks window size,
root.maxsize(350, 250)
root.minsize(350, 250)

#Sets the background color to black
root.configure(background='black')

root.mainloop()
