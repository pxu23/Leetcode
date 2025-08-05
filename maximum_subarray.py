def max_subarray(nums):
    """
        Given an integer array nums, find the contiguous subarray with largest sum
        and return its subarray
        :param nums:the input integer array
        :return: the maximum subarray sum
    """
    max_subarray_sum = float('-inf')
    cur_subarray_sum = float('-inf')

    for i in range(len(nums)):
        cur_val = nums[i]
        cur_subarray_sum = max(cur_subarray_sum + cur_val, cur_val)
        max_subarray_sum = max(max_subarray_sum, cur_subarray_sum)
    return max_subarray_sum

if __name__ == '__main__':
    # Example 1
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(max_subarray(nums))

    # Example 2
    nums = [1]
    print(max_subarray(nums))

    # Example 3
    nums = [5, 4, -1, 7, 8]
    print(max_subarray(nums))