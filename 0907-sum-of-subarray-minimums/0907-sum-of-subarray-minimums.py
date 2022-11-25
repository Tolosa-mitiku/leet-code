class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        ans = 0
        stack = []
        for i in range(len(arr)):
            count = 1
            while stack and stack[-1][0] >= arr[i]:
                x, y = stack.pop()
                ans += count * y * x % ((10 ** 9) + 7)
                count += y
            stack.append((arr[i], count))
            
        count = 1
        while stack:
            x, y = stack.pop()
            ans += count * y * x % ((10 ** 9) + 7)
            count += y
        return ans % ((10 ** 9) + 7)
        