# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold
def calculate_revenue(prices, quantities_sold):
    for i in prices[i]:
        revenue_per = prices[i] * quantities_sold[i]
        revenue.append(revenue_per)
        return revenue
def formatted_output(revenues):
    revenues = list(zip(products, revenue))
    revenue_per_product = sorted(revenues)
    for p, q in revenue_per_product:
        print(f"{p} has total revenue of ${q}")
calculate_revenue(prices, quantities_sold)
formatted_output(revenues)
# Example of expected output line (do not remove):
print(f"{revenue[0]} has total revenue of ${revenue[1]}")