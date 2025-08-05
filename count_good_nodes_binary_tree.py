# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def goodNodes(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    good_nodes = 0

    largest = float('-inf')

    stack = [(root, largest)]

    while stack:
        node, largest = stack.pop()

        if node.val >= largest:
            good_nodes += 1

        largest = max(largest, node.val)

        if node.right:
            stack.append((node.right, largest))

        if node.left:
            stack.append((node.left, largest))

    return good_nodes