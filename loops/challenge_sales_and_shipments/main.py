# List of products with their initial stock levels at the start of the week
products = [
    ["Apples", 150],  
    ["Bananas", 200],
    ["Oranges", 100],
    ["Mangoes", 120]
]

# List of products sold by the end of the week
units_sold = [["Apples", 30], ["Bananas", 45], ["Oranges", 20], ["Mangoes", 10]]

# New shipment received at the end of the week
shipment_received = [["Apples", 50], ["Bananas", 70], ["Oranges", 30], ["Mangoes", 40]]
for i in range(len(products)):
    name, stock = products[i]
    newstock = stock - units_sold[i][1]
    products[i] = [name, newstock]
for i in range(len(products)):
    name, stock = products[i]
    newstock = stock + shipment_received[i][1]
    products[i]= [name, newstock]
print(f"Final stock levels for all products: {products}")