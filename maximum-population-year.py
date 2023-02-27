class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        ans = [0] * 100
        for b, d  in logs:
            ans[b-1950] += 1
            ans[d-1950] -= 1
        maxx = 0
        count = 0
        curr = 0
        for i in range(len(ans)):
            curr += ans[i]
            if curr > count:
                count = curr
                maxx = i
        return maxx+1950