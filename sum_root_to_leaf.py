# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumNumbers(root):
    """
    :type root: Optional[TreeNode]
    :rtype: int
    """

    def preorder(node, num):
        if not node:
            return 0

        num = num * 10 + node.val

        # is leaf node
        if not node.left and not node.right:
            return num
        return preorder(node.left, num) + preorder(node.right, num)

    return preorder(root, 0)