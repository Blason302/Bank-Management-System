class NotEnoughBalance(Exception):
    pass
class Account:
    def __init__(self,number,name,balance):
        self.number = number
        self.name = name
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
        print(f"Available Balance after depositing {amount} : {self.balance}")
    def withdraw(self,amount):
       if amount > self.balance:
           raise NotEnoughBalance(f"Not enough Balance, Current Balance : {self.balance}")
       else:
           self.balance -= amount
           print(F"Available Balance after withdrawing {amount} : {self.balance}")
    def check_balance(self):
        print(self.balance)
        
class Bank:
    def __init__(self):
        self.accounts = []
    def create_account(self):
        name = input("Enter a name : ")
        number = int(input("Enter Account Number : "))
        balance = int(input("Enter Account Balance : "))
        account = Account(number,name,balance)
        self.accounts.append(account)
        print("Account Created Successfully")

    def deposit(self):
        amount = int(input("Enter an amount to deposit : "))
        Number = int(input("Enter the account NUmber : "))
        for i in self.accounts:
            if Number == i.number:
                return i.deposit(amount)
            print("Invalid Account Number!")
    def Withdraw(self):
        amount = int(input("Enter an amount to withdraw : "))
        Number = int(input("Enter the account Number : "))
        for i in self.accounts:
            if Number == i.number:
                try:
                    return i.withdraw(amount)
                except NotEnoughBalance as e:
                    print(e)
            print("Invalid Account Number!")

    def check_balance(self):
        Number = int(input("Enter the account Number : "))
        for i in self.accounts:
            if Number == i.number:
                return i.check_balance()
            print("Invalid Account Number!")
    def All_accounts(self):
        print(self.accounts)
    
bank = Bank()
menu = ["1. Create an Account", "2. Deposit", "3. Withdraw", "4. Check Balance", "5. Show All Accounts", "6. Exit"]
while(True):
    print("------>> Menu <<---------")
    print(menu)
    choose = int(input("Choose from Menu : "))
    if choose == 1:
        bank.create_account()
    elif choose == 2:
        bank.deposit()
    elif choose == 3:
        bank.Withdraw()
    elif choose == 4:
        bank.check_balance()
    elif choose == 5:
        bank.All_accounts()
    else:
        print("----->> EXIT <<-----")
        break
