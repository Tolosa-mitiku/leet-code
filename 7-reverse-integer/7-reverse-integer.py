class Solution:
    def reverse(self, x: int) -> int:
        num = list(str(x))
        num.reverse()
        if num[-1] == "-":
            num.pop()
            x = int("".join(num))
            x *= -1
        else:
            x = int("".join(num))
        return x if x < (2 ** 31 - 1) and x > -1 * (2 ** 31) else 0