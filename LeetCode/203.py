# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def removeElements(head, val):
        dummy_head = ListNode(next=head)  # 添加一个虚拟节点
        cur = dummy_head
        while cur.next is not None:
            if cur.next.val == val:
                cur.next = cur.next.next  # 删除cur.next节点
            else:
                cur = cur.next
        return dummy_head.next


print(Solution().removeElements([1, 2, 6, 3, 4, 5, 6], 6))
