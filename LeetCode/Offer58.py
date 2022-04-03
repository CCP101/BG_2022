class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        # return s[n:] + s[0:n]

        s = list(s)
        s[0:n] = list(reversed(s[0:n]))
        s[n:] = list(reversed(s[n:]))
        s.reverse()
        
        return "".join(s)

print(Solution().reverseLeftWords("  hello world  ", 5))