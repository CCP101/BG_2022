class Solution:
    @staticmethod
    def findMinArrowShots(points) -> int:
        if len(points) == 0:
            return 0
        points.sort(key=lambda x: x[0])
        result = 1
        for i in range(1, len(points)):
            if points[i][0] > points[i - 1][1]:
                result += 1
            else:
                points[i][1] = min(points[i - 1][1], points[i][1])  # 更新重叠气球最小右边界
        return result


soul = Solution()
print(soul.findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]))
