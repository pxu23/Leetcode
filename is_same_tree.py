def isSameTree(p, q):
    """
    :type p: Optional[TreeNode]
    :type q: Optional[TreeNode]
    :rtype: bool
    """

    if not p and not q:
        return True

    if not p:
        return False

    if not q:
        return False

    return (p.val == q.val and
            isSameTree(p.left, q.left) and
            isSameTree(p.right, q.right))