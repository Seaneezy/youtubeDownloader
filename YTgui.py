import pafy
import getpass
import platform
import os
from tkinter import *
user=getpass.getuser()
#validate is exclusive to this program because of entryData
def validate(n):
    entryData=url_entry.get()
    if entryData.count("youtu",0,len(entryData))==1:
        validLabel=Label(root,text="Valid URL!",fg="cyan")
        validLabel.grid(row=3,column=4)
        n=1
    elif entryData.count(".be",0,len(entryData))==1:
        validLabel=Label(root,text="Valid URL!",fg="cyan")
        validLabel.grid(row=3,column=4)
        n=1
    else:
        invalidLabel=Label(root,text="invalid URL",fg="red")
        invalidLabel.grid(row=3,column=4)
        n=0
    return n
#download() is exclusive to this program because of entryData
def download(n):
    entryData=url_entry.get()
    vid=pafy.new(entryData)
    best=vid.getbest()
    if not os.path.exists("/Users/"+user+"/Desktop/YTvideos"):
        os.makedirs("/Users/"+user+"/Desktop/YTvideos")
    dloadLabel=Label(root,text="Now downloading: "+vid.title+", In Desktop/YTvideos",fg="blue")
    dloadLabel.grid(row=5,columnspan=5)
    filename=best.download(filepath="/Users/"+user+"/Desktop/YTvideos/"+vid.title + "." +best.extension,quiet=False)
    #progressLabel=Label(root,text=best.download(filepath="/Users/"+user+"/Desktop/YTvideos/"+vid.title + "." +best.extension,quiet=False))
    #progressLabel.grid(row=6,columnspan=5)
#loadTitle is exclusive to this program because of entryData
def loadTitle(n):
    entryData=url_entry.get()
    n=pafy.new(entryData)
    best=n.getbest()
    vidT=n.title
    titleL=Label(root,text=vidT)
    titleL.grid(row=4,columnspan=4)
    bestRes=best.resolution
    bestFile=best.extension
    label2=Label(root,text="Best stream: "+bestRes+", "+bestFile)
    label2.grid(rowspan=3,columnspan=4)


root=Tk()
mainFrame=Frame()
title_label=Label(root,text="YTDownloader by Seaneezy",fg="blue")
title_label.grid(row=0,columnspan=4)
url_label=Label(root,text="URL: ")
url_entry=Entry(root,bg="white",fg="black")
url_label.grid(row=1,column=0)
url_entry.grid(row=1,column=1)

load_button=Button(root,text="Load")
load_button.grid(row=1,column=3)
load_button.bind("<Button-1>",validate,loadTitle)
d_button=Button(root,text="Download")
d_button.bind("<Button-1>",download)
d_button.grid(row=3,columnspan=4)




root.mainloop()