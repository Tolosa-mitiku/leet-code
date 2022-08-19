class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right, best = 1, max(piles), -1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            ans = 0
            for i in piles:
                ans += ceil(i / mid)
            
            if ans > h:
                left = mid + 1
            else:
                best = mid
                right = mid - 1
        return best