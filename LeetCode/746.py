class Solution:
    def minCostClimbingStairs(self, cost):
        dp = [0] * (len(cost))
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, len(cost)):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
        return min(dp[len(cost) - 1], dp[len(cost) - 2])


soul = Solution()
print(soul.minCostClimbingStairs( [1,100,1,1,1,100,1,1,100,1]))