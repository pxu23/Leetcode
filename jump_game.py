def canJump(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    n = len(nums)
    goal = n - 1

    for i in range(n - 1, -1, -1):
        max_jump = nums[i]
        if i + max_jump >= goal:
            goal = i

    return True if goal == 0 else False

if __name__=="__main__":
    # Example 1
    nums = [2, 3, 1, 1, 4]
    print(canJump(nums))

    # Example 2
    nums = [3,2,1,0,4]
    print(canJump(nums))