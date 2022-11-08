class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n)
        dp[-1] = cost[-1]
        dp[-2] = cost[-2]
        for i in range(3,n+1):
            dp[len(cost)-i] = cost[len(cost)-i] + min(dp[len(cost)-i+1], dp[len(cost)-i+2])
        return min(dp[0], dp[1])