import math

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums):
    """
    :type nums: List[int]
    :rtype: Optional[TreeNode]
    """

    def getBST(nums, l, r):
        if l > r:
            return None

        if l == r:
            return TreeNode(nums[l])

        mid = int(math.ceil((l + r) / 2))
        node = TreeNode(nums[mid])
        node.left = getBST(nums, l, mid - 1)
        node.right = getBST(nums, mid + 1, r)

        return node

    return getBST(nums, 0, len(nums) - 1)