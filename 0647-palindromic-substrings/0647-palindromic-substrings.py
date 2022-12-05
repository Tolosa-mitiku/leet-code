class Solution:
    def countSubstrings(self, s: str) -> int:
        
        ans = 0
        s = list(s)
        for i in range(len(s)):
            temp = []
            for j in range(i, len(s)):
                temp.append(s[j])
                reverse = temp.copy()
                reverse.reverse()
                if temp == reverse:
                    ans += 1
        return ans