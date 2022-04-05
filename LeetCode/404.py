# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root) -> int:
        if not root:
            return 0
        count = 0
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
            
        return count

        # left_left_leaves_sum = self.sumOfLeftLeaves(root.left)  # 左
        # right_left_leaves_sum = self.sumOfLeftLeaves(root.right) # 右
        
        # cur_left_leaf_val = 0
        # if root.left and not root.left.left and not root.left.right: 
        #     cur_left_leaf_val = root.left.val 
            
        # return cur_left_leaf_val + left_left_leaves_sum + right_left_leaves_sum # 中