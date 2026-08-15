import json
from datetime import datetime, timezone

def read_inventory():
    try:
        with open("inventory.json", "r") as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        with open("inventory.json", "w") as f:
            json.dump({}, f)
        return {"metadata": {}, "products": {}}

def add_product(product, category, price, quantity):
    inventory = read_inventory()
    next_id = inventory["metadata"].get("next_id", 1)
    product_id = f"PROD-{next_id:03d}"
    inventory["products"][product_id] = {
        "name": product,
        "category": category,
        "price": price,
        "quantity": quantity
    }
    inventory["metadata"]["next_id"] = next_id + 1
    inventory["metadata"]["total_products"] = len(inventory["products"])
    inventory["metadata"]["last_updated"] = datetime.now(timezone.utc).isoformat()
    with open("inventory.json", "w") as f:
        json.dump(inventory, f, indent=4)

def remove_product_by_id(prod_id):
    inventory = read_inventory()
    if prod_id in inventory["products"]:
        del inventory["products"][prod_id]
        inventory["metadata"]["total_products"] = len(inventory["products"])
        inventory["metadata"]["last_updated"] = datetime.now(timezone.utc).isoformat()
        with open("inventory.json", "w") as f:
            json.dump(inventory, f, indent=4)
        return True
    return False

def search_product(product):
    inventory = read_inventory()
    for i in inventory["products"].values():
        if i['name'].lower() == product.lower():
            return i
    return None

def update_product(product):
    inventory = read_inventory()
    found = False
    try:
        for i in inventory["products"].values():
            if i["name"] == product:
                found = True
                choice = input("What would you like to edit:\n1. Name\n2. Category\n3. Price\n4. Quantity\n->")     
                if choice == "1" or choice.lower() == "name":
                    new_name = input("Enter new name: ")
                    i["name"] = new_name
                elif choice == "2" or choice.lower() == "category":
                    new_category = input("Enter new category: ")
                    i['category'] = new_category
                elif choice == "3" or choice.lower() == "price":
                    try:
                        new_price = int(input("Enter new price: "))
                        i["price"] = new_price
                    except ValueError:
                        print("Invalid input. Price must be a number.")
                        break
                elif choice == "4" or choice.lower() == "quantity":
                    try:
                        new_quantity =  int(input("Enter new quantity: "))
                        i['quantity'] = new_quantity
                    except ValueError:
                        print("Invalid input. Quantity must be a number.")
                        break
                else:
                    print("Invalid choice. Please select a valid option.")
                    break

                inventory["metadata"]["last_updated"] = datetime.now(timezone.utc).isoformat()
        if not found:
            print("Product not found.")
        with open ("inventory.json", "w") as f:
            json.dump(inventory, f, indent=4)
    except KeyError:
        print("No products found in inventory.")

def update_product_by_id(prod_id, field, value):
    inventory = read_inventory()
    if prod_id in inventory["products"]:
        if field in inventory["products"][prod_id]:
            inventory["products"][prod_id][field] = value
            inventory["metadata"]["last_updated"] = datetime.now(timezone.utc).isoformat()
            with open("inventory.json", "w") as f:
                json.dump(inventory, f, indent=4)
            return True
    return False

def get_valid_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("That's not a valid float number — try again.")

def get_valid_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("That's not a valid number — try again.")