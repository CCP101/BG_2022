# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def countNodes(root: TreeNode) -> int:
        # if not root:
        #     return 0
        # return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        if not root:
            return 0
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
            res.append(level)
        count = 0
        for i in range(len(res)):
            count += len(res[i])
        return count
