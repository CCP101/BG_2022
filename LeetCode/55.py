class Solution:
    def canJump(self, nums) -> bool:
        cover = 0
        if len(nums) == 1: 
            return True
        i = 0