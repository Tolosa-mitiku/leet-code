class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        firstsum = [0]
        lastsum = [0]
        countfirst = 0
        countlast = 0
        for i in range(len(nums)):
            countfirst += nums[i]
            firstsum.append(countfirst)
            countlast += nums[len(nums)-i-1]
            lastsum.append(countlast)
        lastsum.reverse()
        ans = -1
        for i in range(1, len(nums)+1):
            if firstsum[i-1] == lastsum[i]:
                return i-1
        return ans