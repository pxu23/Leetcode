def maxProfit(prices):
    max_profit = 0
    min_price = float('inf')

    for i in range(len(prices)):
        # buy at the lowest price
        min_price = min(min_price, prices[i])

        # the maximum profit so far
        max_profit = max(max_profit, prices[i] - min_price)

    return max_profit

if __name__ == "__main__":
    # Example 1
    prices = [7, 1, 5, 3, 6, 4]
    print(maxProfit(prices))

    # Example 2
    prices = [7, 6, 4, 3, 1]
    print(maxProfit(prices))