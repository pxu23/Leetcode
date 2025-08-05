# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sortList(head):
    """
    :type head: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    arr = []

    cur_node = head
    while cur_node:
        arr.append(cur_node.val)
        cur_node = cur_node.next

    arr.sort()
    dummy = ListNode()

    cur = dummy
    for i in range(len(arr)):
        node = ListNode(arr[i])
        cur.next = node
        cur = cur.next

    return dummy.next