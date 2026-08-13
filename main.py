import json
from pathlib import Path
from secrets import choice
from core_logic import read_inventory, add_product, remove_product_by_id, search_product, update_product, update_product_by_id 

data = read_inventory()

def main():
    choice = input("What would you like to do:\n1. Add Product\n2. Remove Product\n3. Search Product\n4. Update Product\n-> ")

    if choice == "1" or choice.lower() == "add product":
        product = input("Enter product name: ")
        category = input("Enter product category: ")
        try:
            price = int(input("Enter product price: "))
        except ValueError:
            print("Invalid price. Please enter a valid integer.")
            return
        try:
            quantity = int(input())
            product_id = int(input("Enter product ID to remove: "))
            remove_product_by_id(product_id)
        except ValueError:
            print("Invalid product ID. Please enter a valid integer.")
    elif choice == "3" or choice.lower() == "search product":
        product_name = input("Enter product name to search: ")
        search_product(data, product_name)
    elif choice == "4" or choice.lower() == "update product":
        product_id = int(input("Enter product ID to update: "))
        new_name = input("Enter new product name: ")
        new_category = input("Enter new product category: ")
        new_price = int(input("Enter new product price: "))
        update_product_by_id(data, product_id, new_name, new_category, new_price)