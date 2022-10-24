class Solution:
    def inbound(self,i,j, grid):
        return 0 <= i < len(grid) and 0 <= j < len(grid[0])
    def solve(self, grid: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        adj = [[0,1],[1,0],[-1,0],[0,-1]]
        visited = set()
        flag = True


        def dfs(i,j):
            nonlocal flag
            visited.add((i,j))
            temp.add((i,j))
            for drow, dcol in adj:
                newrow, newcol = i+drow, j+dcol
                if not self.inbound(newrow,newcol, grid):
                    flag = False
                if (newrow, newcol) not in visited and self.inbound(newrow,newcol, grid) and grid[newrow][newcol] == "O":
                    dfs(newrow,newcol)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "O" and (i,j) not in visited:
                    temp = set()
                    dfs(i, j)
                    if flag:
                        for row,col in temp:
                            grid[row][col] = "X"
                    flag = True