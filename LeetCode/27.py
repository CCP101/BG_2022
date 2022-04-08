from typing import Tuple, List, Any


class Solution:
    @staticmethod
    def removeElement(nums, val) -> Tuple[int, List[Any]]:
        # slow, fast = 0, 0
        # while fast < len(nums):
        #     if nums[fast] != val:
        #         nums[slow] = nums[fast]
        #         slow += 1
        #     fast += 1
        # return(slow, nums[0:slow])
        count = 0
        nlist = list(nums)
        for i in range(len(nlist)):
            if nlist[i] == val:
                count += 1
        while val in nlist:
            nlist.remove(val)
        return count, nlist


index, num = (Solution().removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
print("index={0},nums={1}".format(index, num))
