class BankAccountProtected:
    def __init__(self, acc_num, owner, initial_balance=0.0):
        self.account_number = acc_num 
        self.owner_name = owner 
        self._balance = initial_balance 
        print(f"Protected account created. Balance: ${self._balance}")

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited ${amount}. New balance ${self._balance}")

    def get_balance(self): 
        return self._balance

    def display_balance(self):
        print(f"Current balance (via getter): ${self.get_balance()}")

acc_p = BankAccountProtected("P001", "Protected User", 100)
acc_p.deposit(50)
acc_p.display_balance()

print(f"Directly accessing _balance: {acc_p._balance}")
acc_p._balance = 1000 
print(f"Directly modified _balance: {acc_p._balance}")
acc_p.display_balance()