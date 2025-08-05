def numSquares(n: int) -> int:
    res = [float('inf')] * (n + 1)
    res[0] = 0
    res[1] = 1

    for i in range(1, n + 1):
        for j in range(1, i):
            if j ** 2 > i:
                break
            res[i] = min(res[i], 1 + res[i - j ** 2])

    return res[-1]

if __name__=="__main__":
    # Example 1
    n = 12
    print(numSquares(n))

    # Example 2
    n = 13
    print(numSquares(n))