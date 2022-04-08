class Solution:
    @staticmethod
    def reverseStr(s: str, k: int) -> str:
        s = list(s)
        for i in range(0, len(s), 2 * k):
            print(i)
            s[i:i + k] = reversed(s[i:i + k])
        return ''.join(s)


print(Solution().reverseStr("abcdefg", 2))
