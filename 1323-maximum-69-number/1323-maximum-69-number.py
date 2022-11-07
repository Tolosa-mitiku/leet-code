class Solution:
    def maximum69Number (self, num: int) -> int:
        ans = -1
        count = 0
        res = num
        while num != 0:
            if num % 10 == 6:
                ans = count
            num //= 10
            count += 1
        return res + ((10 ** (ans)) * 3) if ans != -1 else res