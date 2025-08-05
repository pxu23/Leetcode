# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

def construct(grid):
    if len(grid) == 1:
        return Node(grid[0][0], True, None, None, None, None)

    isLeaf = True
    val = grid[0][0]
    visited = set()
    for i in range(len(grid)):
        for j in range(len(grid)):
            visited.add(grid[i][j])
            val = grid[i][j]

    if len(visited) > 1:
        isLeaf = False

    if isLeaf:
        return Node(val, isLeaf, None, None, None, None)

    mid = int(len(grid) / 2)
    top_left_grid = []
    for i in range(mid):
        top_left_grid.append([])
        for j in range(mid):
            top_left_grid[i].append(grid[i][j])

    top_right_grid = []
    for i in range(mid):
        top_right_grid.append([])
        for j in range(mid, len(grid)):
            top_right_grid[i].append(grid[i][j])

    bottom_left_grid = []
    for i in range(mid, len(grid)):
        bottom_left_grid.append([])
        for j in range(mid):
            bottom_left_grid[i - mid].append(grid[i][j])

    bottom_right_grid = []
    for i in range(mid, len(grid)):
        bottom_right_grid.append([])
        for j in range(mid, len(grid)):
            bottom_right_grid[i - mid].append(grid[i][j])

    top_left = construct(top_left_grid)
    top_right = construct(top_right_grid)
    bottom_left = construct(bottom_left_grid)
    bottom_right = construct(bottom_right_grid)

    node = Node(val, isLeaf, top_left, top_right, bottom_left, bottom_right)

    return node