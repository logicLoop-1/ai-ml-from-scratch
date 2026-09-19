class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.__balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.transactions.append(f"Deposited: {amount}") 
        else:
            print("Please enter a positive amount.")   
        pass
    def withdraw(self, amount):
        if amount <= 0:
             print("amount must be positive or greter than zero.")
        elif amount > self.__balance:
             print("Insufficient balance")
        else:
             self.__balance -= amount
             self.transactions.append(f"withdraw: {amount}")     
        pass

    def get_balance(self):
        return self.__balance
    def transactions_History(self):
        if not self.transactions:
            print("no transactions yet")
        for transaction in self.transactions:
            print(transaction)
account = BankAccount("Menka", 500)

while True:
        print(f"\n=== {account.name}'s Bank Account ===")
        print("1. Check balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("5. check transactions history")

        choice = input("Choose an option: ")

        if choice == "1":
            print(f"Balance: {account.get_balance()}")
        elif choice == "2":
            while   True:
                try:
                    amount = float(input("Amount to deposit: "))
                    account.deposit(amount)
                    break
                except ValueError:
                    print("invalid input! try again.")
        elif choice == "3":
            while True:
                try:
                    amount = float(input("Amount to withdraw: "))
                    account.withdraw(amount)
                    break
                except ValueError:
                     print("invalid input! try again.")
        elif choice == "4":
            print("Goodbye!")
            break
        elif choice == "5":
            account.transactions_History()
        else:
            print("Invalid option, try again.")

