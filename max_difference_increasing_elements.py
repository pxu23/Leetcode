def maximumDifference(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    max_diff = -1
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            diff = nums[j] - nums[i]
            if diff > 0:
                max_diff = max(diff, max_diff)

    return max_diff

if __name__ == '__main__':
    # Example 1
    nums = [7, 1, 5, 4]
    print(maximumDifference(nums))

    # Example 2
    nums = [9, 4, 3, 2]
    print(maximumDifference(nums))

    # Example 3
    nums = [1, 5, 2, 10]
    print(maximumDifference(nums))