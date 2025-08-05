def threeSumClosest(nums, target):
    nums.sort()
    closest = float('inf')
    result = float('inf')

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l, r = i + 1, len(nums) - 1

        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if abs(s - target) < closest:
                closest = abs(s - target)
                result = s
            if s > target:
                r -= 1
            elif s < target:
                l += 1
            else:
                return target
    return result

if __name__=="__main__":
    # Example 1
    nums = [-1,2,1,-4]
    target = 1
    res = threeSumClosest(nums, target)
    print(res)

    # Example 2
    nums = [0, 0, 0]
    target = 1
    res = threeSumClosest(nums, target)
    print(res)