class Bank:
    def openaccount(self,cname,acno,balance):
        self.c=cname
        self.ac=acno
        self.b=balance
        print("Hello" ,self.c,"Your account number",self.ac,"Is opened With",self.b, "Rs.")

    def deposit(self,amount):
        self.b=self.b+amount

    def withdraw(self,amount):
        if amount<=self.b:
            self.b=self.b-amount
        else:
            self.needs=amount-self.b
            print("Sorry you need Another", self.needs, "Rs")

    def checkbalance(self):
        print("Current Balance: " ,self.b)

b1=Bank()
print("*" *50)

cname=input("Enter Customer Name: ")
print("*" *50)
acno=int(input("Enter Account Number: "))
print("*" *50)
balance=int(input("Enter Initial Balance: "))
print("*" *50)

b1.openaccount(cname,acno,balance)

while True:
    print("*" *50)
    print("1.Deposite")
    print("2.Withdraw")
    print("3.check Balance")
    print("4.Exit")
    print("*" *50)

    choice=int(input("Enter your Choice: "))
    print("*"*50)

    if choice==1:
        amount=int(input("Enter Deposite Amount: "))
        b1.deposit(amount)
    elif choice==2:
        amount=int(input("Enter Withdraw Amount: "))
        b1.withdraw(amount)
        print("*"*50)
    elif choice==3:
        b1.checkbalance()
        print("*"*50)
    else:
        print("Invalid Choice. Bye")
        break
        
    
