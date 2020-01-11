__author__ = 'Mohamed_Ramadan_PC'
x=input("Enter The First String :- ")

y=input("Enter The Second String :- ")

new =""
for tempx in x :
    for tempy in y :
        if tempx==tempy :
            if new.find(tempx)==-1 :
                new +=tempx

print(new)