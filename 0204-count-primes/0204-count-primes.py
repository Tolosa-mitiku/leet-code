class Solution:
    def countPrimes(self, n: int) -> int:
        n -= 1
        if n < 2: return 0
        prime = [True for i in range(n+1)]
        p = 2
        while p * p <= n:
            if prime[p]:
                for i in range(2 * p,n+1,p):
                    prime[i] = False
            p += 1
        return sum(prime) - 2