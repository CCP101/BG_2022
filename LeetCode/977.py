# 暴力写法
# class Solution:
#     def sortedSquares(self, nums):
#         for index in range(0, len(nums)):
#             if nums[index] < 0:
#                 nums[index] = abs(nums[index])
#         nums.sort()
#         for index in range(0, len(nums)):
#             nums[index] = nums[index] ** 2
#         return nums

# 快慢指针
class Solution:
    @staticmethod
    def sortedSquares(nums):
        slow, fast, index = 0, len(nums) - 1, len(nums) - 1
        ans = [-1] * len(nums)
        while slow <= fast:
            lnum = nums[slow] ** 2
            rnum = nums[fast] ** 2
            if lnum < rnum:
                ans[index] = rnum
                fast -= 1
                index -= 1
            else:
                ans[index] = lnum
                slow += 1
                index -= 1
        return ans


print(Solution().sortedSquares([-4, -1, 0, 3, 10]))
