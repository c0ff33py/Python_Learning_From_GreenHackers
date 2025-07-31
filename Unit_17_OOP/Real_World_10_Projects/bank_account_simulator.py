"""
Project Goal:
Build a `BankAccount` class that can:
-   Create a bank account with initial balance
-   Deposit money
-   Withdraw money
-   Show current balance
-   Prevent overdraft(don't allow withdrawal if not enough balance)   

"""

# 🏦 Bank Account Simulator using OOP


class BankAccount:
    # Constructor (__init__)
    def __init__(self, owner_name, balance=0):
        self.owner = owner_name  # Account owner's name
        self.__balance = balance  # private vairable (encapsulate)

    # Deposit method to add money
    def deposit(self, amount):
        if amount >= 0:
            self.__balance += amount
            print(f"✅ {amount} MMK deposited.")
        else:
            print("❌ Invalid deposit amount.")

    # Withdraw method with overdraft protection
    def withdraw(self, amount):
        if amount <= 0:
            print("❌ Withdrawal amount must be positive.")
        elif amount > self.__balance:
            print("❌ Insufficient balance.")
        else:
            self.__balance -= amount
            print(f'✅ {amount} MMK withdrawn.')

    # Method to check balance (getter)
    def check_balance(self):
        print(f"💰 Current balance: {self.__balance} MMK.")

    # String representation method (for print object)

    def __str__(self):
        return f"🏦 BankAccount({self.owner}, Balance: {self.__balance} MMK.)"

# ---------------------------
# -----Testing the class-----
# ----------------------------


# Create accounts
acc1 = BankAccount("c0ff33py", 1000000)
acc2 = BankAccount("Win Htut", 50000000)

# Account 1 operations
print(f"\n{acc1.owner}'s Account:")
acc1.check_balance()
acc1.deposit(20000)
acc1.withdraw(15000)
acc1.withdraw(3500000)  # output: Insufficient balance.
acc1.check_balance()

# Account 2 operations
print(f"\n{acc2.owner}'s Account:")
acc2.check_balance()
acc2.deposit(3500000)
acc2.withdraw(1500000)
acc2.withdraw(50000)
acc2.check_balance()

# Show account object
print("\n Account Summary: ")
print(acc1)
print(acc2)
