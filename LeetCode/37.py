class Solution:
    @staticmethod
    def solveSudoku(board) -> None:
        #     """
        #     Do not return anything, modify board in-place instead.
        #     """
        #     self.backtracking(board)

        # def backtracking(self, board: List[List[str]]) -> bool:
        #     # 若有解，返回True；若无解，返回False
        #     for i in range(len(board)): # 遍历行
        #         for j in range(len(board[0])):  # 遍历列
        #             # 若空格内已有数字，跳过
        #             if board[i][j] != '.': continue
        #             for k in range(1, 10):
        #                 if self.is_valid(i, j, k, board):
        #                     board[i][j] = str(k)
        #                     if self.backtracking(board): return True
        #                     board[i][j] = '.'
        #             # 若数字1-9都不能成功填入空格，返回False无解
        #             return False
        #     return True # 有解

        # def is_valid(self, row: int, col: int, val: int, board: List[List[str]]) -> bool:
        #     # 判断同一行是否冲突
        #     for i in range(9):
        #         if board[row][i] == str(val):
        #             return False
        #     # 判断同一列是否冲突
        #     for j in range(9):
        #         if board[j][col] == str(val):
        #             return False
        #     # 判断同一九宫格是否有冲突
        #     start_row = (row // 3) * 3
        #     start_col = (col // 3) * 3
        #     for i in range(start_row, start_row + 3):
        #         for j in range(start_col, start_col + 3):
        #             if board[i][j] == str(val):
        #                 return False
        #     return True
        row = [set(range(1, 10)) for _ in range(9)]  # 行剩余可用数字
        col = [set(range(1, 10)) for _ in range(9)]  # 列剩余可用数字
        block = [set(range(1, 10)) for _ in range(9)]  # 块剩余可用数字

        empty = []  # 收集需填数位置
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':  # 更新可用数字
                    val = int(board[i][j])
                    row[i].remove(val)
                    col[j].remove(val)
                    block[(i // 3) * 3 + j // 3].remove(val)
                else:
                    empty.append((i, j))

        def backtrack(iter=0):
            if iter == len(empty):  # 处理完empty代表找到了答案
                return True
            i, j = empty[iter]
            b = (i // 3) * 3 + j // 3
            for val in row[i] & col[j] & block[b]:
                row[i].remove(val)
                col[j].remove(val)
                block[b].remove(val)
                board[i][j] = str(val)
                if backtrack(iter + 1):
                    return True
                row[i].add(val)  # 回溯
                col[j].add(val)
                block[b].add(val)
            return False

        backtrack()
