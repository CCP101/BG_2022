class Solution:
    def reverseWords(self, s: str) -> str:
        # s = s.split(" ")
        # while '' in s:
        #     s.remove('')
        # newlits = []
        # newstr = ""
        # index = len(s) - 1
        # while index >= 0 :
        #     newlits.append(s[index])
        #     index -= 1
        # for i in range(len(newlits)):
        #     if newlits[i] != " ":
        #         if i != len(newlits) - 1:
        #             newstr += newlits[i] + " "
        #         else:
        #             newstr += newlits[i]
        # return newstr

        return ' '.join(reversed(s.split()))


print(Solution().reverseWords("  hello world  "))
