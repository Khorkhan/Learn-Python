# Step 1. Create class
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = float(price) # variable & type (float)
        self.quantity = int(quantity) # variable & type (int)

    def __str__(self):
        # String formatting:
        return f"{self.name:<15} | Price: {self.price:>8.2f} | Quantity: {self.quantity:>5}"
    
# Step 2. Create Working functions & list

inventory = [] # list to store products

def add_product():
    print("\n--- Add New Product ---")
    name = input("Product Name: ")
    price = input("Product Price: ")
    qty = input("Product Quantity: ")

    # Create Object from class Product and add to inventory
    new_item = Product(name, price, qty)
    inventory.append(new_item)
    print("added successfully!")

def show_inventory():
    print("\n--- Inventory List ---")
    if not inventory:
        print("Inventory is empty.")
    else:
        # loop through inventory and print each product
        for item in inventory:
            print(item)

def main():
    while True: #infinite Loop till break
        print("\n=== Mini Inventory System ===")
        print("1. Show Inventory")
        print("2. Add Product")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            show_inventory()
        elif choice == "2":
            add_product()
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# run program
if __name__ == "__main__":
    main()