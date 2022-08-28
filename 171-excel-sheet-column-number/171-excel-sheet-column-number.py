class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        for i in range(len(columnTitle)-1,-1,-1):
            ans +=  (ord(columnTitle[i]) - 64) * (26 ** (len(columnTitle)-i-1))
        return ans