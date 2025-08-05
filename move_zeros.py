def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    i = 0

    for n in nums:
        if n != 0:
            nums[i] = n
            i += 1

    for j in range(i, len(nums)):
        nums[j] = 0

if __name__ == '__main__':
    # Example 1
    nums = [0, 1, 0, 3, 12]
    moveZeroes(nums)
    print(nums)

    # Example 2
    nums = [0]
    moveZeroes(nums)
    print(nums)