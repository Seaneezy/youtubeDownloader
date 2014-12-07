import pafy

url=input("url: ")
video=pafy.new(url)
best=video.getbest()
filename=best.download(filepath="/Users/ss/Desktop/YT videos/"+video.title + "." +best.extension,quiet=False)



""" SIMPLE COMPRESSED CODE
import pafy
url=input("Enter the youtube URL: ")
video=pafy.new(url)
best=video.getbest()
filename=best.download(filepath="/Users/ss/Desktop/YT videos/"+video.title + "." +best.extension,quiet=False)
"""