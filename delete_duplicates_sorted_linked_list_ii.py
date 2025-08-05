def deleteDuplicates(head):
    """
    :type head: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    if not head:
        return head

    hashmap = {}
    curr_node = head
    while curr_node:
        hashmap[curr_node.val] = hashmap.get(curr_node.val, 0) + 1
        curr_node = curr_node.next

    # remove all the duplicates
    curr_node = head
    while curr_node:
        while curr_node.next and hashmap[curr_node.next.val] > 1:
            curr_node.next = curr_node.next.next
        curr_node = curr_node.next

    if hashmap[head.val] > 1:
        return head.next
    return head