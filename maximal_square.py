def maximalSquare(matrix) -> int:
    m = len(matrix)
    n = len(matrix[0])
    max_square_length = 0
    cache = [[0] * n for _ in range(m)]
    for j in range(n - 1, -1, -1):
        for i in range(m - 1, -1, -1):
            if j == n - 1:
                cache[i][j] = 1 if matrix[i][j] == "1" else 0
                max_square_length = max(max_square_length, cache[i][j])
                continue
            if i == m - 1:
                cache[i][j] = 1 if matrix[i][j] == "1" else 0
                max_square_length = max(max_square_length, cache[i][j])
                continue

            if matrix[i][j] == "0":
                cache[i][j] = 0
                max_square_length = max(max_square_length, cache[i][j])
                continue

            cache[i][j] = min(int(cache[i + 1][j]), int(cache[i][j + 1]), int(cache[i + 1][j + 1])) + 1
            max_square_length = max(max_square_length, cache[i][j])

    max_area = max_square_length ** 2
    return max_area

if __name__=="__main__":
    # Example 1
    matrix = [["1", "0", "1", "0", "0"],
              ["1", "0", "1", "1", "1"],
              ["1", "1", "1", "1", "1"],
              ["1", "0", "0", "1", "0"]]
    print(maximalSquare(matrix))

    # Example 2
    matrix = [["0", "1"], ["1", "0"]]
    print(maximalSquare(matrix))

    # Example 3
    matrix = [["0"]]
    print(maximalSquare(matrix))