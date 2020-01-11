__author__ = 'Mohamed_Ramadan_PC'
import math
class mahmoud:
    def __init__(self):
        self.w1=.1
        self.w2=.2
        self.w3=.3
    def learning (self,x1,x2,x3,result):
        flag=0
        while(flag==0):
            sum=x1*self.w1+x2*self.w2+x3*self.w3
            y1=1/(1+(math.e**-sum))
            if((y1>=.5 and result==1)or(y1<.5 and result==0)):
                flag=1
            else:
                self.w1=self.w1+.01*(result-y1)
                self.w2=self.w2+.01*(result-y1)
                self.w3=self.w3+.01*(result-y1)

    def predection (self,x1,x2,x3):
         sum=x1*self.w1+x2*self.w2+x3*self.w3
         y1=1/(1+(math.e**-sum))
         if(y1>=.5):
             print("have diabitic")
         else:
              print("haven't diabitic")

s=mahmoud()
s.learning(20,10,5,1)
s.learning(30,8,2,0)
s.predection(30,8,2)
print(s.w1)
print(s.w2)
print(s.w3)