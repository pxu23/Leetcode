def setZeroes(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    numRows = len(matrix)
    numCols = len(matrix[0])

    rows_with_zero_hashmap = {}
    cols_with_zero_hashmap = {}

    for i in range(numRows):
        for j in range(numCols):
            if matrix[i][j] == 0:
                rows_with_zero_hashmap[i] = 1
                cols_with_zero_hashmap[j] = 1

    for i in range(numRows):
        for j in range(numCols):
            if (rows_with_zero_hashmap.get(i, 0) == 1 or
                    cols_with_zero_hashmap.get(j, 0) == 1):
                matrix[i][j] = 0

if __name__=="__main__":
    # Example 1
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    setZeroes(matrix)
    print(matrix)

    # Example 2
    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    setZeroes(matrix)
    print(matrix)