from collections import deque


def rightSideView(root):
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
        level = []
        for i in range(n):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res.append(level[-1])
    return res