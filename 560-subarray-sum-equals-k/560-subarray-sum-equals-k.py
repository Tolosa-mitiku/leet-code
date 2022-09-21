class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        summ = 0
        prefixdict = defaultdict(int)
        prefixdict[0] += 1
        for i in nums:
            summ += i
            if summ - k in prefixdict:
                ans += prefixdict[summ-k]
            prefixdict[summ] += 1
        return ans