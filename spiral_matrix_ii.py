def generateMatrix(n):
    """
    :type n: int
    :rtype: List[List[int]]
    """

    res = [n * [0] for _ in range(n)]
    # print(res)
    left, right = 0, n
    top, bottom = 0, n

    cur_val = 1
    while left < right and top < bottom:
        # process the top row
        for i in range(left, right):
            res[top][i] = cur_val
            cur_val += 1
        top += 1

        # process the right column
        for j in range(top, bottom):
            res[j][right - 1] = cur_val
            cur_val += 1
        right -= 1

        # process the bottom row
        for i in range(right - 1, left - 1, -1):
            res[bottom - 1][i] = cur_val
            cur_val += 1
        bottom -= 1

        # process the left column
        for j in range(bottom - 1, top - 1, -1):
            res[j][left] = cur_val
            cur_val += 1
        left += 1
    return res

if __name__ == '__main__':
    # Example 1
    n = 3
    print(generateMatrix(n))

    # Example 2
    n = 1
    print(generateMatrix(n))