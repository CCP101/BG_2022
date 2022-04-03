# 顺序查找写法
# class Solution:
#     def search(self, nums, target) -> int:
#         for _ in range(0, len(nums)):
#             if nums[_] == target:
#                 return(_)
#         return(-1)

# 二分查找写法
class Solution:
    def search(self, nums, target) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1


sol = Solution()
print(sol.search([-1, 0, 3, 5, 9, 12], 9))
