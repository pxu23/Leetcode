def deleteDuplicates(head):
    """
    :type head: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    curr_node = head
    while curr_node and curr_node.next:
        while curr_node.next and curr_node.val == curr_node.next.val:
            curr_node.next = curr_node.next.next
        curr_node = curr_node.next

    return head