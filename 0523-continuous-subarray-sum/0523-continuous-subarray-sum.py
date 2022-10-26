class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefixdict = defaultdict(int)
        prefixdict[0] = -1
        prefixsum = 0
        for i in range(len(nums)):
            prefixsum += nums[i]
            if prefixsum % k in prefixdict:
                if i - prefixdict[prefixsum %k] >=2:
                    return True
            else:
                prefixdict[prefixsum % k] = i
        return False