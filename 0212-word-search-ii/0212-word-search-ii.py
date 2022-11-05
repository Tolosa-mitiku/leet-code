class Solution:
    def isBound(self, row, col, m, n):
        return 0 <= row < m and 0 <= col < n
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        if not board or not words: return []
        
        boardc = Counter(sum(board, []))
        words = [word for word in words if Counter(word) <= boardc]
        trie = {}
        for word in words:
            node = trie
            for c in reversed(word):
                node = node.setdefault(c, {})
            node['$'] = word
            
        def find(i, j, node):
            if '$' in node: out.append(node.pop('$'))
            if not node: return
            tmp, board[i][j] = board[i][j], '#'
            for dx,dy in [(i+1, j),(i-1,j), (i,j+1), (i,j-1)]:
                if self.isBound(dx, dy, m, n)and board[dx][dy] in node:
                    find(dx,dy,node[board[dx][dy]])
                    if not node[board[dx][dy]]: node.pop(board[dx][dy])
                        
            board[i][j] = tmp
            return 0
                    
        out = []
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    find(i, j, trie[board[i][j]])
                    if not trie[board[i][j]]: trie.pop(board[i][j])
                if len(words) == len(out): return out
        return out