def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """

    cnt = 0
    m = len(grid)
    n = len(grid[0])

    def dfs(i, j):
        stack = []
        stack.append((i, j))
        grid[i][j] = "0"

        while len(stack) > 0:
            r, c = stack.pop()
            if c + 1 < n and grid[r][c + 1] == "1":
                stack.append((r, c + 1))
                grid[r][c + 1] = "0"

            if c - 1 >= 0 and grid[r][c - 1] == "1":
                stack.append((r, c - 1))
                grid[r][c - 1] = "0"

            if r + 1 < m and grid[r + 1][c] == "1":
                stack.append((r + 1, c))
                grid[r + 1][c] = "0"

            if r - 1 >= 0 and grid[r - 1][c] == "1":
                stack.append((r - 1, c))
                grid[r - 1][c] = "0"

    for i in range(m):
        for j in range(n):
            if grid[i][j] == "0":
                continue

            # perform the dfs
            dfs(i, j)

            cnt += 1

    return cnt

if __name__=="__main__":
    # Example 1
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    print(numIslands(grid))

    # Example 2
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    print(numIslands(grid))