class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        scounter = collections.Counter(s)
        tcounter = collections.Counter(t)
        return scounter == tcounter