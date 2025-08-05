import copy


def gameOfLife(board) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    copied_board = copy.deepcopy(board)

    for i in range(len(board)):
        for j in range(len(board[0])):
            num_live_neighbors = 0
            for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]:
                neighbor_x = i + dx
                neighbor_y = j + dy
                if neighbor_x < 0 or neighbor_x >= len(board):
                    continue

                if neighbor_y < 0 or neighbor_y >= len(board[0]):
                    continue

                if copied_board[neighbor_x][neighbor_y] == 1:
                    num_live_neighbors += 1
            print(num_live_neighbors)
            if board[i][j] == 1:
                if num_live_neighbors < 2 or num_live_neighbors > 3:
                    board[i][j] = 0
            else:
                if num_live_neighbors == 3:
                    board[i][j] = 1
if __name__=="__main__":
    # Example 1
    board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    gameOfLife(board)
    print(board)