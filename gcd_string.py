def gcdOfStrings(str1, str2):
    """
    :type str1: str
    :type str2: str
    :rtype: str
    """
    len1 = len(str1)
    len2 = len(str2)

    res = ""

    for i in range(min(len1, len2)):
        if str1[i] != str2[i]:
            return ""

        # check if a divisor
        if len1 % (i + 1) != 0 or len2 % (i + 1) != 0:
            continue

        f1 = len1 // (i + 1)
        f2 = len2 // (i + 1)

        if f1 * str1[:i + 1] == str1 and f2 * str2[:i + 1] == str2:
            res = str1[:i + 1]
    return res

if __name__ == '__main__':
    # Example 1
    str1 = "ABCABC"
    str2 = "ABC"
    print(gcdOfStrings(str1, str2))

    # Example 2
    str1 = "ABABAB"
    str2 = "ABAB"
    print(gcdOfStrings(str1, str2))

    # Example 3
    str1 = "LEET"
    str2 = "CODE"
    print(gcdOfStrings(str1, str2))