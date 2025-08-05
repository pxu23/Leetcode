def exist(board, word):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    """
    m = len(board)
    n = len(board[0])

    def dfs(row, col, index):

        if board[row][col] != word[index]:
            return False

        if index == len(word) - 1 and board[row][col] == word[index]:
            return True

        temp = board[row][col]
        board[row][col] = "#"
        for row_offset, col_offset in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row = row + row_offset
            new_col = col + col_offset
            if new_row >= m or new_row < 0:
                continue
            if new_col >= n or new_col < 0:
                continue
            if dfs(new_row, new_col, index + 1):
                return True
        board[row][col] = temp
        return False

    for i in range(m):
        for j in range(n):
            if not word.startswith(board[i][j]):
                continue

            if dfs(i, j, 0):
                return True

    return False

if __name__=="__main__":
    # Example 1
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    print(exist(board, word))

    # Example 2
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "SEE"
    print(exist(board, word))

    # Example 3
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCB"
    print(exist(board, word))