__author__ = 'Mohamed_Ramadan_PC'
array=[]
for l in range(5):
    x=input("Enter a value : ")
# this in version 2 >>>> to convert input method to take a string y=raw_input("enter a value")
    array.insert(l,x)
    print(x)
print("___________")
for i in range(5):
    print(array.insert(l,l))