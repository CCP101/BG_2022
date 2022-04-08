# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traversal(self, nums, left: int, right: int) -> TreeNode:
        if left > right:
            return None
        mid = left + (right - left) // 2
        mid_root = TreeNode(nums[mid])
        mid_root.left = self.traversal(nums, left, mid - 1)
        mid_root.right = self.traversal(nums, mid + 1, right)
        return mid_root

    def sortedArrayToBST(self, nums):
        root = self.traversal(nums, 0, len(nums) - 1)
        return root
