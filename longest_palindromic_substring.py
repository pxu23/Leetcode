def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    n = len(s)
    dp = [[False] * n for _ in range(n)]

    start = 0
    max_length = 1

    for i in range(n):
        dp[i][i] = True

    # length of 2
    for i in range(n - 1):
        dp[i][i + 1] = True if s[i] == s[i + 1] else False
        if dp[i][i + 1]:
            start = i
            max_length = 2

    for length in range(3, n + 1):
        for i in range(n - length + 1):
            if s[i + length - 1] == s[i] and dp[i + 1][i + length - 2]:
                dp[i][i + length - 1] = True
                if length > max_length:
                    start = i
                    max_length = length

    return s[start: start + max_length]

if __name__=="__main__":
    # Example 1
    s = "babad"
    print(longestPalindrome(s))

    # Example 2
    s = "cbbd"
    print(longestPalindrome(s))