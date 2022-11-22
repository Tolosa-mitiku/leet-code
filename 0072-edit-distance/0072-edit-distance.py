class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def dp(i, j):
            if i == len(word1):
                return len(word2) - j
            elif j == len(word2):
                return len(word1) - i
            
            ans = float("inf")
            if word1[i] == word2[j]:
                ans = min(ans, dp(i+1, j+1))
            ans = min(ans, 1 + dp(i+1, j+1), 1 + dp(i+1, j), 1 + dp(i, j+1))
            return ans
        return dp(0, 0)
            
            
            