from collections import defaultdict

def findOrder(numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: List[int]
    """
    if len(prerequisites) == 0:
        return [i for i in range(numCourses)]

    # adjacency
    adjacency = defaultdict(list)
    for elem in prerequisites:
        if elem[0] == elem[1]:
            return False
        adjacency[elem[1]].append(elem[0])

    visiting = [False] * numCourses
    visited = [False] * numCourses

    res = []

    def dfs(node):
        if visited[node]:
            return True

        if visiting[node]:
            return False
        visiting[node] = True
        for neighbor in adjacency[node]:
            if not dfs(neighbor):
                return False
        visiting[node] = False
        visited[node] = True
        res.insert(0, node)

        return True

    for i in range(numCourses):
        if not dfs(i):
            return []
    return res

if __name__=="__main__":
    # Example 1
    numCourses = 2
    prerequisites = [[1, 0]]
    print(findOrder(numCourses, prerequisites))

    # Example 2
    numCourses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    print(findOrder(numCourses, prerequisites))

    # Example 3
    numCourses = 1
    prerequisites = []
    print(findOrder(numCourses, prerequisites))