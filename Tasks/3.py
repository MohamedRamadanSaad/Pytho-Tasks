__author__ = 'Mohamed_Ramadan_PC'
x=input("Please Enter Your Word ")

bebin = 0

while bebin<len(x) :
    next=0
    while next<len(x) :
        print(x[(bebin+next)%len(x)],end="")
        next+=1

    print(" , ",end="")
    bebin+=1