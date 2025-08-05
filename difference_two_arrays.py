def findDifference(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[List[int]]
    """
    # hashmap for nums1
    hashmap_nums1 = {}

    # hashmap for nums2
    hashmap_nums2 = {}

    for i, n1 in enumerate(nums1):
        hashmap_nums1[n1] = i

    for i, n2 in enumerate(nums2):
        hashmap_nums2[n2] = i

    answer0 = []
    answer1 = []

    for k1 in hashmap_nums1:
        if k1 not in hashmap_nums2:
            answer0.append(k1)

    for k2 in hashmap_nums2:
        if k2 not in hashmap_nums1:
            answer1.append(k2)

    result = [answer0, answer1]

    return result

if __name__=="__main__":
    # Example 1
    nums1 = [1, 2, 3]
    nums2 = [2, 4, 6]
    print(findDifference(nums1, nums2))

    # Example 2
    nums1 = [1, 2, 3, 3]
    nums2 = [1, 1, 2, 2]
    print(findDifference(nums1, nums2))