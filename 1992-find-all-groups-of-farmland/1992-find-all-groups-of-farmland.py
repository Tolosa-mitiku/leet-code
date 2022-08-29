class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        bound = lambda row, col : 0 <= row < len(land) and 0 <= col < len(land[0])
        Adj = [[0,1], [1,0]]
        
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
                    if bound(nrow+row, ncol+col) and land[nrow+row][ncol+col] == 1:
                        queue.append((nrow+row, ncol+col))
                        land[nrow+row][ncol+col] = 0
            return [minn[0], minn[1], maxx[0], maxx[1]]
        for i in range(len(land)):
            for j in range(len(land[0])):
                if land[i][j]:
                    ans.append(helper(i, j))
        return ans
                    