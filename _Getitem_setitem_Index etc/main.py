
class  Numbers:
    def __init__(self,data=None):
        if data==None:
            self.data=[]
            self.even =[]
            self.odd=[]
    def add_number(self,no):
        """This method will add the number in the list and creates two list one for even and one for old"""
        if no%2==0:
            self.even.append(no)
        else:
            self.odd.append(no)
        self.data.append(no)
    def delete(self,number):
        """This method will delete the number from the list"""
        try:
            self.data.remove(number)
            self.odd.remove(number)
            self.even.remove(number)
        except ValueError:
            pass
    def __index__(self,value):
        return value
    def __setitem__(self, index, value):
        """This method will set the items in the list in either the even list or the odd list depending upon the number :)"""
        val = self.data[index]
        self.data[index]=value
        if value%2==0:
            ind=self.even.index(val)
            self.even[ind]=value
        else:
            ind = self.odd.index(val)
            self.odd[ind] = value
    def __getitem__(self, index):
        return self.data[index]
    def __iter__(self,w):
        if w==1:
            return self.odd.__iter__()
        else:
            return self.even.__iter__()
    def __next__(self):
        """This will print the numbers in the odd even odd even sequence as much as possible as written in the lab"""
        d = self.__iter__(1)
        r=self.__iter__(2)
        e=""
        try:
            while True:
                e+= f"{d.__next__()}\n"
                e+=f"{r.__next__()}\n"
        except StopIteration:
            pass
        return e
    def __str__(self):
        return self.__next__()
def main():
    c=Numbers()
    c.add_number(4)#add
    c.add_number(7.11)
    c.add_number(8)
    c.add_number(6.7)
    c.add_number(6)
    print(c)
    c.delete(4)#Delete
    c[0]=12##Alter
    c[1]=8.90
    print(c)
    print(c[2])#search
    print(c[c.__index__(2)])#index operator
main()































































# list=["a","b","c","d","e"]
# iter_list=list.__iter__()
# try:
#     while True:
#         print(iter_list.__next__())
# except:This metod is used to print the list(iterable) manually
#     print("all Done!")
