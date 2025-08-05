def fourSum(nums, target):
    res = []
    nums.sort()

    for i in range(len(nums) - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        for j in range(i + 1, len(nums) - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            # two sum II
            l, r = j + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[j] + nums[l] + nums[r]
                if s > target:
                    r -= 1
                elif s < target:
                    l += 1
                else:
                    res.append([nums[i], nums[j], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
    return res

if __name__ == '__main__':
    # Example 1
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    print(fourSum(nums, target))

    # Example 2
    nums = [2, 2, 2, 2, 2]
    target = 8
    print(fourSum(nums, target))