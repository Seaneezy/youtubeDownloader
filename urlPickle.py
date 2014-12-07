
#function to validate the YOUTUBE url
def validate(url):
    #counting "youtu" from the start>end of the string
    if url.count("youtu",0,len(url))==1:
        #counting ".com" from the start>end of the string
        if url.count(".com",0,len(url))==1:
            #url is set to 1 for reference that the url is valid.
            url = 1
    return url
#simple input function to get the user's URL
n=input("Enter valid URL: ")
#validating 'n' and assigning the value into 'val'
val=validate(n)
#is the url valid?
if val==1:
    #failsafe verification
    #first 'if' statement is for finding the ID of youtube.com URL's
    if n.count(".com/")==1:
        if n.count("v=")==1:
            #finding the place of 'v=' in
            nv=n.find("v=")
            #setting 'id' to the 2 values ahead of the start of v=
            id=n[nv+2]
            print(id)
        #second 'IF' statement is for finding the ID of youtu.be url's
        if n.count(".be")==1:
            nv2=n.find(".be/")
            id=n[nv2+4]
            print(id)
else:
    print("That is not a valid URL. Please enter a valid YouTube URL like youtube.com/watch?v= or youtu.be/")
