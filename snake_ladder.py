from collections import deque

def snakesAndLadders(board) -> int:
    queue = deque()
    queue.append(1)
    n = len(board)
    dest = n ** 2

    def get_row_col_num(number):
        row_idx = n - 1 - (number - 1) // n
        if ((number - 1) // n) % 2 == 0:
            col_idx = (number - 1) % n
        else:
            col_idx = (n - 1) - ((number - 1) % n)

        return row_idx, col_idx

    min_moves = 0
    visited = set()
    visited.add(1)
    while queue:
        q_len = len(queue)
        for _ in range(q_len):
            cur_node = queue.popleft()

            if cur_node == dest:
                return min_moves

            for next_val in range(cur_node + 1, min(cur_node + 6, dest) + 1):

                # check if snake or ladder present
                row_idx, col_idx = get_row_col_num(next_val)

                if board[row_idx][col_idx] != -1:
                    next_val = board[row_idx][col_idx]

                if next_val in visited:
                    continue

                queue.append(next_val)
                visited.add(next_val)

        min_moves += 1

    return -1

if __name__=="__main__":
    # Example 1
    board = [[-1, -1, -1, -1, -1, -1],
             [-1, -1, -1, -1, -1, -1],
             [-1, -1, -1, -1, -1, -1],
             [-1, 35, -1, -1, 13, -1],
             [-1, -1, -1, -1, -1, -1],
             [-1, 15, -1, -1, -1, -1]]
    print(snakesAndLadders(board))

    # Example 2
    board = [[-1, -1], [-1, 3]]
    print(snakesAndLadders(board))