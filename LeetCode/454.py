class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4) -> int:
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        records = dict()
        for num1 in nums1:
            for num2 in nums2:
                if num1 + num2 not in records:
                    records[num1 + num2] = 1
                else:
                    records[num1 + num2] += 1
        res = 0
        for num3 in nums3:
            for num4 in nums4:
                if -(num3+num4) in records:
                    res += records[-num3 - num4]
        return res

print(Solution().fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2]))