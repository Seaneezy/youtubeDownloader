import pafy
import getpass
import platform
import os
import tkinter
user=getpass.getuser()
OS=platform.system()
def validate(url):
    if url.count("youtu",0,len(url))==1:
        url=1
    elif url.count(".be",0,len(url))==1:
        url=1
    return url

url=input("Enter Youtube URL: ")
val=validate(url)
if OS=="Darwin":
    if val==1:
        print("URL is valid!")
        video=pafy.new(url)
        best=video.getbest()
        if not os.path.exists("/Users/"+user+"/Desktop/YTvideos"):
            os.makedirs("/Users/"+user+"/Desktop/YTvideos")
        print("Now downloading: "+video.title+", In Desktop/YTvideos")
        filename=best.download(filepath="/Users/"+user+"/Desktop/YTvideos/"+video.title + "." +best.extension,quiet=False)
        print(filename)
    else:
        print("Invalid URL.")



"""WORKING WITH WINDOWS COMPATIBILITY
elif OS=="Windows":
    Wuser=getpass.getuser()
    if val==1:
        print("URL is valid!")
        video=pafy.new(url)
        best=video.getbest()

"""
""" SIMPLE COMPRESSED CODE
import pafy
url=input("Enter the youtube URL: ")
video=pafy.new(url)
best=video.getbest()
filename=best.download(filepath="/Users/ss/Desktop/YT videos/"+video.title + "." +best.extension,quiet=False)
"""