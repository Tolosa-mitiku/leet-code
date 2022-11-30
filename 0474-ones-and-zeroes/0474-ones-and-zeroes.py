class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        binarystring = []
        
        for string in strs:
            one = 0
            for i in string:
                if i == "1":
                    one += 1
            binarystring.append([one, len(string) - one])
        @cache
        def dp(ind, m, n):
            if ind == len(binarystring):
                return 0
            
            ans = dp(ind+1, m, n)
            if m - binarystring[ind][1] >= 0 and n - binarystring[ind][0] >= 0:
                ans = max(ans, 1 + dp(ind+1, m - binarystring[ind][1], n - binarystring[ind][0]))
            return ans
        return dp(0, m, n)