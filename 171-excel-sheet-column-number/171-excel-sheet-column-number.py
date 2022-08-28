class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        return sum((ord(columnTitle[len(columnTitle)-i-1]) - 64) * (26 ** (i)) for i in range(len(columnTitle)))