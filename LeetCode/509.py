class Solution:
    @staticmethod
    def fib(n: int) -> int:
        if n < 2:
            return n
        a, b= 0, 1
        count = 0
        for _ in range(1,n):
            count = a + b
            a, b = b, count
        return count
