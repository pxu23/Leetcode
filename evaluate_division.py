from collections import defaultdict

def calcEquation(equations, values, queries):
    """
    :type equations: List[List[str]]
    :type values: List[float]
    :type queries: List[List[str]]
    :rtype: List[float]
    """

    # adjacency list
    adjacency = defaultdict(list)

    # values dictionary
    value_dict = defaultdict(int)

    for i, eq in enumerate(equations):
        elem1, elem2 = eq[0], eq[1]
        adjacency[elem1].append(elem2)
        adjacency[elem2].append(elem1)
        value_dict[(elem1, elem2)] = values[i]
        value_dict[(elem2, elem1)] = float(1) / values[i]

    res = [-1] * len(queries)

    for i, q in enumerate(queries):
        start_node = q[0]
        end_node = q[1]

        if start_node not in adjacency or end_node not in adjacency:
            continue

        stack = [(start_node, 1)]
        visited = set([start_node])
        while stack:
            cur_node, cur_product = stack.pop()
            if cur_node == end_node:
                res[i] = cur_product
                break

            for neigh in adjacency[cur_node]:
                if neigh in visited:
                    continue

                stack.append((neigh, cur_product * value_dict[(cur_node, neigh)]))
                visited.add(neigh)

    return res

if __name__=="__main__":
    # Example 1
    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"],["a", "a"], ["x", "x"]]
    print(calcEquation(equations, values, queries))

    # Example 2
    equations = [["a", "b"], ["b", "c"], ["bc", "cd"]]
    values = [1.5, 2.5, 5.0]
    queries = [["a", "c"], ["c", "b"]]
    print(calcEquation(equations, values, queries))

    # Example 3
    equations = [["a", "b"]]
    values = [0.5]
    queries = [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]
    print(calcEquation(equations, values, queries))
                                                                                             ["bc", "cd"], ["cd", "bc"]]