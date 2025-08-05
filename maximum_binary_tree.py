class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def constructMaximumBinaryTree(nums):
    """
    :type nums: List[int]
    :rtype: Optional[TreeNode]
    """
    if len(nums) == 0:
        return None

    max_idx, max_elem = 0, nums[0]

    for i, elem in enumerate(nums):
        if elem > max_elem:
            max_elem = elem
            max_idx = i

    node = TreeNode(max_elem)
    node.left = constructMaximumBinaryTree(nums[:max_idx])
    node.right = constructMaximumBinaryTree(nums[max_idx + 1:])

    return node