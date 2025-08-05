def arrangeCoins(n):
    """
    :type n: int
    :rtype: int
    """
    cur_sum = 0
    cnt = 0

    i = 0
    while cur_sum <= n:
        cur_sum = cur_sum + i + 1
        cnt = cnt + 1
        i = i + 1

    return cnt - 1

if __name__=="__main__":
    # Example 1
    n = 5
    print(arrangeCoins(n))

    # Example 2
    n = 8
    print(arrangeCoins(n))