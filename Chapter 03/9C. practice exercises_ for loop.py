# Exercise 1: Customer Purchase Summary Report

transactions = [
    {"customer": "Alex", "product": "Laptop", "amount": 1200},
    {"customer": "Jay", "product": "Mouse", "amount": 25},
    {"customer": "Jammie", "product": "Headphones", "amount": 150},
    {"customer": "Alex", "product": "Keyboard", "amount": 75},
    {"customer": "Jammie", "product": "Monitor", "amount": 300},
]

summary = {}

for tx in transactions:
    name = tx["customer"]
    amount = tx["amount"]
    if name in summary:
        summary[name] += amount
    else:
        summary[name] = amount

for customer, total in summary.items():
    print(f"{customer} spent a total of ${total}")


#%%
# Exercise 2: Stock Portfolio Tracker

portfolio = {
    "AAPL": {"shares": 10, "price": 1250.3},
    "GOOGL": {"shares": 5, "price": 2800.5},
    "TSLA": {"shares": 8, "price": 190.1}
}


total_value = 0

for stock, data in portfolio.items():
    stock_value = data["shares"] * data["price"]
    print(f"{stock}: ${stock_value:.2f}")
    total_value += stock_value

print(f"\nTotal Portfolio Value: ${total_value:.2f}")