class Solution:
    def __init__(self):
        self.path = []
        self.paths = []

    def subsets(self, nums):
        self.backtracking(nums, 0)
        return self.paths

    def backtracking(self, nums, start_index):
        self.paths.append(self.path[:])
        if start_index == len(nums):
            return

        for i in range(start_index, len(nums)):
            self.path.append(nums[i])
            self.backtracking(nums, i+1)
            self.path.pop()    
