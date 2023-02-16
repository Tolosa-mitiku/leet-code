class Solution:
    def romanToInt(self, s: str) -> int:
        dict1 = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        ans = 0
        prev = 0
        for i in range(len(s)-1,-1,-1):
            if dict1[s[i]] >= prev:
                ans += dict1[s[i]]
            else:
                ans -= dict1[s[i]]
            prev = dict1[s[i]]
        return ans
        