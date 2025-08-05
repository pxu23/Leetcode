# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseBetween(head, left, right):
    """
    :type head: Optional[ListNode]
    :type left: int
    :type right: int
    :rtype: Optional[ListNode]
    """
    if not head or not head.next:
        return head
    dummy = ListNode()
    dummy.next = head
    ltail = dummy
    for i in range(left - 1):
        ltail = ltail.next

    prev = ListNode()
    cur = ltail.next

    for j in range(right - left + 1):
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp

    ltail.next.next = cur
    ltail.next = prev
    return dummy.next
