class Solution:
    def __init__(self) -> None:
        self.path = []
        self.paths = []

    def combinationSum2(self, candidates, target: int):
        candidates.sort()
        self.backtracking(candidates, target, 0, 0)
        return self.paths

    def backtracking(self, candidates, target, sum, startIndex):
        if sum == target:
            self.paths.append(self.path[:])
            return
        if sum > target:
            return
        for i in range(startIndex, len(candidates)):
            if i > startIndex and candidates[i] == candidates[i - 1]:
                continue
            sum += candidates[i]
            self.path.append(candidates[i])
            self.backtracking(candidates, target, sum, i + 1)
            print(self.path, sum, i + 1)
            sum -= candidates[i]
            self.path.pop()


SOUL = Solution()
print(SOUL.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
