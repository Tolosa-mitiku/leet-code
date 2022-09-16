class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)
        dp = [[0] * (m+1) for _ in range(m+1)]
        
        for l in range(m-1, -1, -1):
            for i in range(m-1, -1, -1):
                r = n - (i-l) - 1
                if r < 0 or r >= n: break
                leftPick = dp[l+1][i+1] + nums[l] * multipliers[i]
                rightPick = dp[l][i+1] + nums[r] * multipliers[i]
                dp[l][i] = max(leftPick, rightPick)
                
        return dp[0][0]