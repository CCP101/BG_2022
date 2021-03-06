class Solution:
    @staticmethod
    def repeatedSubstringPattern(s: str) -> bool:
        # n = len(s)
        # for i in range(1, n // 2 + 1):
        #     if n % i == 0:
        #         if all(s[j] == s[j - i] for j in range(i, n)):
        #             return True
        # return False

        return (s + s).find(s, 1) != len(s)


print(Solution().repeatedSubstringPattern("abab"))
