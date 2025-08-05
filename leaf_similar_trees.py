# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def leafSimilar(root1, root2):
    """
    :type root1: Optional[TreeNode]
    :type root2: Optional[TreeNode]
    :rtype: bool
    """
    leaf_seq1 = []
    leaf_seq2 = []

    # depth first search on root 1
    stack1 = [root1]
    while stack1:
        cur_node = stack1.pop()
        if not cur_node.right and not cur_node.left:
            # leaf found
            leaf_seq1.append(cur_node.val)

        if cur_node.right:
            stack1.append(cur_node.right)
        if cur_node.left:
            stack1.append(cur_node.left)

    # depth first search on root2
    stack2 = [root2]
    while stack2:
        cur_node = stack2.pop()
        if not cur_node.right and not cur_node.left:
            # leaf found
            leaf_seq2.append(cur_node.val)

        if cur_node.right:
            stack2.append(cur_node.right)

        if cur_node.left:
            stack2.append(cur_node.left)

    if len(leaf_seq1) != len(leaf_seq2):
        return False

    for i in range(len(leaf_seq1)):
        if leaf_seq1[i] != leaf_seq2[i]:
            return False

    return True