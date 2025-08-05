def maxProduct(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    max_subarray_product = nums[0]
    max_product_so_far = nums[0]
    min_product_so_far = nums[0]

    for i in range(1, len(nums)):
        curr_val = nums[i]
        if curr_val == 0:
            max_product_so_far = 1
            min_product_so_far = 1

        temp = max_product_so_far
        max_product_so_far = max(curr_val, min_product_so_far * curr_val, max_product_so_far * curr_val)
        min_product_so_far = min(curr_val, min_product_so_far * curr_val, temp * curr_val)
        max_subarray_product = max(max_subarray_product, max_product_so_far)

    return max_subarray_product

if __name__ == '__main__':
    # Example 1
    nums = [2, 3, -2, 4]
    print(maxProduct(nums))

    # Example 2
    nums = [-2, 0, -1]
    print(maxProduct(nums))