# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
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
        levelNum = len(res)
        yy = res[0][0]
        for l1 in range(len(res)):
            res[l1].reverse()
        for l1 in range(len(res)):
            if l1 != levelNum -1 :
                Clevel = res[l1]
                Nlevel = res[l1+1]
                count = 0
                for node in Clevel:
                    node.left = Nlevel[count*2]
                    node.right = Nlevel[count*2+1]
                    count += 1
        return yy

        # if not root:
        #     return None
        # root.left, root.right = root.right, root.left #中
        # self.invertTree(root.left) #左
        # self.invertTree(root.right) #右
        # return root