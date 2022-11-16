class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        adj = [[0,1],[1,0],[0,-1],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]
        
        def inbound(row,col):
            return 0 <= row < len(board) and 0 <= col < len(board[0])
        for i in range(len(board)):
            for j in range(len(board[0])):
                count = 0
                for x, y in adj:
                    if inbound(i+x, j+y) and (board[i+x][j+y] == 1 or board[i+x][j+y] == -2):
                        count += 1
                if board[i][j] == 1 and (count < 2 or count > 3):
                    board[i][j] = -2
                elif board[i][j] == 0 and count == 3:
                    board[i][j] = 2
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == -2:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1
                    