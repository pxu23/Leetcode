import heapq
import math

def kClosest(points, k):
    """
    :type points: List[List[int]]
    :type k: int
    :rtype: List[List[int]]
    """

    heap = []

    for x, y in points:
        dist = math.sqrt(x ** 2 + y ** 2)
        heapq.heappush(heap, (dist, [x, y]))

    res = []

    for _ in range(k):
        res.append(heapq.heappop(heap)[1])

    return res

if __name__ == '__main__':
    # Example 1
    points = [[1,3],[-2,2]]
    k = 1
    print(kClosest(points, k))

    # Example 2
    points = [[3, 3], [5, -1], [-2, 4]]
    k = 2
    print(kClosest(points, k))