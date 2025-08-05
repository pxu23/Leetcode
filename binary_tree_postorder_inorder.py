# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(inorder, postorder):
    """
    :type inorder: List[int]
    :type postorder: List[int]
    :rtype: Optional[TreeNode]
    """
    if not postorder or not inorder:
        return None

    n = len(postorder)
    root = TreeNode(postorder[-1])

    mid = inorder.index(postorder[-1])

    root.left = buildTree(inorder[:mid], postorder[:mid])
    root.right = buildTree(inorder[mid + 1:], postorder[mid: n - 1])

    return root