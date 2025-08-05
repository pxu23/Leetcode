# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def lowestCommonAncestor(root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    if not root:
        return None

    if p.val == root.val or q.val == root.val:
        return root

    l = lowestCommonAncestor(root.left, p, q)
    r = lowestCommonAncestor(root.right, p, q)

    if l and r:
        return root

    return l if l else r