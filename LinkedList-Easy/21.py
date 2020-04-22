# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = node = ListNode(0)

        while l1 and l2:
            if l1.val <= l2.val:
                node.next, l1 = l1, l1.next
            else:
                node.next, l2 = l2, l2.next

            node = node.next

        node.next = l1 if l1 else l2

        return dummy.next

s = Solution()
dummy = ListNode(0)

l1 = ListNode(1)
second = ListNode(2)
third= ListNode(4)
l1.next=second
second.next = third



l2 = ListNode(1)
second = ListNode(3)
third= ListNode(4)
l2.next=second
second.next = third

rs = s.mergeTwoLists(l1, l2)


while (rs):
    print(rs.val)
    rs = rs.next
