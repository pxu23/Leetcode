def isBalanced(num: str) -> bool:
    evenSum = 0
    oddSum = 0

    for i in range(0, len(num), 2):
        oddSum = oddSum + int(num[i])
        if i + 1 < len(num):
            evenSum = evenSum + int(num[i + 1])

    return oddSum == evenSum

if __name__=='__main__':
    # Example 1
    num = "1234"
    print(isBalanced(num))

    # Example 2
    num = "24123"
    print(isBalanced(num))