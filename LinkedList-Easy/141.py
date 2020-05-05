# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        l={}
        while head:
            if(head in l):
                return True
            else:
                l[head]=True
            head=head.next
        return False