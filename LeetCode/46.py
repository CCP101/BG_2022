class Solution:
    def __init__(self):
        self.path = []
        self.paths = []

    def permute(self, nums):
        # def backtrack(first = 0):
        #     # 所有数都填完了
        #     if first == n:  
        #         res.append(nums[:])
        #     for i in range(first, n):
        #         # 动态维护数组
        #         nums[first], nums[i] = nums[i], nums[first]
        #         # 继续递归填下一个数
        #         backtrack(first + 1)
        #         # 撤销操作
        #         nums[first], nums[i] = nums[i], nums[first]
        # n = len(nums)
        # res = []
        # backtrack()
        # return res
        self.backtracking(nums)
        return self.paths

    def backtracking(self, nums):
        # Base Case本题求叶子节点
        if len(self.path) == len(nums):
            self.paths.append(self.path[:])
            return

        # 单层递归逻辑
        for i in range(0, len(nums)):  # 从头开始搜索
            # 若遇到self.path里已收录的元素，跳过
            if nums[i] in self.path:
                continue
            self.path.append(nums[i])
            self.backtracking(nums)
            self.path.pop()
        

soul = Solution()
print(soul.permute([1,2,3,4]))