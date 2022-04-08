class Solution:
    @staticmethod
    def reverse(x) -> int:
        if x < 0:
            x = -x
            sign = -1
        else:
            sign = 1
        res = 0
        while x:
            res = res * 10 + x % 10
            x //= 10
        return res * sign if res < 2 ** 31 else 0


print(Solution.reverse(10))
