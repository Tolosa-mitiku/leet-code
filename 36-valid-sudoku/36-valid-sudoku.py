class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        count = defaultdict(list)
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] != ".":
                    if board[i][j] in count:
                        for k in count[board[i][j]]:
                            if k[0] == i or k[1] == j or (k[0]//3 == i//3 and k[1]//3 == j//3):
                                return False                          
                    count[board[i][j]].append((i, j))
        return True
                    
                        