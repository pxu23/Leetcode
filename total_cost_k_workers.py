import heapq

def totalCost(costs, k, candidates):
    """
    :type costs: List[int]
    :type k: int
    :type candidates: int
    :rtype: int
    """

    heap = []
    n = len(costs)

    front_end = -1
    for i in range(min(candidates, n)):
        heapq.heappush(heap, (costs[i], i))
        front_end += 1

    rear_end = n
    for i in range(n - 1, max(candidates - 1, n - candidates - 1), -1):
        heapq.heappush(heap, (costs[i], i))
        rear_end -= 1

    total_cost = 0
    for _ in range(k):
        cur_cost, cur_idx = heapq.heappop(heap)

        if cur_idx <= front_end:
            front_end += 1

            if front_end < rear_end:
                heapq.heappush(heap, (costs[front_end], front_end))

        if cur_idx >= rear_end:
            rear_end -= 1
            if front_end < rear_end:
                heapq.heappush(heap, (costs[rear_end], rear_end))

        total_cost += cur_cost
    return total_cost

if __name__=="__main__":
    # Example 1
    costs = [17, 12, 10, 2, 7, 2, 11, 20, 8]
    k = 3
    candidates = 4
    print(totalCost(costs, k, candidates))

    # Example 2
    costs = [1, 2, 4, 1]
    k = 3
    candidates = 3
    print(totalCost(costs, k, candidates))