# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def getMinimumDifference(root: TreeNode) -> int:
        res = []
        r = float("inf")

        def buildaList(root):
            if not root:
                return None
            if root.left:
                buildaList(root.left)
            res.append(root.val)
            if root.right:
                buildaList(root.right)
            return res

        buildaList(root)
        for i in range(len(res) - 1):
            r = min(abs(res[i] - res[i + 1]), r)
        return r
