def maxProfit(prices):
    total_profit = 0
    for i in range(len(prices)):
        if i > 0 and prices[i] > prices[i - 1]:
            profit = prices[i] - prices[i - 1]
            total_profit += profit
    return total_profit

if __name__=="__main__":
    # Example 1
    prices = [7,1,5,3,6,4]
    print(maxProfit(prices))

    # Example 2
    prices = [1, 2, 3, 4, 5]
    print(maxProfit(prices))

    # Example 3
    prices = [7, 6, 4, 3, 1]
    print(maxProfit(prices))