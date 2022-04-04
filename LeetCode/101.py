# Definition for a binary tree node.
from sympy import false


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root) -> bool:
        # if not root:
        #     return True
        # stack = [root]
        # res = []
        # Fnode = TreeNode("N")
        # while stack:
        #     level = []
        #     for _ in range(len(stack)):
        #         node = stack.pop(0)
        #         if node.val:
        #             level.append(node.val)
        #         if not node.left or not node.right:
        #             continue
        #         if node.left:
        #             stack.append(node.left)
        #         else:
        #             stack.append(Fnode)
        #         if node.right:
        #             stack.append(node.right)
        #         else:
        #             stack.append(Fnode)
        #     res.append(level)
        # for i in range(len(res)):
        #     level = res[i]
        #     length = len(level)
        #     if length > 1:
        #         list1 = list(reversed(level))
        #         if list1 == level:
        #             continue
        #         else:
        #             return False
        # return True 
        if not root:
            return True
        st = [] #这里改成了栈
        st.append(root.left)
        st.append(root.right)
        while st:
            leftNode = st.pop()
            rightNode = st.pop()
            if not leftNode and not rightNode:
                continue
            if not leftNode or not rightNode or leftNode.val != rightNode.val:
                return False
            st.append(leftNode.left)
            st.append(rightNode.right)
            st.append(leftNode.right)
            st.append(rightNode.left)
        return True