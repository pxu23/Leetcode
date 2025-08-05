def merge(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: List[List[int]]
    """
    intervals.sort()

    stack = [intervals[0]]

    def is_overlap(interval1, interval2):
        return interval1[1] >= interval2[0]

    for i in range(1, len(intervals)):
        cur_interval = intervals[i]
        cur_interval_stack = stack[-1]
        if is_overlap(cur_interval_stack, cur_interval):
            merged_interval = [min(cur_interval[0], cur_interval_stack[0]),
                               max(cur_interval[1], cur_interval_stack[1])]
            stack.pop()
            stack.append(merged_interval)
        else:
            stack.append(cur_interval)

    return stack

if __name__=="__main__":
    # Example 1
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(merge(intervals))

    # Example 2
    intervals = [[1, 4], [4, 5]]
    print(merge(intervals))