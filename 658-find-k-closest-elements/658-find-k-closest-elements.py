class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, k
        summ = 0
        for i in range(k):
            summ += abs(x-arr[i])
        minl = 0
        minr = k - 1
        ans = summ
        while r < len(arr):
            summ -= abs(x-arr[l])
            summ += abs(x-arr[r])
            l+=1
            if summ < ans:
                ans = summ
                minl = l
                minr = r
            r+=1
        ans = []
        for i in range(minl, minr+1):
            ans.append(arr[i])
        return ans
            