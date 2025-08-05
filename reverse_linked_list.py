class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def reverseList(head):
    """
    :type head: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    curnode = head
    prevnode = None

    while curnode:
        next_node = curnode.next
        curnode.next = prevnode

        prevnode = curnode
        curnode = next_node

    return prevnode

if __name__ == "__main__":
    # Example 1
    head = [1, 2, 3, 4, 5]
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    head = node1
    head = (reverseList(head))
    cur = head
    while cur:
        print(f"value is {cur.val}")
        cur = cur.next