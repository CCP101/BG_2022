class Solution:
    @staticmethod
    def partitionLabels(s: str):
        hash = [0] * 26
        for i in range(len(s)):
            hash[ord(s[i]) - ord('a')] = i
        result = []
        left = 0
        right = 0
        for i in range(len(s)):
            right = max(right, hash[ord(s[i]) - ord('a')])
            if i == right:
                result.append(right - left + 1)
                left = i + 1
        return result


soul = Solution()
print(soul.partitionLabels("ababcbacadefegdehijhklij"))
