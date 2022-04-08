# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def minCameraCover(root: TreeNode) -> int:
        result = 0

        def travelsal(curr):
            nonlocal result

            left, right = 0, 0
            if curr.left:
                left = travelsal(curr.left)
            else:
                left = 2
            if curr.right:
                right = travelsal(curr.right)
            else:
                right = 2

            if left == 2 and right == 2:
                return 0
            elif left == 0 or right == 0:
                result += 1
                return 1
            elif left == 1 or right == 1:
                return 2

        if travelsal(root) == 0:
            result += 1

        return result
