def reverse(x: int) -> int:
    res = 0

    negative = False
    if x < 0:
        negative = True

    x = abs(x)
    while x > 0:
        digit = x % 10
        # print(digit)
        res = 10 * res + digit
        x = x // 10

    if negative:
        res = res * -1

    if res < -1 * 2 ** 31 or res > 2 ** 31 - 1:
        return 0
    return res

if __name__=="__main__":
    # Example 1
    x = 123
    print(reverse(x))

    # Example 2
    x = -123
    print(reverse(x))

    # Example 3
    x = 120
    print(reverse(x))


