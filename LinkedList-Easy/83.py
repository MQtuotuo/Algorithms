# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        p = head
        while p:
            if p.next and p.next.val == p.val:
                p.next = p.next.next
            else:
                p = p.next

        return head

    def deleteDuplicates1(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        # remove one node and don't move the head pointer yet
        if head.val == head.next.val:
            head.next = head.next.next
            self.deleteDuplicates(head)
        else:  # not a duplicate search from next node
            head.next = self.deleteDuplicates(head.next)

        return head

s = Solution()


l1 = ListNode(1)
second = ListNode(1)
third= ListNode(2)
l1.next=second
second.next = third

rs = s.deleteDuplicates(l1)


while (rs):
    print(rs.val)
    rs = rs.next
