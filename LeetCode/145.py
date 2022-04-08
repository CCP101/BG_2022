class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def postorderTraversal(root):
        # if not root:
        #     return []
        # stack = [root]
        # result = []
        # while stack:
        #     node = stack.pop()
        #     # 中结点先处理
        #     result.append(node.val)
        #     # 左孩子先入栈
        #     if node.left:
        #         stack.append(node.left)
        #     # 右孩子后入栈
        #     if node.right:
        #         stack.append(node.right)
        # # 将最终的数组翻转
        # return result[::-1]
        result = []
        st = []
        if root:
            st.append(root)
        while st:
            node = st.pop()
            if node is not None:
                st.append(node)  # 中
                st.append(None)

                if node.right:  # 右
                    st.append(node.right)
                if node.left:  # 左
                    st.append(node.left)
            else:
                node = st.pop()
                result.append(node.val)
        return result


print(Solution.postorderTraversal())
