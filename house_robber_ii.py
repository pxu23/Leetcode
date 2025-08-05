def rob(nums):
    if len(nums) == 1:
        return nums[0]

    n = len(nums)

    nums_without_first = nums[1:]
    nums_without_last = nums[:-1]

    res_without_first = [0] * (n - 1)
    res_without_last = [0] * (n - 1)

    max_robbed_without_first = 0
    for i in range(n - 1):
        if i == 0:
            res_without_first[i] = nums_without_first[i]
        elif i < 2:
            res_without_first[i] = max(nums_without_first[i], res_without_first[i - 1])
            max_robbed_without_first = max(max_robbed_without_first, res_without_first[i])
        else:
            res_without_first[i] = max(nums_without_first[i] + res_without_first[i - 2], res_without_first[i - 1])
    max_robbed_without_first = max(max_robbed_without_first, res_without_first[i])

    max_robbed_without_second = 0
    for i in range(n - 1):
        if i == 0:
            res_without_last[i] = nums_without_last[i]
        elif i < 2:
            res_without_last[i] = max(nums_without_last[i], res_without_last[i - 1])
        else:
            res_without_last[i] = max(nums_without_last[i] + res_without_last[i - 2], res_without_last[i - 1])

        max_robbed_without_second = max(max_robbed_without_second, res_without_last[i])

    res = max(max_robbed_without_first, max_robbed_without_second)

    return res

if __name__=="__main__":
    # Example 1
    nums = [2, 3, 2]
    print(rob(nums))

    # Example 2
    nums = [1, 2, 3, 1]
    print(rob(nums))

    # Example 3
    nums = [1, 2, 3]
    print(rob(nums))