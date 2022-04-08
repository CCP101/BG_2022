# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def mergeTrees(root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1:
            return root2
        if not root2:
            return root1
        stack1, stack2 = [root1], [root2]
        while stack1 or stack2:
            node1 = stack1.pop()
            node2 = stack2.pop()
            if node1.left and node2.left:
                stack1.append(node1.left)
                stack2.append(node2.left)
            if node1.right and node2.right:
                stack1.append(node1.right)
                stack2.append(node2.right)
            node1.val += node2.val
            if not node1.left and node2.left:
                node1.left = node2.left
            if not node1.right and node2.right:
                node1.right = node2.right
        return root1
