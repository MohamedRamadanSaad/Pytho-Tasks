__author__ = 'Mohamed_Ramadan_PC'
class Shape:
    x=0
    y=0

    def __init__(self,x_,y_):
        self.x=x_
        self.y=y_

    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def prnt_shape(self):
        print(str(self.x))
        print(str(self.y))
shape=Shape(30,46)
shape.prnt_shape()