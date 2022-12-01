class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        @cache
        def dp(ind, days, maxsofar):
            if ind == len(jobDifficulty) and days == 0:
                return maxsofar
            if ind >= len(jobDifficulty) or days <= 0:
                return float("inf")
            
            return min(dp(ind+1, days, max(maxsofar, jobDifficulty[ind])), max(maxsofar, jobDifficulty[ind]) + dp(ind+1, days - 1, 0))
            return ans
        
        res = dp(0, d, 0)
        return res if res != float("inf") else -1