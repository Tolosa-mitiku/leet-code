class Solution:
    def numSquares(self, n: int) -> int:
        
        @cache
        def dp(n):
            if n == 0:
                return 0
            ans = float("inf")
            for i in range(1, int(n ** (0.5))+1):
                ans = min(ans, 1 + dp(n - (i * i)))
            return ans
        return dp(n)
            