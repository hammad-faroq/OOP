class Book():
    pages=15#class attribute
    def __init__ (self, title,author,ISBN,publisher):
        self.title=title
        self.__author=author#Non public attribute get accesed by mangling
        self.pages=Book.pages
        self.isbn=ISBN
        self._publisher=publisher


# book=Book("my book","hammad","12","2022")
# print(book.title)
# print(book.pages)
# Book.pages=20
#
# print(book._Book__author)#to acces special non public members
# print(book.pages)
# print(book._publisher)

class Circle():
    def __init__ (self,radius,length):
        self.__radius=radius
        self.length=length

    def get_radius(self):
        print("getter")
        return self.__radius

    def set_radius(self,new_radius):
        print("setter")
        if new_radius>0:
            self.__radius=new_radius
        else:
            print("invalid ")
    any=property(get_radius,set_radius)

circle=Circle(12,2)
print(circle._Circle__radius)
circle.any=141414#with property it will call sometimes getter sometimes setter accor to the instruction given
print(circle.any)
circle._Circle__radius=155
print(circle.any)