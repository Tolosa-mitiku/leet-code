class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        ans = [pivot] * len(nums)
        lessthanpivotcount = 0
        for num in nums:
            if num <= pivot:
                lessthanpivotcount += 1
        leftcount = 0
        rightcount = lessthanpivotcount
        for i in range(len(nums)):
            if nums[i]<pivot:
                ans[leftcount] =  nums[i]
                leftcount += 1
            elif nums[i]>pivot:
                ans[rightcount] =  nums[i]
                rightcount += 1
        return ans