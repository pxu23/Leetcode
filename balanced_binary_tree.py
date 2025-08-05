class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBalanced(root) -> bool:
    if not root:
        return True

    def height(root):
        if not root:
            return 0

        if root.left is None and root.right is None:
            return 1

        if root.left is None:
            return 1 + height(root.right)

        if root.right is None:
            return 1 + height(root.left)

        return 1 + max(height(root.left), height(root.right))

    stack = [root]
    while stack:
        cur_node = stack.pop()
        left_height = height(cur_node.left)
        right_height = height(cur_node.right)
        if abs(left_height - right_height) > 1:
            return False

        if cur_node.right:
            stack.append(cur_node.right)

        if cur_node.left:
            stack.append(cur_node.left)

    return True