class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        A = []
        for i, j in intervals:
            A.append([i, 1])
            A.append([j+1, -1])
        A.sort()
        ans = 0
        curr = 0
        for i, j in A:
            curr += j
            ans = max(ans, curr)
        return ans