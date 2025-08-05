def rotate(nums, k):
    k = k % len(nums)
    l, r = 0, len(nums) - 1
    # reverse the entrie array
    while l < r:
        # swap nums[l] and nums[r]
        temp = nums[l]
        nums[l] = nums[r]
        nums[r] = temp
        l += 1
        r -= 1

    # then reverse the first k elements of reversed array
    l, r = 0, k - 1
    while l < r:
        temp = nums[l]
        nums[l] = nums[r]
        nums[r] = temp
        l += 1
        r -= 1

    # then reverse the remaining elements of reversed array
    l, r = k , len(nums) - 1
    while l < r:
        temp = nums[l]
        nums[l] = nums[r]
        nums[r] = temp
        l += 1
        r -= 1

if __name__ == '__main__':
    # Example 1
    nums = [1,2,3,4,5,6,7]
    k = 3
    rotate(nums, k)
    print(nums)

    # Example 2
    nums = [-1, -100, 3, 99]
    k = 2
    rotate(nums, k)
    print(nums)