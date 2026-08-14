import json
from pathlib import Path
from secrets import choice
from core_logic import read_inventory, add_product, remove_product_by_id, search_product, update_product, update_product_by_id 


def main():

    while True:
        choice = input("\nWhat would you like to do:\n1. Add Product\n2. Remove Product\n3. Search Product\n4. Update Product\n5. See Inventory\n6. Exit\n-> ")

        if choice == "1" or choice.lower() == "add product":
            product = input("Enter product name: ")
            category = input("Enter product category: ")
            try:
                price = int(input("Enter product price: "))
            except ValueError:
                print("\nInvalid price. Please enter a valid integer.")
            try:
                quantity = int(input("Enter product quantity:"))
            except ValueError:
                print("\nInvalid quantity. Please enter a valid integer.")
            add_product(product, category, price, quantity)
            print(f"\nUpdated Inventory: {read_inventory()}")

        elif choice == "2" or choice.lower() == "remove product":
            product_id = input("Enter product ID to remove: ")
            if not remove_product_by_id(product_id):
                print("\nInvalid product ID. Please enter a valid integer.")
            else:
                update_product_by_id(product_id)
                print(f"\nUpdated Inventory: {read_inventory()}")

        elif choice == "3" or choice.lower() == "search product":
            product_name = input("Enter product name to search: ")
            searched_product =search_product(product_name)
            print(f"\nSearched Product: {searched_product}")

        elif choice == "4" or choice.lower() == "update product":
            product_name = input("Enter product name of which you want to update the details of: ")
            update_product(product_name)
            data = read_inventory()
            print(f"Updated Inventory: {data}\n")

        elif choice == "5" or choice.lower() == "see inventory":
            data = read_inventory()
            print(f"\nCurrent Inventory: {data}")

        elif choice == "6" or choice.lower() == "exit":
            print("Exiting the program.")
            print(f"\n{read_inventory()} \n")
            break

        else:
            print("\nInvalid choice selected. Please select a valid option.\n")

if __name__ == "__main__":
    main()