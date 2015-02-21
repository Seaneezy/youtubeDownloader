import random

list=[3,2,1]
lenL=len(list)
def rotate(pos1):
    list[pos1],list[pos1+1]=list[pos1+1],list[pos1]
    return
"""
#idx is a counter for determining if the program should go to the start of the list
idx=0
#while the counter is less than the length of the list, it will go through the sort process
while idx < len(list):
    #p1 is a second counter used for moving through the list
    p1=0
    #while the second counter +1 is less than the length of the list the rotation will occur
    while p1+1 < len(list):
        #if the first position is greater than the second position it will rotate the two numbers
        if list[p1]>list[p1+1]:
            rotate(p1)
        #counter is moving through the list
        p1+=1
        print(list)
    #idx is increased to repeat the whole loop until it reaches the end of the list.
    idx+=1
print(list)
"""


"""
Repeat steps 1-5 until the counter reaches the end of the list
1.go to start of list
2.create counter for start of list
3.from the start of the list/counter, check if the item after the start
is less than the first number.
4.If so, move on
5.If not, swap the positions.


"""








#main(list)


"""
    while n[cou]>n[cou+1]:
        if n[cou]<n[cou+1]:
            n[cou]=n[cou+1]
        n[cou],n[cou+1]=n[cou+1],n[cou]
        cou+=1
        print(n)
"""