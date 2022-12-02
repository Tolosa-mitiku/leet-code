class Solution:
    def minSteps(self, s: str, t: str) -> int:
        ans = 0
        tcounter = Counter(t)
        scounter = Counter(s)
        for i in scounter:
            if i in tcounter:
                ans += scounter[i] - tcounter[i] if scounter[i] - tcounter[i] >= 0 else 0
            else:
                ans += scounter[i]
        return ans