def longestCommonSubsequence(text1, text2):
    """
    :type text1: str
    :type text2: str
    :rtype: int
    """
    n1 = len(text1)
    n2 = len(text2)

    res = [[0] * (n2 + 1) for _ in range(n1 + 1)]

    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if text1[i - 1] == text2[j - 1]:
                res[i][j] = 1 + res[i - 1][j - 1]
            else:
                res[i][j] = max(res[i - 1][j], res[i][j - 1])
    return res[n1][n2]

if __name__=="__main__":
    # Example 1
    text1 = "abcde"
    text2 = "ace"
    print(longestCommonSubsequence(text1, text2))

    # Example 2
    text1 = "abc"
    text2 = "abc"
    print(longestCommonSubsequence(text1, text2))

    # Example 3
    text1 = "abc"
    text2 = "def"
    print(longestCommonSubsequence(text1, text2))