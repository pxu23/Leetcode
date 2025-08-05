def summaryRanges(nums):
    """
    :type nums: List[int]
    :rtype: List[str]
    """
    if len(nums) == 0:
        return []

    res = []

    left = 0
    right = 0

    while right < len(nums):
        while right < len(nums) - 1 and nums[right + 1] == nums[right] + 1:
            right += 1
        if left != right:
            interval = str(nums[left]) + "->" + str(nums[right])
        else:
            interval = str(nums[left])
        res.append(interval)
        left = right + 1
        right = right + 1
    return res

if __name__=="__main__":
    # Example 1
    nums = [0, 1, 2, 4, 5, 7]
    print(summaryRanges(nums))

    # Example 2
    nums = [0, 2, 3, 4, 6, 8, 9]
    print(summaryRanges(nums))