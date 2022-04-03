class Solution:
    def twoSum(self, nums, target):
        records = dict()
        for idx, val in enumerate(nums):
            if target - val not in records:
                records[val] = idx
                print(records)
            else:
                return [records[target - val], idx] 

sol = Solution()
print(sol.twoSum([6, 7, 11, 3], 9))