class Solution:
    def longestArithSeqLength(self, nums):
        ans, d = 0, defaultdict(lambda: defaultdict(int))
        for i, n1 in enumerate(nums[1:], start=1):
            for j, n2 in enumerate(nums[:i]):
                d[i][n1-n2] = d[j][n1-n2] + 1 if n1-n2 in d[j] else 2
                ans = max(ans, d[i][n1-n2])
        return ans