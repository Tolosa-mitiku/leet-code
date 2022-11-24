class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def inbound(row, col):
            return 0 <= row < len(board) and 0 <= col < len(board[0])
        adj = [[0,1], [1,0], [0,-1], [-1,0]]
        
        def backtrack(row, col, ind, visited):
            if ind == len(word)-1:
                return True
            
            ans = False
            for dr, dc in adj:
                new_row = dr + row
                new_col = dc + col
                if inbound(new_row, new_col) and (new_row, new_col) not in visited and board[new_row][new_col] == word[ind+1]:
                    visited.add((new_row, new_col) )
                    ans = ans or backtrack(new_row, new_col, ind+1, visited)
                    visited.remove((new_row, new_col))
            return ans
        
        res = False
        visited = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    res = res or backtrack(i, j, 0, set([(i,j)]))
        return res