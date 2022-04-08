class Solution:
    @staticmethod
    def merge(intervals):
        if len(intervals) == 0:
            return intervals
        intervals.sort(key=lambda x: x[0])
        print(intervals)
        result = [intervals[0]]
        for i in range(1, len(intervals)):
            last = result[-1]
            if last[1] >= intervals[i][0]:
                result[-1] = [last[0], max(last[1], intervals[i][1])]
            else:
                result.append(intervals[i])
        return result


solu = Solution()
print(solu.merge([[1, 3], [8, 10], [2, 4], [15, 18]]))
