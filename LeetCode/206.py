# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        current = head   
        pre = None
        while(current!=None):
            temp = current.next 
            current.next = pre 
            pre = current
            current = temp
        return pre