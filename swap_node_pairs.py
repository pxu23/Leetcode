class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def swapPairs(head):
    """
    :type head: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    if not head or not head.next:
        return head

    # perform the swap of a pair
    first = head
    second = head.next
    first.next = swapPairs(second.next)
    second.next = first

    return second

if __name__ == '__main__':
    # Example 1
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head = swapPairs(head)
    cur_node = head
    while cur_node:
        print(cur_node.val)
        cur_node = cur_node.next
    print()

    # Example 2
    head = ListNode()
    head = swapPairs(head)
    cur_node = head
    while cur_node:
        print(cur_node.val)
        cur_node = cur_node.next
    print()

    # Example 3
    head = ListNode(1)
    head = swapPairs(head)
    cur_node = head
    while cur_node:
        print(cur_node.val)
        cur_node = cur_node.next
    print()

    # Example 4
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head = swapPairs(head)
    cur_node = head
    while cur_node:
        print(cur_node.val)
        cur_node = cur_node.next
