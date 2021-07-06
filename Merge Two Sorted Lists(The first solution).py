# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# l1: ListNode, l2: ListNode
# 33 ms
def mergeTwoLists(self, l1, l2):
    start = ListNode()
    end = ListNode()
    start.next = end
    while l1 is not None or l2 is not None:
        if l1 is None:
            temp = ListNode(l2.val)
            l2 = l2.next
        elif l2 is None:
            temp = ListNode(l1.val)
            l1 = l1.next
        elif l1.val <= l2.val:
            temp = ListNode(l1.val)
            l1 = l1.next
        else:
            temp = ListNode(l2.val)
            l2 = l2.next
        end.next = temp
        end = end.next
    return start.next.next
