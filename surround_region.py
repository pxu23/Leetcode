from collections import defaultdict

def solve(board):
    """
    :type board: List[List[str]]
    :rtype: None Do not return anything, modify board in-place instead.
    """
    can_surround = defaultdict(lambda: True)

    region_idx = 1
    regions = {}

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != "O":
                continue

            stack = [(i, j)]
            while stack:
                cur_row, cur_col = stack.pop()
                regions[(cur_row, cur_col)] = region_idx
                if cur_row == 0 or cur_col == 0 or cur_row == len(board) - 1 or cur_col == len(board[0]) - 1:
                    can_surround[region_idx] = False
                if cur_row + 1 < len(board) and board[cur_row + 1][cur_col] == "O":
                    stack.append((cur_row + 1, cur_col))
                    board[cur_row + 1][cur_col] = "#"

                if cur_row - 1 >= 0 and board[cur_row - 1][cur_col] == "O":
                    stack.append((cur_row - 1, cur_col))
                    board[cur_row - 1][cur_col] = "#"

                if cur_col + 1 < len(board[0]) and board[cur_row][cur_col + 1] == "O":
                    stack.append((cur_row, cur_col + 1))
                    board[cur_row][cur_col + 1] = "#"

                if cur_col - 1 >= 0 and board[cur_row][cur_col - 1] == "O":
                    stack.append((cur_row, cur_col - 1))
                    board[cur_row][cur_col - 1] = "#"
            region_idx += 1
    # (regions)
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "X":
                continue

            region_idx = regions[(i, j)]
            if can_surround[region_idx]:
                board[i][j] = "X"
            else:
                board[i][j] = "O"

if __name__=="__main__":
    # Example 1
    board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
    solve(board)
    print(board)

    # Example 2
    board = [["X"]]
    solve(board)
    print(board)