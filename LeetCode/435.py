class Solution:
    def eraseOverlapIntervals(self, intervals) -> int:
        if len(intervals) == 0: 
            return 0
        intervals.sort(key=lambda x: x[1])
        count = 1 
        end = intervals[0][1] 
        for i in range(1, len(intervals)):
            if end <= intervals[i][0]:
                count += 1
                end = intervals[i][1]
        return len(intervals) - count

soul = Solution()
print(soul.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))