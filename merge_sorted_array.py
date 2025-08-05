def mergeSortedArray(nums1, nums2, m, n):
    last = m + n - 1
    while m > 0 and n > 0:
        if nums1[m - 1] < nums2[n - 1]:
            nums1[last] = nums2[n - 1]
            n -= 1
        else:
            nums1[last] = nums1[m - 1]
            m -= 1
        last -= 1

    while n > 0:
        nums1[last] = nums2[n - 1]
        last -= 1
        n -= 1

if __name__ == '__main__':
    # Example 1
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    mergeSortedArray(nums1, nums2, m, n)
    print(nums1)

    # Example 2
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    mergeSortedArray(nums1, nums2, m, n)
    print(nums1)

    # Example 3
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    mergeSortedArray(nums1, nums2, m, n)
    print(nums1)