import math


def deleteMiddle(head):
    """
    :type head: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    num_nodes = 0
    curr_node = head

    while curr_node:
        num_nodes += 1
        curr_node = curr_node.next

    mid = math.floor(num_nodes / 2)

    if mid == 0:
        return None

    i = 0
    curr_node = head
    while curr_node:
        if i == mid - 1:
            curr_node.next = curr_node.next.next
            break
        curr_node = curr_node.next
        i += 1

    return head