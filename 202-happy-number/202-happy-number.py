class Solution:
    def isHappy(self, n: int) -> bool:
        def helper(n):
            num = str(n)
            if len(num) == 1:
                if n == 1 or n == 7:
                    return True
                else:
                    return False
            ans = 0
            for i in num:
                ans += int(i) ** 2
            return helper(ans)
        return helper(n)