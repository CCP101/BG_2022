class Solution:
    @staticmethod
    def minWindow(s: str, t: str) -> str:
        # 手动实现
        start = 0
        end = 0
        flag = 1
        length = 10000000000
        for index in range(len(s)):
            t_cp = t
            flag = 1
            if s[index] in t:
                t_cp = t_cp.replace(s[index], "", 1)
                if t_cp == "":
                    return t
                s_index = index + 1
                while t_cp != "":
                    if s_index == len(s):
                        break
                    if s[s_index] in t:
                        t_cp = t_cp.replace(s[s_index], "", 1)
                    if t_cp == "":
                        flag = 0
                        break
                    s_index += 1
                if s_index - index >= len(t) - 1 and flag == 0:
                    if s_index - index + 1 < length:
                        length = s_index - index + 1
                        start = index
                        end = int(start + length)
        index += length
        return s[start:end] if flag == 1 else ""


print(Solution.minWindow("cae"))
