class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    @staticmethod
    def connect(root):
        if not root:
            return None
        stack = [root]
        while stack:
            n = len(stack)
            for _ in range(n):
                node = stack.pop(0)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
                if _ == n - 1:
                    break
                node.next = stack[0]
        return root