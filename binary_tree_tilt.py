class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findTilt(root):
    """
    :type root: Optional[TreeNode]
    :rtype: int
    """

    if not root:
        return 0

    def computeTilt(node):
        if not node.left and not node.right:
            return 0

        if not node.left:
            return abs(-1 * findSumOfNodeValues(node.right))

        if not node.right:
            return abs(findSumOfNodeValues(node.left))

        return abs(findSumOfNodeValues(node.left) - findSumOfNodeValues(node.right))

    def findSumOfNodeValues(node):
        if not node.left and not node.right:
            return node.val

        if not node.left:
            return node.val + findSumOfNodeValues(node.right)

        if not node.right:
            return node.val + findSumOfNodeValues(node.left)

        return node.val + findSumOfNodeValues(node.left) + findSumOfNodeValues(node.right)

    if root.left is None and root.right is None:
        return 0

    if root.left is None:
        return computeTilt(root) + findTilt(root.right)

    if root.right is None:
        return computeTilt(root) + findTilt(root.left)

    return computeTilt(root) + findTilt(root.left) + findTilt(root.right)