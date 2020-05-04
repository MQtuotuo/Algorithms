class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        tmp = []
        curr = head
        while curr:
            tmp.append(curr.val)
            curr = curr.next
        curr = head
        while curr:

            data = tmp.pop()
            if curr.val != data:
                return False
            curr = curr.next
        return True


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        p = head
        q = head
        prev = []
        i = 0
        while q:
            prev.append(q)
            q = q.next
            i = i + 1
        if i < 1:
            return True
        q = prev[i - 1]
        count = 1
        while count <= i // 2 + 1:
            if prev[-count].val != p.val:
                return False
            p = p.next
            count = count + 1
        return True




