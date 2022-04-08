class Solution:
    def __init__(self):
        self.answers = []
        self.answer = ''
        self.letterMap = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

    def letterCombinations(self, digits: str):
        if not digits:
            return []
        self.backtracking(digits, 0)
        return self.answers

    def backtracking(self, digits: str, index: int):
        if index == len(digits):  # 当遍历穷尽后的下一层时
            self.answers.append(self.answer)
            return
        letters = self.letterMap[digits[index]]
        for letter in letters:
            self.answer += letter  # 处理
            self.backtracking(digits, index + 1)  # 递归至下一层
            self.answer = self.answer[0:-1]  # 回溯
