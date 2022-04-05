class Solution:
    def __init__(self):
        self.path = []
        self.paths = []

    def combinationSum(self, candidates, target: int):
        self.backtracking(candidates, target, 0, 0)
        return self.paths

    def backtracking(self, candidates, target: int, sum: int, start_index: int):
        if sum == target:
            self.paths.append(self.path[:]) 
            return
        if sum > target:
            return 
        
        for i in range(start_index, len(candidates)):
            sum += candidates[i]
            self.path.append(candidates[i])
            self.backtracking(candidates, target, sum, i)  
            sum -= candidates[i]   
            self.path.pop()        
