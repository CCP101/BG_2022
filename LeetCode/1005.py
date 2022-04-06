class Solution:
    def largestSumAfterKNegations(self, nums, k: int) -> int:
        A = sorted(nums, key=abs, reverse=True) 
        for i in range(len(A)):
            if k > 0 and A[i] < 0:
                A[i] *= -1
                k -= 1
        if k > 0:
            A[-1] *= (-1)**k
        return sum(A)
