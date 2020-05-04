# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        size = 0
        p = head
        while p:
            size += 1
            p = p.next
        mid = size // 2
        p, pos = head, 0
        while pos != mid:
            p = p.next
            pos += 1
        return p