class Solution:
    @staticmethod
    def jump(nums) -> int:
        if len(nums) == 1: 
            return 0
        ans = 0
        curDistance = 0
        nextDistance = 0
        for i in range(len(nums)):
            nextDistance = max(i + nums[i], nextDistance)
            if i == curDistance: 
                if curDistance != len(nums) - 1:
                    ans += 1
                    curDistance = nextDistance
                    if nextDistance >= len(nums) - 1: 
                        break
        return ans