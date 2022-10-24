class Solution:
    def maxLength(self, arr: List[str]) -> int:
        ans = 0
        def helper(ind, string):
            nonlocal ans
            if len(string) != len(set(string)):
                return
            ans = max(ans, len(string))
            for i in range(ind, len(arr)):
                helper(i + 1, string + arr[i])
        helper(0, "")
        return ans
        