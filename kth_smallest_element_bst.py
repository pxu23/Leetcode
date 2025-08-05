def kthSmallest(root, k):
    """
    :type root: Optional[TreeNode]
    :type k: int
    :rtype: int
    """

    def inorder(root):
        if not root:
            return []

        return inorder(root.left) + [root.val] + inorder(root.right)

    inorder_res = inorder(root)

    return inorder_res[k - 1]