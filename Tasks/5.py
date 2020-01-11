__author__ = 'Mohamed_Ramadan_PC'
file = open('F:\\txt.txt','r+')
words=0;
lines=0;
for line in file :
    lines+=1;
    temp=line.split();
    words+=len(temp);
    print('words = {} and lines = {}'.format(temp,lines))

print('words = {} and lines = {}'.format(words,lines))