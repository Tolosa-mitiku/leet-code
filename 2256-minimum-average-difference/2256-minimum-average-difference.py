class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        
        prefixsum = [0]
        for num in nums:
            prefixsum.append(prefixsum[-1] + num)
        
        ans = 0
        minaverage = float("inf")
        for i in range(1,len(prefixsum)):
            firsthalfaverage = prefixsum[i] // i
            secondhalfaverage = ((prefixsum[-1] - prefixsum[i]) // (len(nums) - i)) if (len(nums) - i) != 0 else 0
            absdiff = abs(firsthalfaverage - secondhalfaverage)
            if absdiff < minaverage:
                ans = i - 1 
                minaverage = absdiff
        return ans