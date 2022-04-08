class Solution:
    @staticmethod
    def lemonadeChange(bills) -> bool:
        Mdict = {}
        Mdict[5], Mdict[10], Mdict[20] = 0, 0, 0
        for bill in bills:
            if bill == 5:
                Mdict[5] += 1
            elif bill == 10:
                if Mdict[5] < 1: return False
                Mdict[5] -= 1
                Mdict[10] += 1
            else:
                if Mdict[10] > 0 and Mdict[5] > 0:
                    Mdict[10] -= 1
                    Mdict[5] -= 1
                    Mdict[20] += 1
                elif Mdict[5] > 2:
                    Mdict[5] -= 3
                    Mdict[20] += 1
                else:
                    return False
        return True


soul = Solution()
print(soul.lemonadeChange([5, 5, 10, 10, 20]))
