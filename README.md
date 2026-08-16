# Inventory Management CLI

A command-line inventory management tool built in Python. Supports adding,
removing, searching, and updating products, with data persisted to a local
JSON file.

## Features

- Add new products with auto-generated unique IDs (never reused, even after deletion)
- Remove products by ID
- Search products by name
- Update existing product details (name, category, price, quantity)
- View full current inventory
- Input validation on all numeric fields (price, quantity)
- Metadata tracking (last updated timestamp, total product count)

## Tech Stack

- Python 3.14
- Standard library only (`json`, `datetime`) — no external dependencies

## Getting Started

### Prerequisites
- Python 3.8 or higher

### Installation

````bash
git clone https://github.com/rushang1/inventory-cli-python.git
cd inventory-cli-python
````

No dependencies to install — this project uses only Python's standard library.

### Running the app

````bash
python main.py
````

## Usage

On launch, you'll see a menu:

````
What would you like to do:
1. Add Product
2. Remove Product
3. Search Product
4. Update Product
5. See Inventory
6. Exit
