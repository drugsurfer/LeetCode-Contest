# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# l1: ListNode, l2: ListNode
# 28 ms
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        nums = {}
        while l1 is not None:
            if l1.val not in nums.keys():
                nums[l1.val] = 0
            nums[l1.val] += 1
            l1 = l1.next
        while l2 is not None:
            if l2.val not in nums.keys():
                nums[l2.val] = 0
            nums[l2.val] += 1
            l2 = l2.next
        start = ListNode()
        end = ListNode()
        start.next = end
        for i in sorted(nums.keys()):
            for j in range(nums[i]):
                temp = ListNode(i)
                end.next = temp
                end = end.next
        return start.next.next

