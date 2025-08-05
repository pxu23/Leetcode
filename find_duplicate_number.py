def findDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    nums.sort()

    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return nums[i]

    return -1

if __name__ == '__main__':
    # Example 1
    nums = [1, 3, 4, 2, 2]
    print(findDuplicate(nums))

    # Example 2
    nums = [3, 1, 3, 4, 2]
    print(findDuplicate(nums))

    # Example 3
    nums = [3, 3, 3, 3, 3]
    print(findDuplicate(nums))