from collections import defaultdict

def canFinish(numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """
    if len(prerequisites) == 0:
        return True

    # adjacency
    adjacency = defaultdict(list)
    for elem in prerequisites:
        if elem[0] == elem[1]:
            return False
        adjacency[elem[1]].append(elem[0])

    visiting = [False] * numCourses
    visited = [False] * numCourses

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
        return True

    for i in range(numCourses):
        if not dfs(i):
            return False
    return True

if __name__ == '__main__':
    # Example 1
    numCourses = 2
    prerequisites = [[1, 0]]
    print(canFinish(numCourses, prerequisites))

    # Example 2
    numCourses = 2
    prerequisites = [[1, 0], [0, 1]]
    print(canFinish(numCourses, prerequisites))