# Definition for a binary tree node.
from unittest import result


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root, targetSum: int):
        def traversal(cur_node, remain): 
            if not cur_node.left and not cur_node.right and remain == 0: 
                result.append(path[:])
                return

            if not cur_node.left and not cur_node.right: 
                return 

            if cur_node.left: 
                path.append(cur_node.left.val)
                remain -= cur_node.left.val
                traversal(cur_node.left, remain)
                path.pop()
                remain += cur_node.left.val

            if cur_node.right: 
                path.append(cur_node.right.val)
                remain -= cur_node.right.val
                traversal(cur_node.right, remain)
                path.pop()
                remain += cur_node.right.val
        result = []
        path = []
        if not root:
            return []
        path.append(root.val)
        traversal(root, targetSum - root.val)
        return result