def isInterleave(s1: str, s2: str, s3: str) -> bool:
    n1 = len(s1)
    n2 = len(s2)

    if n1 + n2 != len(s3):
        return False

    res = [[False] * (n2 + 1) for _ in range(n1 + 1)]

    res[n1][n2] = True

    for i in range(n1 - 1, -1, -1):
        res[i][n2] = res[i + 1][n2] if s3[i + n2] == s1[i] else False

    for j in range(n2 - 1, -1, -1):
        res[n1][j] = res[n1][j + 1] if s3[n1 + j] == s2[j] else False

    for i in range(n1 - 1, -1, -1):
        for j in range(n2 - 1, -1, -1):
            if s3[i + j] == s1[i]:
                if s3[i + j] == s2[j]:
                    res[i][j] = res[i + 1][j] or res[i][j + 1]
                else:
                    res[i][j] = res[i + 1][j]
            else:
                if s3[i + j] == s2[j]:
                    res[i][j] = res[i][j + 1]
                else:
                    res[i][j] = False
    return res[0][0]

if __name__=='__main__':
    # Example 1
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    print(isInterleave(s1, s2, s3))

    # Example 2
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbbaccc"
    print(isInterleave(s1, s2, s3))

    # Example 3
    s1 = ""
    s2 = ""
    s3 = ""
    print(isInterleave(s1, s2, s3))