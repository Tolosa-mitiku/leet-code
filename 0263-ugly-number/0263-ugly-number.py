class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0: return False
        primefactors = [2,3,5]
        while n != 1:
            isugly = False
            for i in primefactors:
                if n % i == 0:
                    n /= i
                    isugly = True
                    break
            if not isugly:
                return False
        return True
                