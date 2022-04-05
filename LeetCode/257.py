# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root):
    #     path = ''
    #     result = []
    #     if not root: 
    #         return result
    #     self.traversal(root, path, result)
    #     return result

    # def traversal(self, cur: TreeNode, path: str, result):
    #     path += str(cur.val)
    #     # 若当前节点为leave，直接输出
    #     if not cur.left and not cur.right:
    #         result.append(path)
    #         return
    #     if cur.left:
    #         # + '->' 是隐藏回溯
    #         self.traversal(cur.left, path + '->', result)
        
    #     if cur.right:
    #         self.traversal(cur.right, path + '->', result)
        result = []
        path = []
        if not root:
            return result
        self.traversal(root, path, result)
        return result
        
    def traversal(self, cur, path, result):
        path.append(cur.val)
        #这才到了叶子节点
        if not cur.left and not cur.right:
            sPath = ""
            for i in range(len(path)-1):
                sPath += str(path[i])
                sPath += "->"
            sPath += str(path[len(path)-1])
            result.append(sPath)
            return
        if cur.left:
            self.traversal(cur.left, path, result)
            path.pop() #回溯
        if cur.right:
            self.traversal(cur.right, path, result)
            path.pop() #回溯