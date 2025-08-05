def uniquePathsWithObstacles(obstacleGrid):
    """
    :type obstacleGrid: List[List[int]]
    :rtype: int
    """
    numRows = len(obstacleGrid)
    numCols = len(obstacleGrid[0])
    num_unique_path = [numCols * [0] for _ in range(numRows)]

    encountered_obstacle_edge = False
    if obstacleGrid[0][0] == 1:
        num_unique_path[0][0] = 0
    else:
        num_unique_path[0][0] = 1

    # top row
    for j in range(1, numCols):
        if encountered_obstacle_edge:
            num_unique_path[0][j] = 0
        elif obstacleGrid[0][j] == 1:
            num_unique_path[0][j] = 0
            encountered_obstacle_edge = True
        else:
            num_unique_path[0][j] = num_unique_path[0][j - 1]

    # leftmost column
    encountered_obstacle_edge = False
    for i in range(1, numRows):
        if encountered_obstacle_edge:
            num_unique_path[i][0] = 0
        elif obstacleGrid[i][0] == 1:
            num_unique_path[i][0] = 0
            encountered_obstacle_edge = True
        else:
            num_unique_path[i][0] = num_unique_path[i - 1][0]

    for i in range(1, numRows):
        for j in range(1, numCols):
            if obstacleGrid[i][j] == 1:
                num_unique_path[i][j] = 0
            else:
                num_unique_path[i][j] = num_unique_path[i][j - 1] + num_unique_path[i - 1][j]

    return num_unique_path[numRows - 1][numCols - 1]

if __name__ == '__main__':
    # Example 1
    obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    print(uniquePathsWithObstacles(obstacleGrid))

    # Example 2
    obstacleGrid = [[0, 1], [0, 0]]
    print(uniquePathsWithObstacles(obstacleGrid))