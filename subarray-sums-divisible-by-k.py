class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)
        divcount = 0
        prefix[0] += 1
        ans = 0
        for i in nums:
            divcount += i
            if divcount % k in prefix:
                ans += prefix[divcount % k]
            prefix[divcount % k] += 1
        return ans