

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        s = ''
        while head:
            s = s+str(head.val)
            head = head.next
        return int(s, 2)


def iterative(self, head):
    stack = []
    while head:
        stack.append(head.val)
        head = head.next
    i = 0
    s = 0
    while len(stack):
        s += stack.pop() * 2 ** i
        i += 1
    return s