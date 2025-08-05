from collections import deque

def nearestExit( maze, entrance):
    """
    :type maze: List[List[str]]
    :type entrance: List[int]
    :rtype: int
    """
    # djikstra with unit edge cost
    m = len(maze)
    n = len(maze[0])

    queue = deque()
    queue.append((entrance, 0))
    maze[entrance[0]][entrance[1]] = "+"

    while queue:
        cur_cell, cur_dist = queue.popleft()

        # look at the neighbors
        cur_row = cur_cell[0]
        cur_col = cur_cell[1]

        if (cur_row == 0 or cur_row == m - 1 or cur_col == 0 or cur_col == n - 1) and cur_cell != entrance:
            return cur_dist

        if cur_row + 1 < m and maze[cur_row + 1][cur_col] != "+":
            queue.append(([cur_row + 1, cur_col], cur_dist + 1))
            maze[cur_row + 1][cur_col] = "+"

        if cur_row - 1 >= 0 and maze[cur_row - 1][cur_col] != "+":
            queue.append(([cur_row - 1, cur_col], cur_dist + 1))
            maze[cur_row - 1][cur_col] = "+"

        if cur_col + 1 < n and maze[cur_row][cur_col + 1] != "+":
            queue.append(([cur_row, cur_col + 1], cur_dist + 1))
            maze[cur_row][cur_col + 1] = "+"

        if cur_col - 1 >= 0 and maze[cur_row][cur_col - 1] != "+":
            queue.append(([cur_row, cur_col - 1], cur_dist + 1))
            maze[cur_row][cur_col - 1] = "+"
    return -1

if __name__=="__main__":
    # Example 1
    maze = [["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]]
    entrance = [1, 0]
    print(nearestExit(maze, entrance))

    # Example 2
    maze = [["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]]
    entrance = [1, 0]
    print(nearestExit(maze, entrance))

    # Example 3
    maze = [[".", "+"]]
    entrance = [0, 0]
    print(nearestExit(maze, entrance))