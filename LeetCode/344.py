class Solution:
    @staticmethod
    def reverseString(s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # s.reverse()
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1