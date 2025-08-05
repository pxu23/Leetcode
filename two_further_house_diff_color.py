def maxDistance(colors):
    """
    :type colors: List[int]
    :rtype: int
    """
    max_dist = 0
    for i in range(len(colors) - 1):
        for j in range(i + 1, len(colors)):
            if colors[i] != colors[j]:
                dist = abs(j - i)
                max_dist = max(max_dist, dist)

    return max_dist

if __name__ == '__main__':
    # Example 1
    colors = [1, 1, 1, 6, 1, 1, 1]
    print(maxDistance(colors))

    # Example 2
    colors = [1, 8, 3, 8, 3]
    print(maxDistance(colors))

    # Example 3
    colors = [0, 1]
    print(maxDistance(colors))