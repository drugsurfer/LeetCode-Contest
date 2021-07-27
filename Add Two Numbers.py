'''
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''

class ListNode():
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
def add(node):
    if node is None:
        return ''
    else:
        return add(node.next) + str(node.val)
def addTwoNumbers( l1, l2):
        num1 = add(l1)
        num2 = add(l2)
        result = int(num1) + int(num2)
        if result == 0:
            return ListNode(0)
        start = ListNode()
        end = ListNode()
        start.next = end
        while result > 0:
            temp = ListNode(result % 10)
            end.next = temp
            end = end.next
            result //= 10
        return start.next.next
l1 = ListNode(0)
l2 = ListNode(0)
print(addTwoNumbers(l1, l2))