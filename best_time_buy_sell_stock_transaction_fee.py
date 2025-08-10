def maxProfit(prices, fee):
    n = len(prices)
    res = [[0] * n for _ in range(2)]

    res[0][0] = 0
    res[1][0] = -1 * prices[0] - fee

    for i in range(1, n):
        res[0][i] = max(res[0][i - 1], res[1][i - 1] + prices[i])
        res[1][i] = max(res[1][i - 1], res[0][i - 1] - prices[i] - fee)
    return max(res[0][n - 1], res[0][n - 1])

if __name__=="__main__":
    # Example 1
    prices = [1, 3, 2, 8, 4, 9]
    print(maxProfit(prices, 2))

    # Example 2
    prices = [1,3,7,5,10,3]
    print(maxProfit(prices, 3))