class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for x, y in stones:
            for i, j in stones:
                if x == i or y == j:
                    graph[(x,y)].append((i,j))
        
        def dfs(i,j):
            nonlocal count
            visited.add((i, j))
            count += 1
            for k, v in graph[(i,j)]:
                if (k,v) not in visited:
                    dfs(k, v)
        
        count = 0
        visited = set()
        ans = 0
        for k, v in stones:
            if (k, v) not in visited:
                dfs(k, v)
                ans += count - 1
                count = 0
        return ans