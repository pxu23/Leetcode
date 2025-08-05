# Definition for a binary tree node.
from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root):
    """
    :type root: Optional[TreeNode]
    :rtype: List[List[int]]
    """
    if not root:
        return []

    res = []

    queue = deque()
    queue.append(root)

    while queue:
        n = len(queue)
        level = []

        for i in range(n):
            node = queue.popleft()
            # print(node)
            level.append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        res.append(level)

    return res

if __name__=="__main__":
    # Example 1
    node = TreeNode(3)
    node.left = TreeNode(9)
    node.right = TreeNode(20)
    node.right.left = TreeNode(15)
    node.right.right = TreeNode(7)
    print(levelOrder(node))

    # Example 2
    node = TreeNode(1)
    print(levelOrder(node))

    # Example 3
    node = None
    print(levelOrder(node))
