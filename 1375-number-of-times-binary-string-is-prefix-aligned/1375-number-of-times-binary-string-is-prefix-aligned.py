class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        count = 0
        prefix = 0
        ans = 0
        for j in range(len(flips)):
            prefix += j+1
            count += flips[j]
            if count == prefix:
                ans += 1
        return ans