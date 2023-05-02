import sys
import json

class Stock:
    def __init__(self, ticker, name, close):
        self.ticker = ticker
        self.name = name
        self.close = close

def get_stock(ticker):
    with open('stocks.json') as f:
        data = json.load(f)
    for stock_data in data:
        if stock_data['ticker'] == ticker:
            return Stock(stock_data['ticker'], stock_data['name'], stock_data['close'])
    return None

if __name__ == "__main__":
    tickers_and_quantities = sys.argv[1].split(",")
    total_close = 0
    for ticker_quantity in tickers_and_quantities:
        ticker, quantity = ticker_quantity.split(":")
        stock = get_stock(ticker)
        if stock is None:
            print(f"Error: Stock with ticker {ticker} was not found")
            sys.exit(1)
        total_close += stock.close * int(quantity)
    print(total_close)