class User:
    def __init__(self,name,email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0
    def make_deposit(self,amount):
         self.account_balance += amount
         return self
    def make_withdrawal(self,amount):
         self.account_balance -= amount 
         return self
    def transfer_money(self,other_user,amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self
    def display_user_balance(self):
        print(f"User:{self.name}, Balance: {self.account_balance}")
        return self
        



guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
michelle = User("Michelle Lu", "mark@me.com")

guido.make_deposit(200).make_deposit(500).make_deposit(500).make_withdrawal(100).display_user_balance()
monty.make_deposit(800).make_deposit(1300).make_withdrawal(800).make_withdrawal(100).make_withdrawal(500).display_user_balance()
michelle.make_deposit(900).make_withdrawal(300).make_withdrawal(300).make_withdrawal(300).display_user_balance()
print("Transfering Money")
guido.transfer_money(michelle,1100).display_user_balance()
michelle.display_user_balance()