from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def largestValues(self, root):
    """
    :type root: Optional[TreeNode]
    :rtype: List[int]
    """
    if not root:
        return []

    queue = deque()
    queue.append(root)

    res = []
    while queue:
        n = len(queue)
        max_val = float('-inf')
        for _ in range(n):
            cur_node = queue.popleft()
            max_val = max(cur_node.val, max_val)
            if cur_node.left:
                queue.append(cur_node.left)

            if cur_node.right:
                queue.append(cur_node.right)

        res.append(max_val)

    return res