def minDistance(word1: str, word2: str) -> int:
    n1 = len(word1)
    n2 = len(word2)

    res = [[0] * (n2 + 1) for _ in range(n1 + 1)]

    for i in range(1, n1 + 1):
        res[i][0] = res[i - 1][0] + 1

    for j in range(1, n2 + 1):
        res[0][j] = res[0][j - 1] + 1

    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if word1[i - 1] == word2[j - 1]:
                res[i][j] = res[i - 1][j - 1]
            else:
                res[i][j] = 1 + min(res[i - 1][j], res[i][j - 1],
                                    res[i - 1][j - 1])

    return res[n1][n2]

if __name__=="__main__":
    # Example 1
    word1 = "horse"
    word2 = "ros"
    print(minDistance(word1, word2))

    # Example 2
    word1 = "intention"
    word2 = "execution"
    print(minDistance(word1, word2))