class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dp(amount):
            if amount < 0:
                return float("inf")
            if amount == 0:
                return 0
            
            ans = float("inf")
            for i in coins:
                ans = min(ans, 1 + dp(amount-i))
            return ans
        ans = dp(amount)
        return ans if ans != float("inf") else -1