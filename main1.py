import sys


def maximize_profit(prices):
    if not prices:
        return 0

    min_price = prices[0]
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(1)

    prices = [int(price) for price in sys.argv[1].split(',')]
    max_profit = maximize_profit(prices)

    print(max_profit)