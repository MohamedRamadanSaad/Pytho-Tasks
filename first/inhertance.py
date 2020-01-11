__author__ = 'Mohamed_Ramadan_PC'
class shape:
    __x=0 # __ is privete
    y=0

    def getX(self):
        return self.x

    def getX(self):
        print("this is method Overriding brtween super and scale")

    def getY(self):
        return self.y

class Rectangle(shape):
    width = 0
    hight=0

    def __int__(self,width_,height_):
        self.width=width_
        self.hight=height_

re=Rectangle(100,200)
re.getX()