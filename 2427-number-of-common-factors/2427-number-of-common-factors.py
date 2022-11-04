class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        ans = 0
        for potentialfactor in range(1, min(a,b)+1):
            if a % potentialfactor == 0 and b % potentialfactor == 0:
                ans += 1
        return ans