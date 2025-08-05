def equalPairs(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    numRows = len(grid)
    numCols = len(grid[0])

    hashmap_rows = {}
    hashmap_cols = {}

    for i in range(numRows):
        row = []
        for j in range(numCols):
            row.append(grid[i][j])
        hashmap_rows[i] = row

    for j in range(numCols):
        col = []
        for i in range(numRows):
            col.append(grid[i][j])
        hashmap_cols[j] = col

    count = 0
    for i in range(numRows):
        for j in range(numCols):
            if hashmap_rows[i] == hashmap_cols[j]:
                count += 1
    return count

if __name__ == '__main__':
    # Example 1
    grid = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]
    print(equalPairs(grid))

    # Example 2
    grid = [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]
    print(equalPairs(grid))