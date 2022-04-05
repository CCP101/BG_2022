# Definition for a binary tree node.
from inspect import stack


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        if not root: 
            return False
        stack = [[root,root.val]]

        while stack:
            pop = stack.pop()
            node,val = pop[0], pop[1]
            if val == targetSum and not node.left and not node.right: 
                return True
            if node.left:
                stack.append([node.left,val+node.left.val])
            if node.right:
                stack.append([node.right,val+node.right.val])
        return False
