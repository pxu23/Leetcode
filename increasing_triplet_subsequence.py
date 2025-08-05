def increasingTriplet(nums):
    first = float('inf')
    second = float('inf')

    for i in range(len(nums)):
        if nums[i] <= first:
            first = nums[i]
        elif nums[i] <= second:
            second = nums[i]

        if nums[i] > first and nums[i] > second:
            return True
    return False

if __name__=="__main__":
    # Example 1
    nums = [1, 2, 3, 4, 5]
    print(increasingTriplet(nums))

    # Example 2
    nums = [5, 4, 3, 2, 1]
    print(increasingTriplet(nums))

    # Example 3
    nums = [2, 1, 5, 0, 4, 6]
    print(increasingTriplet(nums))