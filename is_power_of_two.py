def isPowerOfTwo(n):
    for i in range(0, n + 1):
        if 2 ** i > n:
            break
        elif 2 ** i == n:
            return True
    return False

if __name__ == '__main__':
    # Example 1
    n = 1
    print(isPowerOfTwo(n))

    # Example 2
    n = 16
    print(isPowerOfTwo(n))

    # Example 3
    n = 3
    print(isPowerOfTwo(n))