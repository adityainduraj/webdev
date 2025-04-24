class Restaurant:
    def __init__(self):
        self.menu_items = []
        self.book_table = []
        self.customer_orders = []
    def add_item_to_menu(self, item):
        self.menu_items.append(item)
        print(f"Added {item} to the menu.")
    def book_tables(self, table_number):
        self.book_table.append(table_number)
        print(f"Table {table_number} has been booked.")
    def customer_order(self, order):
        self.customer_orders.append(order)
        print(f"Order {order} has been placed.")
    def print_menu(self):
        print("Menu Items:")
        for item in self.menu_items:
            print(f"- {item}")
    def print_table_reservations(self):
        print("Table Reservations:")
        for table in self.book_table:
            print(f"- Table {table}")
    def print_customer_orders(self):
        print("Customer Orders:")
        for order in self.customer_orders:
            print(f"- {order}")
def main():
    restaurant = Restaurant()   
    print("1. Add item to menu\n2. Book a table\n3. Place an order\n4. Print menu\n5. Print table reservations\n6. Print customer orders\n7. Exit\n")
    while True:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            item = input("Enter the item to add to the menu: ")
            restaurant.add_item_to_menu(item)
        elif choice == 2:
            table_number = input("Enter the table number to book: ")
            restaurant.book_tables(table_number)
        elif choice == 3:
            order = input("Enter the customer order: ")
            restaurant.customer_order(order)
        elif choice == 4:
            restaurant.print_menu()
        elif choice == 5:
            restaurant.print_table_reservations()
        elif choice == 6:
            restaurant.print_customer_orders()
        elif choice == 7:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

# 1. Add item to menu
# 2. Book a table
# 3. Place an order
# 4. Print menu
# 5. Print table reservations
# 6. Print customer orders
# 7. Exit

# Enter your choice: 1
# Enter the item to add to the menu: 5
# Added 5 to the menu.
# Enter your choice: 2
# Enter the table number to book: 34
# Table 34 has been booked.
# Enter your choice: 3
# Enter the customer order: 45
# Order 45 has been placed.
# Enter your choice: 4
# Menu Items:
# - 5
# Enter your choice: 5
# Table Reservations:
# - Table 34
# Enter your choice: 6
# Customer Orders:
# - 45
# Enter your choice: 7