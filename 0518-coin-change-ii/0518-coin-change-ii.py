class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        @cache
        def dp(ind, target):
            if target == 0:
                return 1
            if ind < 0:
                return 0

            if target < coins[ind]:
                return dp(ind - 1, target)
            else:
                return dp(ind, target - coins[ind]) + dp(ind - 1, target)
        ans = dp(len(coins)-1, amount)
        return ans