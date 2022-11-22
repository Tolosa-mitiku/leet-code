class Solution:
    def numSquares(self, n: int) -> int:
        
        queue = deque([(n, 0)])
        while queue:
            num, dist = queue.popleft()
            for i in range(int(num ** (0.5)), 0, -1):
                var = num - (i * i)
                if var == 0:
                    return dist + 1
                if var >= 0:
                    queue.append((var, dist + 1))
            