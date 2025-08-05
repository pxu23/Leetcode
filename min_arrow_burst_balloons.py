def findMinArrowShots(points):
    """
    :type points: List[List[int]]
    :rtype: int
    """
    points.sort()
    left = points[0][0]
    right = points[0][1]

    cnt = 1
    for i in range(1, len(points)):
        cur_point = points[i]
        if (cur_point[1] >= left and cur_point[1] <= right) or (cur_point[0] >= left and cur_point[0] <= right):
            left = max(left, cur_point[0])
            right = min(right, cur_point[1])
            continue

        cnt += 1
        left = points[i][0]
        right = points[i][1]

    return cnt

if __name__=='__main__':
    # Example 1
    points = [[10, 16], [2, 8], [1, 6], [7, 12]]
    print(findMinArrowShots(points))

    # Example 2
    points = [[1, 2], [3, 4], [5, 6], [7, 8]]
    print(findMinArrowShots(points))

    # Example 3
    points = [[1, 2], [2, 3], [3, 4], [4, 5]]
    print(findMinArrowShots(points))