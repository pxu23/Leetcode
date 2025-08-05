def uniquePaths(m, n):
    unique_paths = {}
    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0:
                unique_paths[i, j] = 1
            else:
                unique_paths[i,j] = unique_paths[i-1, j] + unique_paths[i, j-1]
    return unique_paths[m - 1, n - 1]

if __name__ == '__main__':
    # Example 1
    m = 3
    n = 7
    print(uniquePaths(m, n))

    # Example 2
    m = 3
    n = 2
    print(uniquePaths(m, n))