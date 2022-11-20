class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dp(ind, target):
            if target > amount:
                return float("inf")
            if target == amount:
                return 0
            if ind == len(coins):
                return float("inf")
            
            ans = min(1 + dp(ind, target + coins[ind]), dp(ind + 1, target), 1 + dp(ind + 1, target + coins[ind]))
            return ans
        ans = dp(0, 0)
        return ans if ans != float("inf") else -1