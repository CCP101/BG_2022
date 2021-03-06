class Solution:
    @staticmethod
    def removeDuplicates(s: str) -> str:
        res = list()
        for i in s:
            if res and res[-1] == i:
                res.pop()
            else:
                res.append(i)
        return ''.join(res)
