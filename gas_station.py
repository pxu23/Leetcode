def canCompleteCircuit(gas, cost) -> int:
    total_gas = 0
    total_cost = 0
    for i in range(len(gas)):
        total_gas += gas[i]
        total_cost += cost[i]

    if total_gas < total_cost:
        return -1

    cur_total = 0
    start = 0
    for i in range(len(gas)):
        diff = gas[i] - cost[i]
        cur_total = cur_total + diff
        if cur_total < 0:
            cur_total = 0
            start = i + 1

    return start

if __name__=="__main__":
    # Example 1
    gas = [2, 3, 4]
    cost = [3, 4, 3]
    print(canCompleteCircuit(gas, cost))

    # Example 2
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    print(canCompleteCircuit(gas, cost))