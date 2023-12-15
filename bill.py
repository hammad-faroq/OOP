
class Bill:
    data="Mobolo\nMobile city\nDeals in all kinds of Mobile sets and Accsessories"
    cell="Cell No: 0321-0000000\nCASHMENO"
    Adress= "Basement  # 4, Hafeez center, Near Monal Resturent, Lahore."
    list=["pant","shirt","shoes","trousers"]
    price=[1500,1300,2300,700]
    def __init__(self):
        self.no=int(input("Enter the bill :"))
        self.day=int(input("Enter the day of the month :"))
        if self.day=="today":
            t=Datetime.month
        self.month=int(input("Enter the month :"))
        self.year=int(input('Enter the year :'))
        self.d1=Datetime(self.month,self.day,self.year)
        self.name=input("Enter the name of the customer :")
        self.address=input("Enter the address of the customer write abc if dont want to write anything :")
        self.data=[]
        self.total=0
        self.d=""
        self.data1()
    def data1(self):
        """This method is used to add more items to the bill"""
        more_bill=True
        while more_bill:
            self.pirticulars=input("Enter the particulars :")
            self.qty=int(input("Enter the quantity of the product :"))
            for i in range(len(Bill.list)-1):
                if self.pirticulars==Bill.list[i]:
                    rate=Bill.price[i]
                    amount=self.qty*rate
                    self.total+=self.qty*rate
                    self.data.append((self.pirticulars,rate,self.qty,amount))
            more=input("Do you want to add more items to the bill :")
            if more=="no":
                self.signature=input("Please enter y for 'yes' and n for 'no' to confirm the bill :")
                self.total1()
                more_bill=False
    def total1(self):
        """This method is used to print all the items in specific order"""
        for i in self.data:
            self.d+=f"{i[0]}\t\t\t\t{i[1]}   \t\t{i[2]}\t\t{i[3]}\n"
    @property
    def pirticulars(self):
        return self._pirticulars
    @pirticulars.setter
    def pirticulars(self,value):
        if value not in Bill.list:
             self.pirticulars=input("sorry this item is out of stock Enter the particulars :")
        else:
            self._pirticulars=value

    def __str__(self):
        return (f"{Bill.data}\n{Bill.cell}\nNo_____{self.no}_____\nDate _____{self.d1.__str__()}_____\nCustomer Name :_____{self.name}_____\nCustomer address :_____{self.address}_____\nPirticulars\t\t\tRate\t\tQty\t\tAmount\n{self.d}\nSignature: {self.signature}es_____ Total: Rs {self.total} Only_____\n\n{Bill.Adress}")

#__________________________________________________________________Date Time class____________________________________________________________________________________________#
class Datetime():
    def __init__(self,month,date,year):
        self.month=month
        self.date = date
        self.year=year
    @property
    def date(self):
        return self._date
    @date.setter
    def date(self,value):
        if self.month == 2 and value > 28:
            self.date = int(input("Date for month 2 cannot exceed 28 Enter again :) :"))
        elif self.month==1 or self.month==3 or self.month==5 :
            if value > 31:
                self.date = int(input(f"Date for month {self.month} exceed 31 Enter again :) :"))
            else:
                self._date = value
        elif self.month == 7 or self.month == 10 or self.month == 12 :
            if  value > 31:
                self.date = int(input(f"Date for month {self.month} exceed 31 Enter again :) :"))
            else:
                self._date = value
        elif self.month==4 or self.month==6 or self.month==9  and value >30:
            self.date = int(input(f"Date for month {self.month} exceed 30 Enter again :) :"))
        elif self.month==11 and value>30:
            self.date = int(input(f"Date for month {self.month} exceed 30 Enter again :) :"))
        else:
            self._date=value
    @property
    def month(self):
        return self._month
    @month.setter
    def month(self,value):
        if value >12:
            self.month=int(input("Month cannot Exceed 12 Enter again :"))
        else:
            self._month=value
    @property
    def year(self):
        return self._year
    @year.setter
    def year(self,value):
        if value<0 and value<1000:
            self.year=int(input(F"Invalid year {value} Enter again :"))
        else:
            self._year=value

    def __str__(self):
        return f"{self._date}//{self.month}//{self.year}"

def main():
    b=Bill()
    print(b)
main()
#_______________________________________________________________________inputs and outputs _________________________________________________________________________________________#
# Mobolo
# Mobile city
# Deals in all kinds of Mobile sets and Accsessories
# Cell No: 0321-0000000
# CASHMENO
# No_____12_____
# Date _____10//12//2022_____
# Customer Name :_____hammad farooq_____
# Customer address :_____lahore raod shp_____
# Pirticulars			Rate		Qty		Amount
# shirt				1300   		3		3900
# pant				1500   		2		3000
# shirt				1300   		3		3900
# shoes				2300   		4		9200
#
# Signature: yes_____ Total: Rs 20000 Only_____
#
# Basement  # 4, Hafeez center, Near Monal Resturent, Lahore.