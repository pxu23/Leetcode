def combine(n, k):
    """
    :type n: int
    :type k: int
    :rtype: List[List[int]]
    """
    res = [[]]
    for i in range(1, k + 1):
        res = [elem + [j] for elem in res for j in range(i, n + 1) if
               len(elem) == 0 or j > elem[-1]]
    return res

if __name__ == '__main__':
    # Example 1
    n = 4
    k = 2
    print(combine(n, k))

    # Example 2
    n = 1
    k = 1
    print(combine(n, k))