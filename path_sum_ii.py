class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def pathSum(root, targetSum):
    """
    :type root: Optional[TreeNode]
    :type targetSum: int
    :rtype: List[List[int]]
    """
    if not root:
        return []

    stack = [[root]]

    res = []
    while stack:
        cur_path = stack.pop()
        cur_node = cur_path[-1]

        if not cur_node.right and not cur_node.left:
            total_path_sum = 0
            for node in cur_path:
                total_path_sum += node.val
            if total_path_sum == targetSum:
                res.append([node.val for node in cur_path])

        if cur_node.right:
            stack.append(cur_path + [cur_node.right])

        if cur_node.left:
            stack.append(cur_path + [cur_node.left])

    return res