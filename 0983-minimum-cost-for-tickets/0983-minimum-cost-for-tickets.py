class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        @cache
        def dp(ind, var):
            if ind == len(days):
                return 0
            
            ans = float("inf")
            if days[ind] <= var:
                ans = min(ans, dp(ind+1, var))
            else:
                dwy = [1, 7, 30]
                for i in range(len(costs)):
                    ans = min(ans, costs[i] + dp(ind + 1, days[ind] + dwy[i]-1))
            return ans
        return dp(0, -1)