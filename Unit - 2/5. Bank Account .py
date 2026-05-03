class BankAccount :
    def __init__(self , account_number , balance = 0) :
        self.account_number = account_number
        self.balance = balance

# Method to deposite money
    def deposite(self , amount) :
        if amount > 0 :
            self.balance += amount
            print(f"Deposited amount {amount} successfully .")
        else :
            print("Invalid deposiite amount .")

# method to withdraw money
    def withdraw(self , amount) :
        if amount > 0 :
            if amount <= self.balance :
                self.balance -= amount
                print(f"Withdrawn amount {amount} successfully .")
            else:
                print("Insufficient balance .")
        else :
            print("Invalid withdrawl amount.") 

# Method to check balance
    def check_balance(self) :
        print(f"Current Balance : {self.balance}")

# Example usage
account1 = BankAccount("ACC1001",5000)

account1.check_balance()
account1.deposite(2000)
account1.withdraw(1500)
account1.check_balance()
