def hammingWeight(n):
    """
    :type n: int
    :rtype: int
    """
    cnt = 0

    while n > 0:
        if n % 2 == 1:
            cnt += 1
        n = n // 2

    return cnt

if __name__ == '__main__':
    # Example 1
    n = 11
    print(hammingWeight(n))

    # Example 2
    n = 128
    print(hammingWeight(n))

    # Example 3
    n = 2147483645
    print(hammingWeight(n))