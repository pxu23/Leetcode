def minCostClimbingStairs(cost):
    """
    :type cost: List[int]
    :rtype: int
    """

    # min cost
    min_cost = len(cost) * [0]

    # last stair step (base case)
    n = len(cost)
    min_cost[n - 1] = cost[n - 1]
    min_cost[n - 2] = min(cost[n - 2] + min_cost[n - 1], cost[n - 2])
    for j in range(len(cost) - 3, -1, -1):
        min_cost[j] = min(cost[j] + min_cost[j + 1], cost[j] + min_cost[j + 2])

    return min(min_cost[0], min_cost[1])

if __name__ == '__main__':
    # Example 1
    cost = [10,15,20]
    print(minCostClimbingStairs(cost))

    # Example 2
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    print(minCostClimbingStairs(cost))