# Definition for a binary tree node.
# class TreeNode:
def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
class Solution:
    def invertTree(self, root):
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            level = []
            for _ in range(len(stack)):
                node = stack.pop(0)
                level.append(node)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            res.append(level)
        print(len(res))
