def countBits(n):
    """
    :type n: int
    :rtype: List[int]
    """
    dp = [0] * (n + 1)
    offset = 1

    for i in range(1, n + 1):
        # print(i)
        # print(offset)
        if i == 2 * offset:
            offset = offset * 2
        dp[i] = dp[i - offset] + 1

    return dp

if __name__=="__main__":
    # Example 1
    n = 2
    print(countBits(n))

    # Example 2
    n = 5
    print(countBits(n))