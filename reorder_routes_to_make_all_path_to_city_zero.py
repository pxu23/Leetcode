from collections import deque, defaultdict

def minReorder(n, connections):
    """
    :type n: int
    :type connections: List[List[int]]
    :rtype: int
    """
    queue = deque()

    # build the adjacency
    adjacency = defaultdict(list)
    direct_adjacency = defaultdict(list)

    for a, b in connections:
        adjacency[a].append(b)
        adjacency[b].append(a)
        direct_adjacency[a].append(b)

    cnt = 0
    stack = [0]
    visited = set([0])
    while stack:
        cur = stack.pop()
        visited.add(cur)
        for neigh in adjacency[cur]:
            if neigh in visited:
                continue

            if neigh in direct_adjacency[cur]:
                cnt += 1

            stack.append(neigh)
    return cnt

if __name__=="__main__":
    # Example 1
    n = 6
    connections = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]
    print(minReorder(n, connections))

    # Example 2
    n = 5
    connections = [[1, 0], [1, 2], [3, 2], [3, 4]]
    print(minReorder(n, connections))

    # Example 3
    n = 3
    connections = [[1, 0], [2, 0]]
    print(minReorder(n, connections))