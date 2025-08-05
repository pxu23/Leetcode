def findMaxConsecutiveOnes(nums):
    res = 0
    num_cons_ones = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            num_cons_ones += 1
        else:
            res = max(res, num_cons_ones)
            num_cons_ones = 0

    res = max(res, num_cons_ones)
    return res

if __name__ == '__main__':
    # Example 1
    nums = [1, 1, 0, 1, 1, 1]
    print(findMaxConsecutiveOnes(nums))

    # Example 2
    nums = [1, 0, 1, 1, 0, 1]
    print(findMaxConsecutiveOnes(nums))