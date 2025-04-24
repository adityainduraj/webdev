class Inventory:
    def __init__(self):
        self.items = {}
    def add_item(self, item_id, item_name, stock_count, price):
        if item_id in self.items:
            print(f"Item with ID {item_id} already exists...")
        else:
            self.items[item_id] = {
                'item_name': item_name,
                'stock_count': stock_count,
                'price': price
            }
            print(f"Item {item_name} added successfully.")
    def update_item(self, item_id, stock_count=None, price=None):
        if item_id in self.items:
            if stock_count is not None:
                self.items[item_id]['stock_count'] = stock_count
            if price is not None:
                self.items[item_id]['price'] = price
            print(f"Item with ID {item_id} updated successfully.")
        else:
            print(f"Item with ID {item_id} does not exist.")
    def check_item_details(self, item_id):
        if item_id in self.items:
            return self.items[item_id]
        else:
            print(f"Item with ID {item_id} does not exist.")
            return None
def main():
    inventory = Inventory()
    print("\n1. Add Item\n2. Update Item\n3. Check Item Details\n4. Exit")
    while True:
        choice = input("Enter your choice: ")
        if choice == '1':
            item_id = input("Enter item ID: ")
            item_name = input("Enter item name: ")
            stock_count = int(input("Enter stock count: "))
            price = float(input("Enter price: "))
            inventory.add_item(item_id, item_name, stock_count, price)
        elif choice == '2':
            item_id = input("Enter item ID: ")
            stock_count = input("Enter new stock count (leave blank to skip): ")
            price = input("Enter new price (leave blank to skip): ")
            stock_count = int(stock_count) if stock_count else None
            price = float(price) if price else None
            inventory.update_item(item_id, stock_count, price)
        elif choice == '3':
            item_id = input("Enter item ID: ")
            details = inventory.check_item_details(item_id)
            if details:
                print(f"Item Details: {details}")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please retry.")
if __name__ == "__main__":
    main()

# 1. Add Item
# 2. Update Item
# 3. Check Item Details
# 4. Exit
# Enter your choice: 1
# Enter item ID: 3
# Enter item name: A
# Enter stock count: 3
# Enter price: 230
# Item A added successfully.
# Enter your choice: 1
# Enter item ID: 45
# Enter item name: D
# Enter stock count: 2
# Enter price: 200
# Item D added successfully.
# Enter your choice: 2
# Enter item ID: 3
# Enter new stock count (leave blank to skip): 20
# Enter new price (leave blank to skip): 240
# Item with ID 3 updated successfully.
# Enter your choice: 3
# Enter item ID: 3
# Item Details: {'item_name': 'A', 'stock_count': 20, 'price': 240.0}
# Enter your choice: 4