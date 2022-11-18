class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def mergeSort(nums):
            if len(nums) > 1:
                mid = len(nums) // 2
                left = nums[:mid]
                right = nums[mid:]
                mergeSort(left)
                mergeSort(right)
                
                i = j = 0
                while i < len(left) and j < len(right):
                    if left[i][1] <= right[j][1]:
                        nums[i+j] = left[i]
                        res[left[i][0]] += j
                        i += 1
                    else:
                        nums[i+j] = right[j]
                        j += 1
                
                while i < len(left):
                    nums[i+j] = left[i]
                    res[left[i][0]] += j
                    i += 1
                while j < len(right):
                    nums[i+j] = right[j]
                    j += 1
        res = [0] * len(nums)
        mergeSort(list(enumerate(nums)))
        return res