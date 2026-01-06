class BankAccount:
    def __init__(self,minbal,curbal):
        self.minbal=minbal
        self.curbal=curbal
    @property
    def curbal(self):
        return self._curbal
    @curbal.setter
    def curbal (self,value):
        if value>self.minbal:
            self._curbal=value
        else:
            self.curbal=int(input("Current-Balance can't be less than the min-balance enter again :"))
    @property
    def minbal(self):
        return self._minbal
    @minbal.setter
    def minbal(self,value):
        if value>0:
            self._minbal=value
        else:
            self.minbal=int(input("Enter the min-balance again it can't be less than 0 :"))
    def withdraw(self,amount):
        if self._minbal<=(self._curbal)-(amount):
            self._curbal=(self._curbal)-(amount)
            print(f"Your remaining balance is {self._curbal}")
            print(f"Here's is your amount {amount}")
        else:
            amount=int(input(f"Exception Can't withdraw {amount} from the account because balance is {self._curbal} and min-balance is {self._minbal} Enter again :"))
            self.withdraw(amount=amount)
b=BankAccount(minbal=100,curbal=200)
b.withdraw(20)
a=BankAccount(minbal=80,curbal=300)
a.withdraw(300)
c=BankAccount(minbal=30,curbal=500)
c.withdraw(500)
"""outputs"""
# Exception Can't withdraw 120 from the account because balance is 200 and min-balance is 100 Enter again :100
# Your remaining balance is 100
# Here's is your amount 100
# Exception Can't withdraw 300 from the account because balance is 300 and min-balance is 80 Enter again :230
# Exception Can't withdraw 230 from the account because balance is 300 and min-balance is 80 Enter again :220
# Your remaining balance is 80
# Here's is your amount 220
# Exception Can't withdraw 500 from the account because balance is 500 and min-balance is 30 Enter again :400
# Your remaining balance is 100
# Here's is your amount 400