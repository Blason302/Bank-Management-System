class NotEnoughBalance(Exception):
    pass
class Account:
    def __init__(self,number,name,balance):
        self.number = number
        self.name = name
        self.balance = balance
    def __str__(self):
       return (
        f"----------------------\n"
        f"Account Holder : {self.name}\n"
        f"Number : {self.number}\n"
        f"Balance : {self.balance}\n"
        f"-----------------------\n"
       )
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
        account = self.find_acount(number)
        if account is not None:
            print("Account Number already exist!")
            return
        balance = int(input("Enter Account Balance : "))
        account = Account(number,name,balance)
        self.accounts.append(account)
        print("Account Created Successfully")
    def find_acount(self,number):
        for i in self.accounts:
            if number == i.number:
                return i
        return None
    def deposit(self):
        amount = int(input("Enter an amount to deposit : "))
        Number = int(input("Enter the account NUmber : "))
        account = self.find_acount(Number)
        if account is None:
            print("Invalid Account Number!")
            return
        account.deposit(amount)
    def Withdraw(self):
        amount = int(input("Enter an amount to withdraw : "))
        Number = int(input("Enter the account Number : "))
        account = self.find_acount(Number)
        if account is None:
            print("Invalid Account Number!")
            return
        try:
            return account.withdraw(amount)
        except NotEnoughBalance as e:
            print(e)

    def check_balance(self):
        Number = int(input("Enter the account Number : "))
        account = self.find_acount(Number)
        if account is None:
            print("Invalid Account Number!")
            return
        account.check_balance()
    def All_accounts(self):
        for i in self.accounts:
            print(i)
    
bank = Bank()
menu = ["1. Create an Account", "2. Deposit", "3. Withdraw", "4. Check Balance", "5. Show All Accounts", "6. Exit"]
while(True):
    print("------>> Menu <<---------")
    for item in menu:
        print(item)
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
