def isSymmetric(root):
    """
    :type root: Optional[TreeNode]
    :rtype: bool
    """

    def symmetricHelper(left, right):
        if not left and not right:
            return True

        if not left or not right:
            return False

        return (left.val == right.val and symmetricHelper(left.left, right.right)
                and symmetricHelper(left.right, right.left))

    return symmetricHelper(root.left, root.right)
