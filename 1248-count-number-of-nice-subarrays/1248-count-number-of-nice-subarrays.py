class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)
        oddcount = 0
        prefix[0] += 1
        ans = 0
        for i in nums:
            if i % 2 == 1:
                oddcount += 1
            if oddcount - k in prefix:
                ans += prefix[oddcount - k]
            prefix[oddcount] += 1
        return ans