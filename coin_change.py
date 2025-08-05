def coinChange(coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    min_coins = [0] * (amount + 1)

    for i in range(1, amount + 1):
        min_val = float('inf')
        for coin in coins:
            diff = i - coin
            if diff < 0:
                continue
            min_val = min(min_val, 1 + min_coins[diff])
        min_coins[i] = min_val

    return min_coins[-1] if min_coins[-1] < float('inf') else -1

if __name__ == '__main__':
    # Example 1
    coins = [1, 2, 5]
    amount = 11
    print(coinChange(coins, amount))

    # Example 2
    coins = [2]
    amount = 3
    print(coinChange(coins, amount))

    # Example 3
    coins = [1]
    amount = 0
    print(coinChange(coins, amount))