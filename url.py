#http://youtube.com/watch?v=???????? √
#youtu.be? √
#function to test validation of URL

# determine if the URL is YOUTUBE  URL
def validate(url):
    if url.count("youtu",0,len(url))==1:
        if url.count(".com",0,len(url))==1:
            url = 1
    return url

n=input("Enter valid URL: ")
val=validate(n)
if val==1:
    if n.count(".com/")==1:
        if n.count("v=")==1:
            nv=n.find("v=")
            print(n[nv+2:])
        if n.count(".be")==1:
            nv2=n.find(".be/")
            print(n[nv2+4:])
else:
    print("That is not a valid URL. Please enter a valid YouTube URL like youtube.com/watch?v= or youtu.be/")

#print "youtube" within a valid url
    #nv3=n.find("youtube")
    #print(n[nv3:nv3+7])

"""
n=input("url: ")
dot1=n.find(".")
dot2=n.find(".com")
print("dot1= ",dot1)
print("dot2= ",dot2)
print(n[dot1+1:dot2])
"""


