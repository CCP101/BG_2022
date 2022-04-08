# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def inorderTraversal(self, root):
        # if not root:
        #     return []
        # stack = []
        # result = []
        # cur = root
        # while cur or stack:
        #     if cur:
        #         stack.append(cur)
        #         cur = cur.left
        #     else:
        #         cur = stack.pop()
        #         result.append(cur.val)
        #         cur = cur.right
        # return result

        result = []
        st = []
        if root:
            st.append(root)
        while st:
            node = st.pop()
            if node is not None:
                if node.right:  # 添加右节点（空节点不入栈）
                    st.append(node.right)

                st.append(node)  # 添加中节点
                st.append(None)  # 中节点访问过，但是还没有处理，加入空节点做为标记。

                if node.left:  # 添加左节点（空节点不入栈）
                    st.append(node.left)
            else:  # 只有遇到空节点的时候，才将下一个节点放进结果集
                node = st.pop()  # 重新取出栈中元素
                result.append(node.val)  # 加入到结果集
        return result
