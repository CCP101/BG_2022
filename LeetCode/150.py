class Solution:
    def evalRPN(self, tokens) -> int:
        stack = []
        for item in tokens:
            if item not in {"+", "-", "*", "/"}:
                stack.append(item)
            else:
                first_num, second_num = stack.pop(), stack.pop()
                stack.append(
                    int(eval(f'{second_num} {item} {first_num}')))

        # stack  = []
        # n = len(tokens)
        # a, b = 0, 0
        # for i in range(n):
        #     if stack and tokens[i] in '+-*/':
        #         a = stack.pop()
        #         b = stack.pop()
        #         if tokens[i] == '+':
        #             stack.append(int(b) + int(a))
        #         elif tokens[i] == '-':
        #             stack.append(int(b) - int(a))
        #         elif tokens[i] == '*':
        #             stack.append(int(b) * int(a))
        #         elif tokens[i] == '/':
        #             stack.append(int(b) / int(a))
        #     else:
        #         stack.append(tokens[i])
        return int(stack.pop()) 