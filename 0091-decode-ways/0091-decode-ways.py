class Solution:
    def numDecodings(self, s: str) -> int:
        @cache
        def dp(ind):
            if ind == len(s):
                return 1
            ans = 0
            if ind + 2 <= len(s) and "09" < s[ind] + s[ind+1] < "27":
                ans += dp(ind + 2)
            if "0" < s[ind] <= "9":
                ans += dp(ind + 1)
            return ans
        return dp(0)