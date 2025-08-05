from collections import deque


def combinationSum(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    res = []
    queue = deque()

    queue.append([])

    while queue:
        cur = queue.popleft()
        cur_sum = 0
        for elem in cur:
            cur_sum += elem

        if cur_sum == target:
            res.append(cur)

        for val in candidates:
            if len(cur) == 0 or val >= cur[-1]:
                if cur_sum + val <= target:
                    queue.append(cur + [val])

    return res

if __name__=="__main__":
    # Example 1
    candidates = [2,3,6,7]
    target = 7
    print(combinationSum(candidates, target))

    # Example 2
    candidates = [2, 3, 5]
    target = 8
    print(combinationSum(candidates, target))

    # Example 3
    candidates = [2]
    target = 1
    print(combinationSum(candidates, target))