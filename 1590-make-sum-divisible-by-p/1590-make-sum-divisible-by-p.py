class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        totalsum = sum(nums)
        prefix = defaultdict(int)
        divcount = 0
        prefix[0] = -1
        ans = inf
        if totalsum % p == 0:
            return 0
        for i in range(len(nums)):
            divcount += nums[i]
            if (divcount - totalsum) % p in prefix:
                ans = min(ans, i - prefix[(divcount - totalsum) % p])
            prefix[divcount % p] = i
        return ans if ans < len(nums) else -1