stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 330,
    "AMZN": 150
}

total_investment = 0

print("Available Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock} : ${price}")

n = int(input("\nEnter the number of different stocks you own: "))

for i in range(n):
    stock_name = input("\nEnter stock name: ").upper()

    if stock_name in stock_prices:
        quantity = int(input("Enter quantity: "))
        investment = stock_prices[stock_name] * quantity
        total_investment += investment

        print(f"Investment in {stock_name}: ${investment}")
    else:
        print("Stock not available in price list!")

print("\n----------------------------")
print("Total Investment Value: $", total_investment)
print("----------------------------")

save = input("Do you want to save the result? (yes/no): ").lower()

if save == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio Tracker\n")
        file.write("-----------------------\n")
        file.write(f"Total Investment Value: ${total_investment}")
    print("Result saved in portfolio.txt")
else:
    print("Result not saved.")