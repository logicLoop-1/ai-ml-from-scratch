class Medicine:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} - ${self.price} - Qty: {self.quantity}"


class Inventory:
    def __init__(self):
        self.medicines = {}  

    def add_medicine(self, medicine):
        # store it in self.medicines, keyed by medicine.name
        pass

    def sell(self, name, quantity):
        # check the medicine exists, check enough quantity is in stock,
        # then reduce quantity - reject invalid amounts (same idea as your BankAccount withdraw!)
        pass

    def restock(self, name, quantity):
        # increase quantity for an existing medicine
        pass

    def low_stock_report(self, threshold=10):
        # return/print all medicines with quantity below the threshold
        pass

    def show_all(self):
        for med in self.medicines.values():
            print(med)


def main():
    inventory = Inventory()

    while True:
        print("\n=== Medical Store Inventory ===")
        print("1. Add medicine")
        print("2. Sell medicine")
        print("3. Restock medicine")
        print("4. View all medicines")
        print("5. Low stock report")
        print("6. Exit")

        choice = input("Choose an option: ")
        # build out each branch, calling the Inventory methods above

main()