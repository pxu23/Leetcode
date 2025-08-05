class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameterOfBinaryTree(root):
    """
    :type root: Optional[TreeNode]
    :rtype: int
    """
    max_diameter = 0

    def height_diameter(node, max_diameter):
        if not node:
            return 0, 0

        if node.left is None and node.right is None:
            return 0, 0

        if node.left is None:
            right_height, _ = height_diameter(node.right, max_diameter)
            max_diameter = max(max_diameter, 1 + right_height)
            return 1 + right_height, 1 + right_height

        if node.right is None:
            left_height, _ = height_diameter(node.left, max_diameter)
            max_diameter = max(max_diameter, 1 + left_height)
            return 1 + left_height, 1 + left_height

        right_height, _ = height_diameter(node.right, max_diameter)
        left_height, _ = height_diameter(node.left, max_diameter)
        max_diameter = max(max_diameter, 2 + left_height + right_height)
        return 1 + max(left_height, right_height), 2 + left_height + right_height

    _, _ = height_diameter(root, max_diameter)

    return max_diameter