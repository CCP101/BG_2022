# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def findBottomLeftValue(root) -> int:
        if not root:
            return 0
        count = 0
        res = []
        stack = [root]
        while stack:
            level = []
            for _ in range(len(stack)):
                node = stack.pop(0)
                level.append(node.val)
                if node.left and not node.left.left and not node.left.right:
                    count += node.left.val
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            res.append(level[:])
        return res[-1][0]
