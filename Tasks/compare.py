__author__ = 'Mohamed_Ramadan_PC'
file1 =open('F:\one.txt','r+')
file2 =open('F:\\two.txt','r+')
#file3 =open('F:\\new.txt',"a")
text=file1.read()
text2=file2.read()

arr=[]
count=0
for line1 in text:
   temp=text.split();
   #print('words = {} '.format(temp[0]))
while (count<len(text2)):
  temp=text.split();
  if temp[count] in text2:
     print('words = {} '.format(temp[count]))

     #file3.write(temp[count])
     f=open("F:\\new.txt","a")
     f.write(temp[count])
     f.close()
     count=count+1
#file3.write("mohamed")


file1.close()
file2.close()
file3.close()

