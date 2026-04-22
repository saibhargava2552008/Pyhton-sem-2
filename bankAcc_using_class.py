class bankaccount:
    def _init_(self,name,balance):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance=self.balance+amount
        print(self.name,"totalbalace",self.balance)
    def withdraw(self,amount):
        self.balance=self.balance-amount
        print(self.name,"totalbalace",self.balance)
acc=bankaccount("python",1000)
acc.deposit(666)
acc.deposit(222)
acc.withdraw(100)
