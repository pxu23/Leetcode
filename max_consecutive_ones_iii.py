def longestOnes(nums, k):
    l = 0
    r = 0
    num_bits_flipped = 0
    res = 0
    while r < len(nums):
        while r < len(nums) and num_bits_flipped <= k:
            if nums[r] == 0:
                num_bits_flipped += 1
            r += 1

        if num_bits_flipped <= k:
            res = max(res, r - l)
        else:
            res = max(res, r - l - 1)

        while l < r and num_bits_flipped > k:
            if nums[l] == 0:
                num_bits_flipped -= 1

            l += 1
    return res

if __name__=="__main__":
    # Example 1
    nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    k = 2
    print(longestOnes(nums, k))

    # Example 2
    nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
    k = 3
    print(longestOnes(nums, k))