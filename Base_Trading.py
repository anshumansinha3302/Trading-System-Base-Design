import random

class BasicTradingSystem:
    def __init__(self, initial_balance):
        self.balance = initial_balance
        self.portfolio = {}
        self.transaction_history = []

    def buy(self, stock, price, quantity):
        total_cost = price * quantity
        if self.balance >= total_cost:
            self.balance -= total_cost
            self.portfolio[stock] = self.portfolio.get(stock, 0) + quantity
            self.transaction_history.append({'action': 'buy', 'stock': stock, 'price': price, 'quantity': quantity})
            print(f"Bought {quantity} shares of {stock} at ${price} each.")
        else:
            print("Insufficient funds to buy.")

    def sell(self, stock, price, quantity):
        if self.portfolio.get(stock, 0) >= quantity:
            self.portfolio[stock] -= quantity
            total_revenue = price * quantity
            self.balance += total_revenue
            self.transaction_history.append({'action': 'sell', 'stock': stock, 'price': price, 'quantity': quantity})
            print(f"Sold {quantity} shares of {stock} at ${price} each.")
        else:
            print("Insufficient shares to sell.")

    def check_price(self, stock):
        return round(random.uniform(10, 150), 2)

    def run_strategy(self, stock, buy_price, sell_price, quantity):
        current_price = self.check_price(stock)
        print(f"Current price of {stock} is ${current_price}")

        if current_price <= buy_price:
            self.buy(stock, current_price, quantity)
        elif current_price >= sell_price:
            self.sell(stock, current_price, quantity)
        else:
            print("No action taken.")

    def display_portfolio(self):
        print("\nPortfolio Summary:")
        for stock, quantity in self.portfolio.items():
            print(f"{stock}: {quantity} shares")
        print(f"Available Balance: ${self.balance}\n")
        
    def display_transaction_history(self):
        print("\nTransaction History:")
        for transaction in self.transaction_history:
            print(transaction)

trading_system = BasicTradingSystem(1000)

stock = "AAPL"
buy_price = 90 
sell_price = 130  
quantity = 5

for day in range(1, 6): 
    print(f"Day {day}")
    trading_system.run_strategy(stock, buy_price, sell_price, quantity)


trading_system.display_portfolio()
trading_system.display_transaction_history()
