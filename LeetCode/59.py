class Solution:
    def generateMatrix(self, n: int):
        matrix = [[0] * n for _ in range(n)]
        num = 1
        direction = 0
        while direction < num:
            for up in range(direction, n - 1 - direction):
                matrix[direction][up] = num
                num += 1
            for right in range(direction, n - 1 - direction):
                matrix[right][n - 1 - direction] = num
                num += 1
            for down in range(n - 1 - direction, direction, -1):
                matrix[n - 1 - direction][down] = num
                num += 1
            for left in range(n - 1 - direction, direction, -1):
                matrix[left][direction] = num
                num += 1
            direction += 1
        if n % 2 == 1:
            matrix[n // 2][n // 2] = num
        return matrix


print(Solution().generateMatrix(5))
