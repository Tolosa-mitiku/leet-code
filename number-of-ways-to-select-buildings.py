class Solution:
    def numberOfWays(self, s: str) -> int:
        zeroprefix = []
        oneprefix = []
        c0 = 0
        c1 = 0
        for char in s:
            if char == "0":
                c0 += 1
            else:
                c1 += 1
            zeroprefix.append(c0)
            oneprefix.append(c1)
        ans = 0
        for i in range(1, len(s)-1):
            if s[i] == "0":
                ans += (oneprefix[i-1] * (c1 - oneprefix[i-1]))
            else:
                ans += (zeroprefix[i-1] * (c0 - zeroprefix[i-1]))
        return ans