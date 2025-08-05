def threeSum(nums):
    """

    :param nums:
    :return:
    """
    res = []
    nums.sort()

    for i in range(len(nums)):
        # skip duplicates
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l, r = i + 1, len(nums) - 1

        # Two Sum II
        while l < r:
            cur_sum = nums[i] + nums[l] + nums[r]
            if cur_sum == 0:
                res.append([nums[i], nums[l], nums[r]])
                l += 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
            elif cur_sum < 0:
                l += 1
            elif cur_sum > 0:
                r -= 1

    return res

if __name__ == "__main__":
    # Example 1
    nums = [-1, 0, 1, 2, -1, -4]
    res = threeSum(nums)
    print(res)

    # Example 2
    nums = [0, 1, 1]
    res = threeSum(nums)
    print(res)

    # Example 3
    nums = [0, 0, 0]
    res = threeSum(nums)
    print(res)