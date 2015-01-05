import pafy
import getpass
import platform
import os
import tkinter
user=getpass.getuser()
def validate(n):
    if n.count("youtu",0,len(n))==1:
        vid1=pafy.new(n)
        print("Valid URL!: "+vid1.title,"by: "+vid1.author)
        print("Rating: "+str(vid1.likes)+":"+str(vid1.dislikes))
        print("Views: "+str(vid1.viewcount),", Author: "+str(vid1.author))
        n=n
    elif n.count(".be",0,len(n))==1:
        vid1=pafy.new(n)
        print("Valid URL!: "+vid1.title,"by: "+vid1.author)
        print("Rating: "+str(vid1.likes)+":"+str(vid1.dislikes))
        print("Views: "+str(vid1.viewcount))
        n=n
    else:
        print("Invalid URL!")
        n=0
    return n
def download(n):
    vid=pafy.new(n)
    best=vid.getbest()
    if not os.path.exists("/Users/"+user+"/Desktop/YTvideos"):
        os.makedirs("/Users/"+user+"/Desktop/YTvideos")
    print("Now downloading: "+vid.title+", In Desktop/YTvideos")
    filename=best.download(filepath="/Users/"+user+"/Desktop/YTvideos/"+vid.title + "." +best.extension,quiet=False)
    return n
n=input("url: ")
validate(n)

