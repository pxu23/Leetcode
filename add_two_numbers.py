class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def addTwoNumbers(l1, l2):
    """
    :type l1: Optional[ListNode]
    :type l2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    curr1 = l1
    curr2 = l2

    # summed val
    carry = 0
    prev = ListNode()
    head = prev

    while curr1 or curr2:
        if not curr2:
            summed_digit = (curr1.val + carry)
            curr1 = curr1.next
        elif not curr1:
            summed_digit = (curr2.val + carry)
            curr2 = curr2.next
        else:
            summed_digit = (curr1.val + curr2.val + carry)
            curr1 = curr1.next
            curr2 = curr2.next

        carry = 1 if summed_digit >= 10 else 0
        cur_node = ListNode(summed_digit % 10)
        prev.next = cur_node
        prev = cur_node

    if carry:
        cur_node = ListNode(1)
        prev.next = cur_node

    return head.next