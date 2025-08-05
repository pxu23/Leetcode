from collections import defaultdict
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def pathSum(root, targetSum):
    """
    :type root: Optional[TreeNode]
    :type targetSum: int
    :rtype: int
    """
    if not root:
        return 0

    stack = [root]

    path_sum_of_path_ending_at_node = defaultdict(list)

    cnt = 0

    while stack:
        cur_node = stack.pop()
        if cur_node.val == targetSum:
            cnt += 1
        path_sum_of_path_ending_at_node[cur_node].append(cur_node.val)
        if cur_node.right:
            for path_sum in path_sum_of_path_ending_at_node[cur_node]:
                path_sum_of_path_ending_at_node[cur_node.right].append(path_sum + cur_node.right.val)
                if path_sum + cur_node.right.val == targetSum:
                    cnt += 1
            stack.append(cur_node.right)

        if cur_node.left:
            for path_sum in path_sum_of_path_ending_at_node[cur_node]:
                path_sum_of_path_ending_at_node[cur_node.left].append(path_sum + cur_node.left.val)
                if path_sum + cur_node.left.val == targetSum:
                    cnt += 1
            stack.append(cur_node.left)

    return cnt