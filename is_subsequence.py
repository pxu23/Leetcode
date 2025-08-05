def isSubsequence(s, t):
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return True if i == len(s) else False

if __name__ == '__main__':
    # Example 1
    s = "abc"
    t = "ahbgdc"
    print(isSubsequence(s, t))

    # Example 2
    s = "axc"
    t = "ahbgdc"
    print(isSubsequence(s, t))