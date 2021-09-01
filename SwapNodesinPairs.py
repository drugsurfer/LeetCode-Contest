'''
Given a linked list, swap every two adjacent nodes and return its head.
You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
'''
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
def swapPairs(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    dummy_ = dummy = ListNode(0)
    dummy.next = head
    while dummy.next and dummy.next.next:
        p = dummy.next
        q = dummy.next.next
        dummy.next = q
        p.next = q.next
        q.next = p
    return dummy_.next
