__author__ = 'Mohamed_Ramadan_PC'
x=2000

while x in range(2000,3200) :
    if x%7==0  :
        if x%5!=0 :
            print("{} ".format(x),end=" and ")

    x+=1
