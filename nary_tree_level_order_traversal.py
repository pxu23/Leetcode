from collections import deque

# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

def levelOrder(root):
    """
    :type root: Node
    :rtype: List[List[int]]
    """
    res = []
    if not root:
        return res

    queue = deque()
    queue.append(root)

    while queue:
        n = len(queue)
        level = []
        for _ in range(n):
            node = queue.popleft()
            level.append(node.val)

            for child in node.children:
                queue.append(child)
        res.append(level)
    return res
