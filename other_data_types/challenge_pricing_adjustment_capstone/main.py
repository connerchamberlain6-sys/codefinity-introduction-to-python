grocery_inventory = {"Milk" : ("Dairy", 3.50, 8), "Eggs" : ("Dairy", 5.50, 30), "Bread" : ("Bakery", 2.99, 15), "Apples" : ("Produce", 1.50, 50)}
price_of_eggs = grocery_inventory["Eggs"][1]
category, price, stock = grocery_inventory["Eggs"]
new_price = price - 1
if price_of_eggs > 5:
    print("Eggs are too expensive, reducing the price by $1.")
    grocery_inventory["Eggs"] = (category, new_price, stock)
else:
    print("The price of Eggs is reasonable")
new_item = {"Tomatoes" : ("Produce", 1.20, 30)}
grocery_inventory.update(new_item)
print(f"Inventory after adding Tomatoes: {grocery_inventory}")
milk_stock = grocery_inventory["Milk"][2] 
if milk_stock < 10:
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    newcategory, newprice, newstock = grocery_inventory["Milk"]
    new_milk_stock = milk_stock + 20
    grocery_inventory["Milk"] = (newcategory, newprice, new_milk_stock)
else:
    print("Milk has sufficient stock.")
price_of_apples = grocery_inventory["Apples"][1]
if price_of_apples > 2:
    grocery_inventory.pop("Apples")
    print("Apples removed from inventory due to high price.")
print(f"Updated inventory: {grocery_inventory}")

