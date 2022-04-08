# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def reverseList(head: ListNode) -> ListNode:
        current = head
        pre = None
        while current is not None:
            temp = current.next
            current.next = pre
            pre = current
            current = temp
        return pre
