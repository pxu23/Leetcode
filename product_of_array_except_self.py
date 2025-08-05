def productExceptSelf(nums):
    left_cumulative_prod = [1] * len(nums)
    right_cumulative_prod = [1] * len(nums)

    left_cumulative_prod[0] = nums[0]
    for i in range(1, len(nums)):
        left_cumulative_prod[i] = nums[i] * left_cumulative_prod[i - 1]

    n = len(nums)
    right_cumulative_prod[n - 1] = nums[n - 1]
    for i in range(n - 2, -1, -1):
        right_cumulative_prod[i] = nums[i] * right_cumulative_prod[i + 1]

    res = [1] * n
    res[0] = right_cumulative_prod[1]
    res[-1] = left_cumulative_prod[-2]
    for i in range(1, n - 1):
        res[i] = left_cumulative_prod[i - 1] * right_cumulative_prod[i + 1]

    return res

if __name__ == '__main__':
    # Example 1
    nums = [1, 2, 3, 4]
    print(productExceptSelf(nums))

    # Example 2
    nums = [-1, 1, 0, -3, 3]
    print(productExceptSelf(nums))