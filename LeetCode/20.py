class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for item in s:
            if item == '(' or item == '[' or item == '{':
                stack.append(item)
            else:
                if stack != [] and item == ')':
                    if stack[-1] == '(':
                        stack.pop()
                    else:return False
                elif stack != [] and item == ']':
                    if stack[-1] == '[':
                        stack.pop()
                    else:return False
                elif stack != [] and item == '}':
                    if stack[-1] == '{':
                        stack.pop()
                    else:return False
                else:
                    return False
        print(stack)
        return True if not stack else False

print(Solution().isValid("(])"))