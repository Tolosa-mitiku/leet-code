class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
            @cache
            def dp(start, k):
                if start == len(s) or len(s) - start <= k:
                    return 0
                
                ans = float("inf")
                count = defaultdict(int)
                freq = 0
                
                for j in range(start, len(s)):
                    c = s[j]
                    count[c] += 1
                    freq = max(freq, count[c])
                    
                    comp = 1 + (len(str(freq)) if freq > 1 else 0)
                    
                    prev = (j - start + 1 - freq)
                    if  k >= prev:
                        ans = min(ans, comp + dp(j+1, k - prev))
                return ans
            return dp(0, k)