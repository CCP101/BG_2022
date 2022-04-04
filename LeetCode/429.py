"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self,root):
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            level = []
            for _ in range(len(stack)):
                node = stack.pop(0)
                level.append(node.val)
                if node.children:
                    stack.extend(node.children)
            res.append(level)
        return res