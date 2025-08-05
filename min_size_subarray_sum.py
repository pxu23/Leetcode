def minSubArrayLen(target, nums):
    """
    :type target: int
    :type nums: List[int]
    :rtype: int
    """
    cur_sum = 0
    i = 0
    j = 0
    min_size = float('inf')

    while j < len(nums):
        cur_sum += nums[j]
        while cur_sum >= target:
            min_size = min(min_size, j - i + 1)
            cur_sum -= nums[i]
            i += 1
        j += 1

    return min_size if min_size != float('inf') else 0

if __name__ == '__main__':
    # Example 1
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    print(minSubArrayLen(target, nums))

    # Example 2
    target = 4
    nums = [1, 4, 4]
    print(minSubArrayLen(target, nums))

    # Example 3
    target = 11
    nums = [1, 1, 1, 1, 1, 1, 1, 1]
    print(minSubArrayLen(target, nums))