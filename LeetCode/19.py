# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
        res = ListNode(next=head)
        slow, fast = res, res
        while n != 0:
            fast = fast.next
            n -= 1
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return res.next
