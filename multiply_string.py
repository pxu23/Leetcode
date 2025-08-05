def multiply(num1: str, num2: str) -> str:
    num1_val = 0
    idx = 0
    for i in range(len(num1) - 1, -1, -1):
        cur_digit = ord(num1[i]) - ord("0")
        num1_val = 10 ** idx * cur_digit + num1_val
        idx += 1

    num2_val = 0
    idx = 0
    for i in range(len(num2) - 1, -1, -1):
        cur_digit = ord(num2[i]) - ord("0")
        num2_val = 10 ** idx * cur_digit + num2_val
        idx += 1

    res = num1_val * num2_val
    res = str(res)
    return res

if __name__ == '__main__':
    # Example 1
    num1 = "2"
    num2 = "3"
    print(multiply(num1, num2))

    # Example 2
    num1 = "123"
    num2 = "456"
    print(multiply(num1, num2))