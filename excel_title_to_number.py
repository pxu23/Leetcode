def titleToNumber(columnTitle: str) -> int:
    res = 0
    for elem in columnTitle:
        res = res * 26 + ord(elem) - ord("A") + 1
    return res

if __name__=="__main__":
    # Example 1
    columnTitle = "A"
    print(titleToNumber(columnTitle))

    # Example 2
    columnTitle = "AB"
    print(titleToNumber(columnTitle))

    # Example 3
    columnTitle = "ZY"
    print(titleToNumber(columnTitle))