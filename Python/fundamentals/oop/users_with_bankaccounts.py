class BankAccount:

    all_accounts = []
    def __init__(self,int_rate,balance):
        self.int_rate = int_rate
        self.balance=balance
        BankAccount.all_accounts.append(self)

    def deposit(self,amount):
        self.balance += amount
        return self

    def withdrawl(self, amount):
        if amount > self.balance:
            print("Insufficient Funds: Charging $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self
    
    def display_account_info(self):
        return f"{self.balance}"
    
    def yield_interest(self):
        self.balance *= (1+self.int_rate)
        return self

    @classmethod
    def printallAccountsInfo(cls):
        for account in cls.allAccounts:
            account.display_account_info()

class User:

    def __init__(self, first_name):
        self.first_name = first_name
        self.account = {
            "checking": BankAccount(.05,2000),
            "savings": BankAccount(.06,50000)
        }

    def display_user_balance(self):
        print(f"User:{self.first_name},  Checking Balance: {self.account['checking'].display_account_info()}")
        print(f"User:{self.first_name}, Savings Balance: {self.account['savings'].display_account_info()}")
        return self 
        

monty = User("Monty Python")

monty.account['checking'].deposit(100)
monty.account['savings'].deposit(500)

monty.display_user_balance()