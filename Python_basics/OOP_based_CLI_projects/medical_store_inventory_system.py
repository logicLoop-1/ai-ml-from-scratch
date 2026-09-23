class Medicine:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} - ${self.price:.2f} - Qty: {self.quantity}"


class Inventory:
    def __init__(self):
        self.medicines = {}

    def add_medicine(self, medicine):
        if medicine.name in self.medicines:
            print("Medicine already exists!")
        else:
            self.medicines[medicine.name] = medicine
            print("Medicine added successfully.")

    def sell(self, name, quantity):
        if name not in self.medicines:
            print("Medicine not found.")
            return
        if quantity <= 0:
            print("Quantity must be positive.")
            return
        if quantity > self.medicines[name].quantity:
            print("Not enough stock available.")
            return
        self.medicines[name].quantity -= quantity
        print("Medicine sold successfully.")

    def restock(self, name, quantity):
        if name not in self.medicines:
            print("Medicine not found.")
            return
        if quantity <= 0:
            print("Quantity must be positive.")
            return
        self.medicines[name].quantity += quantity
        print("Medicine restocked successfully.")

    def low_stock_report(self, threshold=10):
        found = False

        for med in self.medicines.values():
            if med.quantity < threshold:
                print(med)
                found = True

        if not found:
            print("No medicines are low in stock.")

    def show_all(self):
        if not self.medicines:
            print("No medicines in inventory.")
            return

        for med in self.medicines.values():
            print(med)
def get_positive_int(message):
    while True:
        try:
            value = int(input(message))

            if value > 0:
                return value
            else:
                print("Please enter a positive number.")

        except ValueError:
            print("Please enter a valid integer.")
def get_positive_float(message):
    while True:
        try:
            value = float(input(message))

            if value > 0:
                return value
            else:
                print("Please enter a positive number.")

        except ValueError:
            print("Please enter a valid number.")


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

        if choice == "1":
            name = input("Enter medicine name: ")
            price = get_positive_float("Enter price: ")
            quantity = get_positive_int("Enter quantity: ")

            medicine = Medicine(name, price, quantity)
            inventory.add_medicine(medicine)

        elif choice == "2":
            name = input("Enter medicine name: ")
            quantity = get_positive_int("Enter quantity to sell: ")

            inventory.sell(name, quantity)

        elif choice == "3":
            name = input("Enter medicine name: ")
            quantity = get_positive_int("Enter quantity to restock: ")

            inventory.restock(name, quantity)

        elif choice == "4":
            inventory.show_all()

        elif choice == "5":
            inventory.low_stock_report()

        elif choice == "6":
            print("Thank you for using the Medical Store Inventory!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()