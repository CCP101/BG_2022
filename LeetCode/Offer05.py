class Solution:
    def replaceSpace(self, s) -> str:
        # return s.replace(" ","%20")

        counter = s.count(' ')
        res = list(s)
        res += ['  '] * counter
        for i in range(len(s)):
            if res[i] == " ":
                res[i+2:] = res[i+1:]
                res[i:i+2] = ['%', '2', '0']
        return ''.join(res[0:len(s)+2*counter])





print(Solution().replaceSpace("    "))