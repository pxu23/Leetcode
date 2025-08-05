def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    if numRows == 1:
        return s

    res = ""
    for i in range(numRows):
        bigjump = (numRows - 1) * 2
        j = i
        while j < len(s):
            # i = 0 or numRows - 1
            res = res + s[j]

            if i != 0 and i != numRows - 1:
                # don't miss the middle character in zigzag
                smalljump = bigjump - 2 * i
                if j + smalljump >= len(s):
                    break

                res = res + s[j + smalljump]

            j = j + bigjump

    return res

if __name__=="__main__":
    # Example 1
    s = "PAYPALISHIRING"
    numRows = 3
    print(convert(s, numRows))

    # Example 2
    s = "PAYPALISHIRING"
    numRows = 4
    print(convert(s, numRows))

    # Example 3
    s = "A"
    numRows = 1
    print(convert(s, numRows))