from collections import deque
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxLevelSum(root):
    """
    :type root: Optional[TreeNode]
    :rtype: int
    """
    queue = deque()
    queue.append(root)

    max_level_sum = float('-inf')
    res = 1
    i = 1
    while queue:
        level_sum = 0
        n = len(queue)
        for _ in range(n):
            node = queue.popleft()
            level_sum += node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        if level_sum > max_level_sum:
            max_level_sum = level_sum
            res = i

        i += 1

    return res
