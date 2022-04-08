class Solution:
    def __init__(self):
        self.path = []
        self.paths = []

    def findSubsequences(self, nums):
        self.backtracking(nums, 0)
        return self.paths

    def backtracking(self, nums, start_index):
        if len(self.path) >= 2:
            self.paths.append(self.path[:])
        if start_index == len(nums):
            return
        usage_list = [False] * 201  # 使用列表去重，题中取值范围[-100, 100]
        for i in range(start_index, len(nums)):
            if (self.path and nums[i] < self.path[-1]) or usage_list[nums[i] + 100] == True:
                continue
            usage_list[nums[i] + 100] = True
            self.path.append(nums[i])
            self.backtracking(nums, i + 1)
            self.path.pop()


soul = Solution()
print(soul.findSubsequences([-10, -20, 5, 8, 9, 100]))
