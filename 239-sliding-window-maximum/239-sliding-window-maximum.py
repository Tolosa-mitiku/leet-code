class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        for i in range(k-1):
            if not queue:
                queue.append(nums[i])
            else:
                while queue and queue[-1] < nums[i]:
                    queue.pop()
                queue.append(nums[i])
        r = k-1
        ans = []
        for i in range(r, len(nums)):
            while queue and queue[-1] < nums[i]:
                queue.pop()
            queue.append(nums[i])
            ans.append(queue[0])
            if queue[0] == nums[i-k+1]:
                queue.popleft()
        return ans
                
        