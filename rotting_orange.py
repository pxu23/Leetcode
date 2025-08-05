from collections import deque

def orangesRotting(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    numFresh = 0
    queue = deque()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                numFresh += 1
            if grid[i][j] == 2:
                queue.append((i, j))

    cnt = 0
    while queue and numFresh > 0:
        n = len(queue)
        if cnt > 0:
            numFresh -= n
        for _ in range(n):
            cur_row, cur_col = queue.popleft()

            # get the adjacent neighbors
            if cur_row - 1 >= 0 and grid[cur_row - 1][cur_col] == 1:
                grid[cur_row - 1][cur_col] = 2
                queue.append((cur_row - 1, cur_col))

            if cur_col - 1 >= 0 and grid[cur_row][cur_col - 1] == 1:
                grid[cur_row][cur_col - 1] = 2
                queue.append((cur_row, cur_col - 1))

            if cur_row + 1 < len(grid) and grid[cur_row + 1][cur_col] == 1:
                grid[cur_row + 1][cur_col] = 2
                queue.append((cur_row + 1, cur_col))

            if cur_col + 1 < len(grid[0]) and grid[cur_row][cur_col + 1] == 1:
                grid[cur_row][cur_col + 1] = 2
                queue.append((cur_row, cur_col + 1))

        if numFresh > 0:
            cnt += 1

    return -1 if numFresh > 0 else cnt

if __name__=="__main__":
    # Example 1
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    print(orangesRotting(grid))

    # Example 2
    grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    print(orangesRotting(grid))

    # Example 3
    grid = [[0, 2]]
    print(orangesRotting(grid))