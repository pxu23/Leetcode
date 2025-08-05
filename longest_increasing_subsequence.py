def lengthOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    res = [1] * n

    for i in range(1, n):
        lis_ending_at_i = 1
        for j in range(i):
            if nums[j] < nums[i]:
                lis_ending_at_i = max(lis_ending_at_i, res[j] + 1)
        res[i] = lis_ending_at_i

    return max(res)

if __name__ == '__main__':
    # Example 1
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(lengthOfLIS(nums))

    # Example 2
    nums = [0, 1, 0, 3, 2, 3]
    print(lengthOfLIS(nums))

    # Example 3
    nums = [7, 7, 7, 7, 7, 7, 7]
    print(lengthOfLIS(nums))