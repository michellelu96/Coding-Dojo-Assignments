class BankAccount:
    def __init__(self,account_name, int_rate=.005, balance=0): 
        self.int_rate = int_rate
        self.balance = balance
        self.account_name= account_name
    def deposit(self, amount):
        self.balance+=amount
        return self
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds: Charging $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self
    def display_account_info(self):
        print(f"Account:{self.account_name} Balance:{self.balance}")
        return self
    def yield_interest(self):
        self.balance *= (1+self.int_rate)
        return self


checking = BankAccount('Checking',.005,9000)
savings = BankAccount('Savings',.005,1000)

print(f"Beginning Checking Balance: {checking.balance}")
print(f"Beginning Savings Balance: {savings.balance}")

checking.deposit(10000).deposit(1000).deposit(8000).withdraw(5000).yield_interest().display_account_info()
savings.deposit(100000).deposit(5).withdraw(500).withdraw(7000).withdraw(900).withdraw(500).yield_interest().display_account_info()
