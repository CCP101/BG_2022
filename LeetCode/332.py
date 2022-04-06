class Solution:
    def findItinerary(self, tickets):
        tickets_dict = {}
        for item in tickets:
            if item[0] not in tickets_dict.keys():
                tickets_dict[item[0]] = []
            tickets_dict[item[0]].append(item[1])
        path = ["JFK"]

        def backtracking(start_point):
            # 终止条件
            if len(path) == len(tickets) + 1:
                return True
            if start_point not in tickets_dict.keys():
                return
            tickets_dict[start_point].sort()
            for _ in tickets_dict[start_point]:
                #必须及时删除，避免出现死循环
                end_point = tickets_dict[start_point].pop(0)
                path.append(end_point)
                # 只要找到一个就可以返回了
                if backtracking(end_point):
                    return True
                path.pop()
                tickets_dict[start_point].append(end_point)

        backtracking("JFK")
        return path

soul = Solution()
print(soul.findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))