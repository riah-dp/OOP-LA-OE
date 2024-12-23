print("Name: Moriah De Pedro")
print("=== OE #6 ===\n")

class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid deposit amount.Amount must be positive.")
    
    def withdraw(self, amount):
        if amount > 0 and amount <=self.__balance:
            self.__balance -= amount
        
        else:
            print("Invalid withdrawal amount.Amount must be positive and less than or equal to the current balance.")

    def display_account_info(self):
        print(f"Account Number: {self.__account_number}")
        print(f"Current Balance: {self.__balance}")

    def get_account_number(self):
        return self.__account_number
    
    def get_balance(self):
        self.display_balance()

    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            print("Invalid balance. Balance must be non-negative.")

    def display_balance(self):
            print(f"Current Balance: {self.__balance}")
            
#Test the BankAccount class
account = BankAccount("808080808", 2000.00)
account.display_account_info()
account.deposit(700.00)
account.display_account_info()
account.withdraw(100.00)
account.display_account_info()
account.set_balance(-300.00)
account.display_account_info()