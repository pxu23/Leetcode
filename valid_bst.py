# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST(root):
    """
    :type root: Optional[TreeNode]
    :rtype: bool
    """

    def isValidBST(root, min_val, max_val):
        if not root:
            return True

        if not (root.val > min_val and root.val < max_val):
            return False

        return isValidBST(root.left, min_val, root.val) and isValidBST(root.right, root.val, max_val)

    min_val = float('-inf')
    max_val = float('inf')

    return isValidBST(root, min_val, max_val)