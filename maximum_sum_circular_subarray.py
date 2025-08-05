def maxSubarraySumCircular(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    max_subarray_sum = float('-inf')
    min_subarray_sum = float('inf')
    n = len(nums)

    total_sum = 0
    cur_subarray_sum_min = 0
    cur_subarray_sum_max = 0
    for val in nums:
        total_sum += val
        cur_subarray_sum_max = max(cur_subarray_sum_max + val, val)
        cur_subarray_sum_min = min(cur_subarray_sum_min + val, val)
        max_subarray_sum = max(max_subarray_sum, cur_subarray_sum_max)
        min_subarray_sum = min(min_subarray_sum, cur_subarray_sum_min)

    if total_sum - min_subarray_sum == 0:
        return max_subarray_sum
    return max(max_subarray_sum, total_sum - min_subarray_sum)

if __name__ == '__main__':
    # Example 1
    nums = [1, -2, 3, -2]
    print(maxSubarraySumCircular(nums))

    # Example 2
    nums = [5, -3, 5]
    print(maxSubarraySumCircular(nums))

    # Example 3
    nums = [-3, -2, -3]
    print(maxSubarraySumCircular(nums))