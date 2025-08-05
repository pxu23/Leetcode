import heapq
def kSmallestPairs(nums1, nums2, k):
    heap = [(nums1[0] + nums2[0], 0, 0)]

    res = []
    visited = set()
    for _ in range(k):
        cur_sum, i, j = heapq.heappop(heap)

        res.append([nums1[i], nums2[j]])
        if i + 1 < len(nums1) and not (i + 1, j) in visited:
            heapq.heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
            visited.add((i + 1, j))
        if j + 1 < len(nums2) and not (i, j + 1) in visited:
            heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
            visited.add((i, j + 1))
    return res

if __name__ == '__main__':
    # Example 1
    nums1 = [1, 7, 11]
    nums2 = [2, 4, 6]
    k = 3
    print(kSmallestPairs(nums1, nums2, k))

    # Example 2
    nums1 = [1, 1, 2]
    nums2 = [1, 2, 3]
    k = 2
    print(kSmallestPairs(nums1, nums2, k))