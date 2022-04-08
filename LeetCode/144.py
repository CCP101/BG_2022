# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def preorderTraversal(root):
        # if not root:
        #     return []
        # res = []
        # stack = [root]
        # while stack:
        #     node = stack.pop()
        #     res.append(node.val)
        #     if node.right:
        #         stack.append(node.right)
        #     if node.left:
        #         stack.append(node.left)
        # return res
        result = []
        st = []
        if root:
            st.append(root)
        while st:
            node = st.pop()
            if node is not None:
                if node.right:  # 右
                    st.append(node.right)
                if node.left:  # 左
                    st.append(node.left)
                st.append(node)  # 中
                st.append(None)
            else:
                node = st.pop()
                result.append(node.val)
        return result
