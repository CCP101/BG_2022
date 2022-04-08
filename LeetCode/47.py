class Solution:
    def __init__(self) -> None:
        self.path = []
        self.paths = []

    def permuteUnique(self, nums):
        nums = sorted(nums)
        used = [0] * len(nums)
        self.backtracking(nums, used)
        return self.paths

    def backtracking(self, nums, used):
        # 终止条件
        if len(self.path) == len(nums):
            self.paths.append(self.path[:])
            return
        for i in range(len(nums)):
            if not used[i]:
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                used[i] = 1
                self.path.append(nums[i])
                self.backtracking(nums, used)
                self.path.pop()
                used[i] = 0
