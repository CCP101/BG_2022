class Solution:
    def __init__(self):
        self.path = []
        self.paths = []

    def subsetsWithDup(self, nums):
        nums.sort()
        self.backtracking(nums, 0)
        return self.paths

    def backtracking(self, nums, start_index):
        self.paths.append(self.path[:])
        if start_index == len(nums):
            return

        for i in range(start_index, len(nums)):
            if i > start_index and nums[i] == nums[i-1]:
                # 当前后元素值相同时，跳入下一个循环，去重
                continue
            self.path.append(nums[i])
            self.backtracking(nums, i+1)
            self.path.pop()    
