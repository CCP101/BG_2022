class Solution:
    @staticmethod
    def reconstructQueue(people):
        people.sort(key=lambda x: (-x[0], x[1]))
        que = []
        for p in people:
            que.insert(p[1], p)
        return que


soul = Solution()
print(soul.reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))
