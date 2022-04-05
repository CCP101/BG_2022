class Solution:
    def __init__(self):
        self.result = []

    def restoreIpAddresses(self, s: str):
        if len(s) > 12: 
            return []
        self.backtracking(s, 0, 0)
        return self.result
    
    def backtracking(self, s: str, start_index: int, point_num: int) -> None:
        if point_num == 3:
            if self.is_valid(s):
                self.result.append(s[:])
            return
        for i in range(start_index, len(s)):
            s = s[:i+1] + '.' + s[i+1:]
            self.backtracking(s, i+2, point_num+1)  
            s = s[:i+1] + s[i+2:]

    def is_valid(self,s:str) -> bool:
        Tlist = s.split(".")
        if len(Tlist) != 4:
            return False
        for i in Tlist:
            if i == "":
                return False 
            if len(i) > 1 and i[0] == "0":
                return False
            num = int(i)
            if num > 255:
                return False
        return True


sou = Solution()
print(sou.restoreIpAddresses("101023"))