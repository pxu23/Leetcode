from collections import deque

def combinationSum3(k, n):
    """
    :type k: int
    :type n: int
    :rtype: List[List[int]]
    """
    queue = deque()
    queue.append([])
    res = []

    while queue:
        cur = queue.popleft()
        cur_sum = 0
        for elem in cur:
            cur_sum += elem
        if len(cur) == k and cur_sum == n:
            res.append(cur)

        if len(cur) == 0:
            for i in range(1, 10):
                if cur_sum + i <= n:
                    queue.append(cur + [i])
        else:
            for i in range(cur[-1] + 1, 10):
                if cur_sum + i <= n:
                    queue.append(cur + [i])
    return res

if __name__ == "__main__":
    # Example 1
    k = 3
    n = 7
    print(combinationSum3(k, n))

    # Example 2
    k = 3
    n = 9
    print(combinationSum3(k, n))

    # Example 3
    k = 4
    n = 1
    print(combinationSum3(k, n))