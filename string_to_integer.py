def myAtoi(s):
    """
    :type s: str
    :rtype: int
    """

    if len(s) == 0:
        return 0

    is_negative = False

    result = 0
    leadingZero = True

    # remove leading zeros
    idx = 0
    while idx < len(s):
        if s[idx] != " " and s[idx] != 0:
            break
        idx += 1

    if idx < len(s):
        if s[idx] == "-":
            is_negative = True
            idx = idx + 1
        elif s[idx] == "+":
            idx += 1

    for i in range(idx, len(s)):
        if s[i] != "0":
            leadingZero = False

        if leadingZero:
            continue

        if not '0' <= s[i] <= '9':
            break
        result = result * 10 + ord(s[i]) - ord('0')

    if is_negative:
        result = result * -1

    if result > 2 ** 31 - 1:
        result = min(result, 2 ** 31 - 1)
    if result < -2 ** 31:
        result = max(result, -2 ** 31)
    return result

if __name__ == '__main__':
    # Example 1
    s = "42"
    print(myAtoi(s))

    # Example 2
    s = " -042"
    print(myAtoi(s))

    # Example 3
    s = "1337c0d3"
    print(myAtoi(s))

    # Example 4
    s = "0-1"
    print(myAtoi(s))

    # Example 5
    s = "words and 987"
    print(myAtoi(s))