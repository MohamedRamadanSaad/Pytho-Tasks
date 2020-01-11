__author__ = 'Mohamed_Ramadan_PC'
class person:

    def __init__(self,firstName,lastName,a):
        self.fname=firstName
        self.lname=lastName
        self.age=a

    def setFirstName(self,NewName):
        self.fname=NewName
    def getLastName(self):
        return self.lname

p=person("Ahmed","Mohamed",20)
print(p.getLastName())