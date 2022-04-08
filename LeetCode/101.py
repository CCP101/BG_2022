# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def isSymmetric(root) -> bool:
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
        st = [root.left, root.right]  # 这里改成了栈
        while st:
            left_node = st.pop()
            right_node = st.pop()
            if not left_node and not right_node:
                continue
            if not left_node or not right_node or left_node.val != right_node.val:
                return False
            st.append(left_node.left)
            st.append(right_node.right)
            st.append(left_node.right)
            st.append(right_node.left)
        return True
