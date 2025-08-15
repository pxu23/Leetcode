import heapq

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    """
    :type lists: List[Optional[ListNode]]
    :rtype: Optional[ListNode]
    """

    heap = []

    for i in range(len(lists)):
        cur_node = lists[i]
        while cur_node:
            heapq.heappush(heap, cur_node.val)
            cur_node = cur_node.next

    res = ListNode()
    cur_node_res = res
    while heap:
        popped_node_val = heapq.heappop(heap)
        new_node = ListNode(popped_node_val)
        cur_node_res.next = new_node
        cur_node_res = cur_node_res.next

    return res.next