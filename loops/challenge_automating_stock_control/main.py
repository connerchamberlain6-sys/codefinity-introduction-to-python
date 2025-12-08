# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}

discount_threshold = 100
print("Processing started")
for item in inventory:
    print(f"Processing {item}")
    current_stock = inventory[item][0]
    min_req_stock = inventory[item][1]
    restock_quan = inventory[item][2]
    sale_status = inventory[item][3]
    while current_stock < min_req_stock:
        current_stock = current_stock + restock_quan
        inventory[item][0]= current_stock
    if (current_stock > discount_threshold) and sale_status == False:
        inventory
print("Processing completed")
    