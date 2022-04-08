class Solution:
    @staticmethod
    def combine(n: int, k: int):
        res = []  # 存放符合条件结果的集合
        path = []  # 用来存放符合条件结果

        def backtrack(startIndex):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(startIndex, n - (k - len(path)) + 2):  # 优化的地方
                # for i in range(startIndex,n+1):  #原代码
                print(path)
                path.append(i)  # 处理节点
                backtrack(i + 1)  # 递归
                print(path)
                path.pop()  # 回溯，撤销处理的节点

        backtrack(1)
        return res

        # ans = list()
        # t = list()
        #
        # def find_all(i, j):
        #     if j == k:
        #         ans.append(t[:])
        #     else:
        #         if i <= n - k + j + 1:
        #             for a in range(i, n + 1):
        #                 t.append(a)
        #                 find_all(a + 1, j + 1)
        #                 t.pop()
        #
        # find_all(1, 0)
        # return ans


print(Solution.combine(10, 3))
