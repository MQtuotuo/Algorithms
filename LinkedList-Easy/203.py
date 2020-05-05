class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        tmp = ListNode(0)
        tmp.next = head

        cur = tmp
        while tmp.next:
            if tmp.next.val == val:
                tmp.next = tmp.next.next
            else:
                tmp = tmp.next
        return cur.next

    def removeElements1(self, head: ListNode, val: int) -> ListNode:
        tmp = ListNode(0)
        tmp.next = head
        previous, current = tmp, tmp.next
        while current:
            if current.val==val:
                previous.next = current.next
            else:
                previous = current
            current = current.next

        return tmp.next

s = Solution()

l1 = ListNode(6)
second = ListNode(2)
third= ListNode(6)
forth = ListNode(3)
fifth = ListNode(4)
sixth = ListNode(6)
l1.next=second
second.next = third
third.next = forth
forth.next = fifth
fifth.next = sixth


rs = s.removeElements1(l1, 6)

test = rs
while (rs):
    print(rs.val)
    rs = rs.next