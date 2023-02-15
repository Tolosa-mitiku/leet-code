class Solution:
    def checkValidString(self, s: str) -> bool:
        
        @cache
        def dp(ind, stack):
            if ind == len(s):
                return stack == 0
            ans = False
            if s[ind] == "(":
                ans = ans or dp(ind+1, stack + 1)
            elif s[ind] == ")":
                if stack - 1 >= 0:
                    ans = ans or dp(ind+1, stack-1)
            else:
                if stack - 1 >= 0:
                    ans = ans or dp(ind+1, stack-1)
                ans = ans or dp(ind+1, stack + 1) or dp(ind+1, stack)
            return ans
        return dp(0 , 0)
                