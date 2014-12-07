import pickle
yt="VQsHnfgQPQ"
#open the file
vidInfo=open("YTurl.txt","wb")
#dumping video ID into the info file
pickle.dump(yt,vidInfo)
#closing the video info file
vidInfo.close()

#unpickle
#open the saved file from before
savedYT=open("YTurl.txt","rb")
#loading file data into py variable
savedID=pickle.load(savedYT)
#close file
savedYT.close()

#printing file data
print("saved info: ", savedID)