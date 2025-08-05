def intToRoman(num):
    """
    :type num: int
    :rtype: str
    """
    if num == 0:
        return 0

    symbol_value_map = [["M", 1000], ["CM", 900], ["D", 500], ["CD", 400], ["C", 100], ["XC", 90], ["L", 50],
                        ["XL", 40], ["X", 10], ["IX", 9], ["V", 5], ["IV", 4], ["I", 1]]

    res = ""
    for symbol, val in symbol_value_map:
        while num - val >= 0:
            res = res + symbol
            num -= val

    return res

if __name__ == '__main__':
    # Example 1
    num = 3749
    print(intToRoman(num))

    # Example 2
    num = 58
    print(intToRoman(num))

    # Example 3
    num = 1994
    print(intToRoman(num))