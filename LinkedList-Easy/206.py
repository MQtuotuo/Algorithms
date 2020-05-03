# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        curr = head
        prev = None
        while curr:
            tmp = curr.next
            curr.next = prev  # curr = 1, curr.next = None; curr = 2,
            prev = curr  # prev = 1
            curr = tmp


            # dummy.next,  head.next, head  = head, dummy.next, head.next

        return prev