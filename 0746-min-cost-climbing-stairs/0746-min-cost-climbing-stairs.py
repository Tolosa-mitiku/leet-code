class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @lru_cache
        def helper(ind):
            if ind == len(cost):
                return 0
            if ind == len(cost)-1:
                return cost[ind]
            return cost[ind] + min(helper(ind+1), helper(ind+2))
        return min(helper(0), helper(1))