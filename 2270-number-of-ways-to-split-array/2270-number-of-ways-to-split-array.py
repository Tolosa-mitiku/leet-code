class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        firstPrefixSum = []
        lastPrefixSum = []
        
        count1 = 0
        count2 = 0
        for i in range(len(nums)):
            count1 += nums[i]
            firstPrefixSum.append(count1)
            count2 += nums[len(nums)-1-i]
            lastPrefixSum.append(count2)
        lastPrefixSum.reverse()
        ans = 0
        for i in range(len(nums)-1):
            if firstPrefixSum[i] >= lastPrefixSum[i+1]:
                ans += 1
        return ans