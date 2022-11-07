class Solution:
    def fib(self, n: int) -> int:
        @lru_cache
        def helper(n):
            if n == 1:
                return 1
            elif n == 0:
                return 0
            return helper(n-1) + helper(n-2)
        return helper(n)