# Definition for a binary tree node.
from sympy import false


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        cur_max = -float("INF")
        def ValidBST(root: TreeNode) -> bool: 
            nonlocal cur_max
            
            if not root: 
                return True
            
            is_left_valid = ValidBST(root.left)
            if cur_max < root.val: 
                cur_max = root.val
            else: 
                return False
            is_right_valid = ValidBST(root.right)
            
            return is_left_valid and is_right_valid
        return ValidBST(root)

        # stack = []
        # cur = root
        # pre = None
        # while cur or stack:
        #     if cur: # 指针来访问节点，访问到最底层
        #         stack.append(cur)
        #         cur = cur.left
        #     else: # 逐一处理节点
        #         cur = stack.pop()
        #         if pre and cur.val <= pre.val: # 比较当前节点和前节点的值的大小
        #             return False
        #         pre = cur 
        #         cur = cur.right
        # return True