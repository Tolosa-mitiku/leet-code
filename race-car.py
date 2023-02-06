class Solution:
    def racecar(self, target: int) -> int:
        dp = [float('inf')] * (target + 1)
        dp[0] = 0
        for t in range(1, target + 1):
            k = t.bit_length()
            if t == 2**k - 1:
                dp[t] = k
                continue
            for j in range(k - 1):
                dp[t] = min(dp[t], dp[t - 2**(k - 1) + 2**j] + k - 1 + j + 2)
            if 2 ** k - 1- t < t:
                dp[t] = min(dp[t], dp[2**k - 1 - t] + k + 1)
        return dp[target]