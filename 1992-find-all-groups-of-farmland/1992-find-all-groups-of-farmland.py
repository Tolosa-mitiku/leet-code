class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        bound = lambda row, col : 0 <= row < len(land) and 0 <= col < len(land[0])
        Adj = [[0,1], [1,0]]
        visited = set()
        
        ans = []
        def helper(x, y):
            maxx = (0,0)
            minn = (len(land)-1,len(land[0])-1)
            queue = deque([(x, y)])
            while queue:
                row, col = queue.popleft()
                maxx = max(maxx, (row, col))
                minn = min(minn, (row, col))
                for nrow, ncol in Adj:
                    if (nrow+row, ncol+col) not in visited and bound(nrow+row, ncol+col) and land[nrow+row][ncol+col] == 1:
                        queue.append((nrow+row, ncol+col))
                    visited.add((nrow+row, ncol+col))
            return [minn[0], minn[1], maxx[0], maxx[1]]
        for i in range(len(land)):
            for j in range(len(land[0])):
                if land[i][j] and (i, j) not in visited:
                    ans.append(helper(i, j))
        return ans
                    