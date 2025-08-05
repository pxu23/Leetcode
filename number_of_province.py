def findCircleNum(isConnected):
    """
    :type isConnected: List[List[int]]
    :rtype: int
    """
    cnt = 0
    stack = []
    visited = set()
    n = len(isConnected)

    for i in range(n):
        if i in visited:
            continue

        # perform the dfs starting from i
        stack = [i]
        visited.add(i)
        while stack:
            cur = stack.pop()

            for j in range(n):
                if isConnected[cur][j] == 1 and j != cur and j not in visited:
                    stack.append(j)
                    visited.add(j)
        cnt += 1

    return cnt

if __name__ == '__main__':
    # Example 1
    isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    print(findCircleNum(isConnected))

    # Example 2
    isConnected = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    print(findCircleNum(isConnected))