class Solution:
    @staticmethod
    def canConstruct(ransomNote: str, magazine: str) -> bool:
        hash = [0] * 26
        for c in magazine:
            hash[ord(c) - ord('a')] += 1
        for c in ransomNote:
            hash[ord(c) - ord('a')] -= 1
            if hash[ord(c) - ord('a')] < 0:
                return False
        return True


print(str(Solution().canConstruct("aa", "ab")))
