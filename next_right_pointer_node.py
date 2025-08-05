# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

from collections import deque

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        queue = deque()
        queue.append(root)
        idx = 0
        while queue:
            for i in range(2 ** idx):
                cur_node = queue.popleft()
                if i == 2 ** idx - 1:
                    next_node = None
                else:
                    next_node = queue[0]

                cur_node.next = next_node

                if cur_node.left and cur_node.right:
                    queue.append(cur_node.left)
                    queue.append(cur_node.right)

            idx += 1

        return root