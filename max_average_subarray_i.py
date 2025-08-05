def findMaxAverage(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: float
    """

    l = 0
    r = k - 1
    cur_sum = 0
    for i in range(l, r + 1):
        cur_sum += nums[i]
    max_average = float(cur_sum) / k

    while r < len(nums) - 1:
        cur_sum -= nums[l]

        l += 1
        r += 1

        cur_sum += nums[r]

        max_average = max(max_average, float(cur_sum) / k)

    return max_average

if __name__ == '__main__':
    # Example 1
    nums = [1, 12, -5, -6, 50, 3]
    k = 4
    print(findMaxAverage(nums, k))

    # Example 2
    nums = [5]
    k = 1
    print(findMaxAverage(nums, k))