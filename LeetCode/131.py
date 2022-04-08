class Solution:
    def __init__(self):
        self.paths = []
        self.path = []

    def partition(self, s: str):
        self.backtracking(s, 0)
        return self.paths

    def backtracking(self, s: str, start_index: int) -> None:
        if start_index >= len(s):
            self.paths.append(self.path[:])
            return
        
        for i in range(start_index, len(s)):
            temp = s[start_index:i+1]
            if temp == temp[::-1]:
                self.path.append(temp)
                self.backtracking(s, i+1)   
                self.path.pop()
            else:
                continue
