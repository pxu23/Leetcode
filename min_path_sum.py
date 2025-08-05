def minPathSum(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    m = len(grid)
    n = len(grid[0])
    min_path_sum = [n * [0] for _ in range(m)]
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if i == m - 1 and j == n - 1:
                min_path_sum[i][j] = grid[i][j]
            elif i == m - 1:
                min_path_sum[i][j] = grid[i][j] + min_path_sum[i][j + 1]
            elif j == n - 1:
                min_path_sum[i][j] = grid[i][j] + min_path_sum[i + 1][j]
            else:
                min_path_sum[i][j] = min(grid[i][j] + min_path_sum[i + 1][j], grid[i][j] + min_path_sum[i][j + 1])
    return min_path_sum[0][0]

if __name__ == '__main__':
    # Example 1
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    print(minPathSum(grid))

    # Example 2
    grid = [[1, 2, 3], [4, 5, 6]]
    print(minPathSum(grid))