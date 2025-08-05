def findPeakElement(nums):
    if len(nums) == 1:
        return 0

    if nums[1] < nums[0]:
        return 0

    for i in range(1, len(nums) - 1):
        if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
            return i

    if nums[len(nums) - 1] > nums[len(nums) - 2]:
        return len(nums) - 1

    return -1

if __name__=="__main__":
    # Example 1
    nums = [1, 2, 3, 1]
    print(findPeakElement(nums))

    # Example 2
    nums = [1, 2, 1, 3, 5, 6, 4]
    print(findPeakElement(nums))
    