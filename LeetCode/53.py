class Solution:
    @staticmethod
    def maxSubArray(nums) -> int:
        result = -float('inf')
        count = 0
        for i in range(len(nums)):
            count += nums[i]
            if count > result:
                result = count
            if count <= 0:
                count = 0
        return result


soul = Solution()
print(soul.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4, 99]))
