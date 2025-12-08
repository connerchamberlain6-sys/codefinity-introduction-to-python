def apply_discount(price, discount=0.05):
    new_price = price - price * discount
    return new_price
def apply_tax(price, tax=0.07):
    new_price = price + price * tax
    return new_price
def calculate_total(price, discount=0.05, tax=0.07):
    new_price = apply_discount(price, discount)
    final_price = apply_tax(new_price, tax)
    return final_price
total_price_default = calculate_total(120)
total_price_custom = calculate_total(100, discount=0.10, tax=0.08)
print(f"Total cost with default discount and tax: ${total_price_default}")
print(f"Total cost with custom discount and tax: ${total_price_custom}")