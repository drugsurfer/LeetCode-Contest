class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        if head.next is None:
            return
        start = ListNode()
        l = start
        r = start
        l.next, r.next = head, head
        for i in range(n + 1):
            r = r.next
        while r.next is not None:
            r = r.next
            l = l.next
        l.next = l.next.next
        return start.next
