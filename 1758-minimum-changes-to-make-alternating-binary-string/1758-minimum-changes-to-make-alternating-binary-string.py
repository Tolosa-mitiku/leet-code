class Solution:
    def minOperations(self, s: str) -> int:
        prev = "1" if s[0] == "0" else "0"
        prev2 = s[0]
        count = 0
        count2 = 0
        for i in s:
            if i == prev:
                prev = "1" if i == "0" else "0"
                count += 1
            else:
                prev = i
            if i == prev2:
                prev2 = "1" if i == "0" else "0"
                count2 += 1
            else:
                prev2 = i
        return min(count, count2)