class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        ans = 0
        for word in words:
            if len(word) < len(pref):
                continue
            if word[:len(pref)] == pref:
                ans += 1
                
        return ans