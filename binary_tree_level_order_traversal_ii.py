from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def levelOrderBottom(root):
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
        level = []
        n = len(queue)
        for _ in range(n):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        res.insert(0, level)

    return res

if __name__ == "__main__":
    # Example 1
    node = TreeNode(3)
    node.left = TreeNode(9)
    node.right = TreeNode(20)
    node.right.left = TreeNode(15)
    node.right.right = TreeNode(7)
    print(levelOrderBottom(node))

    # Example 2
    node = TreeNode(1)
    print(levelOrderBottom(node))

    # Example 3
    node = None
    print(levelOrderBottom(node))