def isSubtree(root, subRoot):
    """
    :type root: Optional[TreeNode]
    :type subRoot: Optional[TreeNode]
    :rtype: bool
    """

    def sameTree(p, q):
        if not p and not q:
            return True

        if not p or not q:
            return False

        return p.val == q.val and sameTree(p.left, q.left) and sameTree(p.right, q.right)

    def has_subtree(root, q):
        if root and not q:
            return False
        if q and not root:
            return False
        if sameTree(root, q):
            return True
        return has_subtree(root.left, q) or has_subtree(root.right, q)

    return has_subtree(root, subRoot)
