class Account:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.__balance = balance   # private attribute

    def deposit(self,amount):
        if amount > 0 :
            self.__balance += amount
            print(f" Added {amount} amount and current balance is {self.__balance}")
        else:
            print("The Amount must be positive")

    def withdraw(self,amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} amount is withdraw and current balance is {self.__balance}")

    # def display_balance(self):
    #     print(f"{self.__balance}")
emp1= Account("Nikhil",5000)
emp1.deposit(500)
emp1.withdraw(600)
#


