class Solution:
    def __init__(self, num):
        self.n = num

    def calculate(self, num):
        sum = 0
        while num > 0:
            sum += (num % 10) ** 2
            num //= 10
        return sum

    def isHappy(self):
        record = set()
        while True:
            self.n = self.calculate(self.n)
            if self.n == 1:
                return True
            if self.n in record:
                return False
            else:
                record.add(self.n)


soul = Solution(19)
print(soul.isHappy())
