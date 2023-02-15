class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = []
        while columnNumber > 0:
            ans.append(chr(65 + (columnNumber-1) % 26))
            columnNumber = (columnNumber - 1) // 26
        ans.reverse()
        return "".join(ans)