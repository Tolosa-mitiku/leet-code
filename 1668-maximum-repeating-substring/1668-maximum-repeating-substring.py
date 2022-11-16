class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        
        ans = 1
        while ans * word in sequence:
            ans += 1
        return ans - 1