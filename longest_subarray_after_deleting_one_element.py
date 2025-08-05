def longestSubarray(nums):
    l = 0
    r = 0
    res = 0

    while r < len(nums):
        num_zeros = 0
        while r < len(nums) and num_zeros < 2:
            if nums[r] == 0:
                num_zeros += 1
                if num_zeros >= 2:
                    break
            r += 1
        res = max(res, r - l - 1)

        while l < r and num_zeros > 1:
            if nums[l] == 0:
                num_zeros -= 1
            l += 1

    return res

if __name__=="__main__":
    # Example 1
    nums = [0,1,1,1,0,1,1,0,1]
    print(longestSubarray(nums))

    # Example 2
    nums = [1, 1, 0, 1]
    print(longestSubarray(nums))

    # Example 3
    nums = [1, 1, 1]
    print(longestSubarray(nums))