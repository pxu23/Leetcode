def eraseOverlapIntervals(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: int
    """
    intervals.sort(key = lambda x: x[1])

    def is_overlap(interval1, interval2):
        return interval1[1] > interval2[0]

    stack = [intervals[0]]

    cnt = 0
    for i in range(1, len(intervals)):
        cur_point = intervals[i]

        if is_overlap(stack[-1], cur_point):
            cnt += 1
            continue

        stack.append(cur_point)

    return cnt

if __name__=='__main__':
    # Example 1
    intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
    print(eraseOverlapIntervals(intervals))

    # Example 2
    intervals = [[1, 2], [1, 2], [1, 2]]
    print(eraseOverlapIntervals(intervals))

    # Example 3
    intervals = [[1, 2], [2, 3]]
    print(eraseOverlapIntervals(intervals))
