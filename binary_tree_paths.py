class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def binaryTreePaths(root):
    """
    :type root: Optional[TreeNode]
    :rtype: List[str]
    """
    stack = [[root]]

    res = []
    while stack:
        cur_path = stack.pop()
        cur_node = cur_path[-1]
        if not cur_node.left and not cur_node.right:
            res.append("->".join([str(node.val) for node in cur_path]))

        if cur_node.right:
            stack.append(cur_path + [cur_node.right])

        if cur_node.left:
            stack.append(cur_path + [cur_node.left])

    return res