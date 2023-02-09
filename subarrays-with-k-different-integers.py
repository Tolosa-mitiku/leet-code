class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def helper(nums, k):
            left = 0
            right = 0
            ans = 0
            visited = set()
            dict1 = collections.Counter()

            while right < len(nums):
                visited.add(nums[right])
                dict1[nums[right]] += 1

                while len(visited) > k:
                    dict1[nums[left]] -= 1
                    if dict1[nums[left]] == 0:
                        visited.remove(nums[left])
                    left += 1

                ans += (right - left + 1)

                right += 1
            return ans
    
        return helper(nums, k) - helper(nums, k - 1)