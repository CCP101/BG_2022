class Solution:
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
                t_cp = t_cp.replace(s[index],"",1)
                if t_cp == "":
                    return t
                s_index = index + 1
                while t_cp != "":
                    if s_index == len(s):
                        break
                    if s[s_index] in t:
                        t_cp = t_cp.replace(s[s_index],"",1)
                    if t_cp == "":
                        flag = 0
                        break
                    s_index += 1
                if s_index-index >= len(t)-1 and flag == 0:
                    if s_index-index+1 < length:
                        length = s_index-index+1
                        start = index
                        end = int(start+length)
        index += length
        return s[start:end] if flag == 1 else "" 

        # 优化版本
        need = defaultdict(int)
        window = defaultdict(int)

        for i in t:
            need[i] += 1

        left, right, valid = 0, 0, 0#valid表示窗口中满足need条件的字符个数，如果valid和len(need)大小相同，则窗口满足条件

        start, lenth = 0, len(s)+1

        while(right < len(s)):
            c = s[right]
            right += 1

            if(c in need):#这个字符有需求, 之前写的need[c]不对，会增加元素（并令默认值为0,因为是defaultdict创建的）
                window[c] += 1
                if(window[c] == need[c]):
                    valid += 1

            while(valid == len(need)):
                if(right - left < lenth):
                    start = left
                    lenth = right - left

                d = s[left]
                left += 1
                if(d in need):#之前写的need[d]只能找到包含S的，找不到最短的
                    if(window[d] == need[d]):
                        valid -= 1
                    window[d] -= 1

        if lenth == len(s)+1:
            return ""
        else:
            return s[start:start+lenth]


print(Solution.minWindow("cabwefgewcwaefgcf","cae"))