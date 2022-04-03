# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        p1, p2 = headA, headB
        while p1 != p2:
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA
        return p1

        # p=headA
        # q=headB
        # while p !=q:
        #     if p is None:
        #         p=headB
        #     else:
        #         p=p.next
        #     if q is None:
        #         q=headA
        #     else:
        #         q=q.next
        # return p

        
# 先比较headA与headB的长度，设置坐标a和b ，遍历一遍headA和headB，得到lenA和lenB，若lenA>lenB，则让a往后跳（lenA-lenB）步，反之让b往后跳（lenB-lenA）步。再开始同步向后跳，直到a=b，退出并返回。
