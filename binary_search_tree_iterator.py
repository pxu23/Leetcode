# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def __init__(self, root):
        def inorder(root):
            if not root:
                return []
            return inorder(root.left) + [root] + inorder(root.right)

        self.inorder = inorder(root)
        self.cur_idx = 0

    def next(self) -> int:
        # print(self.cur_idx)
        output = self.inorder[self.cur_idx].val
        self.cur_idx += 1
        return output

    def hasNext(self) -> bool:
        return self.cur_idx < len(self.inorder)
