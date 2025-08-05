def insert(intervals, newInterval):
    """
    :type intervals: List[List[int]]
    :type newInterval: List[int]
    :rtype: List[List[int]]
    """
    if len(intervals) == 0:
        return [newInterval]

    def is_overlap(interval1, interval2):
        return interval1[1] >= interval2[0]

    n = len(intervals)
    low = 0
    high = n

    stack = []
    while low <= high:
        mid = (low + high) // 2
        # (low)
        # print(mid)
        # print(high)
        if mid == 0:
            if newInterval[0] > intervals[mid][0]:
                low = mid + 1
            else:
                intervals.insert(mid, newInterval)

                stack = [newInterval]
                for j in range(mid + 1, len(intervals)):
                    if is_overlap(stack[-1], intervals[j]):
                        merged_pair = [min(stack[-1][0], intervals[j][0]),
                                       max(stack[-1][1], intervals[j][1])]
                        stack.pop()
                        stack.append(merged_pair)
                    else:
                        stack.append(intervals[j])
                return stack
        if mid == n:
            if newInterval[0] > intervals[mid - 1][0]:
                for j in range(mid):
                    stack.append(intervals[j])
                intervals.insert(mid, newInterval)

                if is_overlap(stack[-1], newInterval):
                    merged_pair = [min(stack[-1][0], newInterval[0]),
                                   max(stack[-1][1], newInterval[1])]
                    stack.pop()
                    stack.append(merged_pair)
                else:
                    stack.append(newInterval)
                return stack
            else:
                high = mid

        if intervals[mid - 1][0] <= newInterval[0] and newInterval[0] <= intervals[mid][0]:
            for j in range(mid):
                stack.append(intervals[j])

            intervals.insert(mid, newInterval)

            for j in range(mid, len(intervals)):
                if is_overlap(stack[-1], intervals[j]):
                    # print(stack[-1])
                    # print(intervals[j])
                    merged_pair = [min(stack[-1][0], intervals[j][0]),
                                   max(stack[-1][1], intervals[j][1])]
                    stack.pop()
                    stack.append(merged_pair)
                else:
                    stack.append(intervals[j])
            return stack

        if newInterval[0] > intervals[mid][0]:
            low = mid + 1

        if newInterval[0] < intervals[mid - 1][0]:
            high = mid
    return None

if __name__=="__main__":
    # Example 1
    intervals = [[1, 3], [6, 9]]
    newInterval = [2, 5]
    print(insert(intervals, newInterval))

    # Example 2
    intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    newInterval = [4, 8]
    print(insert(intervals, newInterval))
