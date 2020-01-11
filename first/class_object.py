__author__ = 'Mohamed_Ramadan_PC'
class Book:
    name=""
    auther="auther"
    price=0.0
    qtynstock=0


    def __int__(self,name,author,year):
        self.name=name
        self.auther=author
        self.qtynstock=year

    def getname(self):
        return self.name

    def getauthor(self):
        return self.auther

    def getprice(self):
        return self.price

    def setPrice(self,price2):
        self.price=price2

    def setAuthor(self,author_):
        self.auther=author_
    def print_book(self):
        print(self.name+""+self.auther+""+str(self.year))



mybook = Book("Hello","World",233)
print (mybook.print_book())