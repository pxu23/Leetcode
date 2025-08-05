def kthFactor(n: int, k: int) -> int:
    idx = 0
    for i in range(1, n + 1):
        if n % i == 0:
            idx += 1
            if idx == k:
                return i
    return -1

if __name__ == '__main__':
    # Example 1
    n = 12
    k = 3
    print(kthFactor(n, k))

    # Example 2
    n = 7
    k = 2
    print(kthFactor(n, k))

    # Example 3
    n = 4
    k = 4
    print(kthFactor(n, k))