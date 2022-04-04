# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode):
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            level = []
            for _ in range(len(stack)):
                node = stack.pop(0)
                level.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
        #     res.insert(0, level)
        # return res

        res.reverse()
        return res