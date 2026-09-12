# Encapsulation in Python


class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Please enter a positive amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal must be positive.")

        elif amount > self.__balance:
            print("Insufficient funds.")

        else:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance


account = BankAccount(4455)

print("Initial balance:", account.get_balance())

account.deposit(500)
print("After deposit:", account.get_balance())

account.withdraw(1000)
print("After withdrawal:", account.get_balance())