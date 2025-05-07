# day10/bank_account.py
class BankAccount:
    def __init__(self, account_number, owner_name, initial_deposit=0.0):
        """Initializes a bank account."""
        self.account_number = account_number
        self.owner_name = owner_name
        if initial_deposit >= 0:
            self.balance = initial_deposit
        else:
            self.balance = 0.0
            print("Initial deposit cannot be negative. Balance set to 0.")
        print(f"Account {self.account_number} for {self.owner_name} created with balance ${self.balance:.2f}")

    def display_balance(self):
        """Displays the current account balance."""
        print(f"Account {self.account_number}: Balance = ${self.balance:.2f}")

    def deposit(self, amount):
        """Deposits a positive amount into the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraws a positive amount if sufficient funds exist."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print(f"Insufficient funds. Cannot withdraw ${amount:.2f}. Balance: ${self.balance:.2f}")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")

    
    def deposit(self, amount):
        """Deposits a positive amount into the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}.")
            self.display_balance() # Call display_balance here
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraws a positive amount if sufficient funds exist."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print(f"Insufficient funds. Cannot withdraw ${amount:.2f}. Balance: ${self.balance:.2f}")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}.")
            self.display_balance() # Call display_balance here

# Test BankAccount
acc1 = BankAccount("ACC1001", "John Doe", 100.00)
acc1.display_balance()
acc1.deposit(50.75)
acc1.withdraw(30.00)
acc1.withdraw(150.00) # Test insufficient funds
acc1.deposit(-10) # Test invalid deposit
acc1.display_balance()

acc2 = BankAccount("ACC1002", "Jane Dane", -50) # Test invalid initial deposit
acc2.display_balance()