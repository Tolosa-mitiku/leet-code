class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1       
        difference = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        q = deque()
        q.append((0,0))
        visited = {(0, 0)}
        def get_neighbours(x,y):
            for xdifference, ydifference in difference:
                new_row = x + xdifference
                new_col = y + ydifference
                
                if 0 <= new_row < len(grid) and 0 <= new_col < len(grid) and not grid[new_row][new_col] and (new_row, new_col) not in visited:
                    yield (new_row, new_col)                                                
            
        
        current_distance = 1
        while q:
            length = len(q)
            for _ in range(length):
                row, col = q.popleft()
                if row == len(grid)-1 and col == len(grid)-1:
                    return current_distance
                
                for p in get_neighbours(row, col):
                    visited.add(p)
                    q.append(p)
                                    
            current_distance+=1
        
        return -1                
        