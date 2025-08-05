def minimumTotal(triangle):
    """
    :type triangle: List[List[int]]
    :rtype: int
    """
    nRow = len(triangle)

    min_path = [[0] * (i + 1) for i in range(nRow)]

    min_path[0][0] = triangle[0][0]

    for i in range(1, nRow):
        min_path[i][0] = triangle[i][0] + min_path[i - 1][0]
        min_path[i][i] = triangle[i][i] + min_path[i - 1][i - 1]

    for i in range(1, nRow):
        for j in range(1, i):
            min_path[i][j] = min(triangle[i][j] + min_path[i - 1][j],
                                 triangle[i][j] + min_path[i - 1][j - 1])

    res = float('inf')
    for i in range(nRow):
        res = min(res, min_path[nRow - 1][i])

    return res

if __name__=="__main__":
    # Example 1
    triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    print(minimumTotal(triangle))

    # Example 2
    triangle = [[-10]]
    print(minimumTotal(triangle))