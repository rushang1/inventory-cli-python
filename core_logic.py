import json

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
    inventory["products"][product] = {
        "name": product,
        "category": category,
        "price": price,
        "quantity": quantity
    }
    with open("inventory.json", "w") as f:
        json.dump(inventory, f, indent=4)

def remove_product_by_id(prod_id):
    inventory = read_inventory()
    if prod_id in inventory["products"]:
        del inventory["products"][prod_id]
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
    try:
        for i in inventory["products"].values():
            if i["name"] == product:
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
                elif choice == "4" or choice.lower() == "quantity":
                    try:
                        new_quantity =  int(input("Enter new quantity: "))
                        i['quantity'] = new_quantity
                    except ValueError:
                        print("Invalid input. Quantity must be a number.")
                else:
                    print("Invalid choice. Please select a valid option.")
        else:
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
            with open("inventory.json", "w") as f:
                json.dump(inventory, f, indent=4)
            return True
    return False