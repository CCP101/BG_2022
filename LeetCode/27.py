class Solution:
    def removeElement(self, nums, val) -> int:
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return(slow, nums[0:slow])

index, nums = (Solution().removeElement([0,1,2,2,3,0,4,2], 2))
print("index={0},nums={1}".format(index,nums))