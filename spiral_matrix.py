def spiralMatrix(matrix):
    res = []
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    t, b = 0, num_rows
    l, r = 0, num_cols

    while t < b and l < r:
        # top row
        for i in range(l, r):
            res.append(matrix[t][i])
        t += 1

        if t >= b or l >= r:
            break

        # right column
        for i in range(t, b):
            res.append(matrix[i][r - 1])
        r -= 1

        if t >= b or l >= r:
            break

        # bottom row
        for i in range(r - 1, l - 1, -1):
            res.append(matrix[b - 1][i])
        b -= 1

        if t >= b or l >= r:
            break

        # left column
        for i in range(b - 1, t - 1, -1):
            res.append(matrix[i][l])
        l += 1

        if t >= b or l >= r:
            break
    return res

if __name__ == '__main__':
    # Example 1
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(spiralMatrix(matrix))

    # Example 2
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print(spiralMatrix(matrix))