def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    max_reward = [0] * len(nums)

    max_reward[0] = nums[0]

    for i in range(1, len(nums)):
        if i - 2 < 0:
            max_reward[i] = max(nums[i], max_reward[i - 1])
        else:
            max_reward[i] = max(nums[i] + max_reward[i - 2], max_reward[i - 1])

    return max_reward[len(nums) - 1]

if __name__=="__main__":
    # Example 1
    nums = [1, 2, 3, 1]
    print(rob(nums))

    # Example 2
    nums = [2, 7, 9, 3, 1]
    print(rob(nums))