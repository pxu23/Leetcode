def reverseBits(n: int) -> int:
    res = 0
    for i in range(32):
        bit = n % 2
        res = res * 2 + bit
        n = n // 2
    return res

if __name__=="__main__":
    # Example 1
    n = 43261596
    print(reverseBits(n))

    # Example 2
    n = 2147483644
    print(reverseBits(n))