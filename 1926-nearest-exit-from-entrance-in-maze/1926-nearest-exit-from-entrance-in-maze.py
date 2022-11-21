class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        def inbound(row, col):
            return 0 <= row < len(maze) and 0 <= col < len(maze[0])
        adj = [[-1,0], [0,-1],[1,0],[0,1]]
        
        queue = deque([(entrance[0], entrance[1], 0)])
        visited = set([(entrance[0], entrance[1])])
        
        while queue:
            row, col, steps = queue.popleft()
            steps += 1
            for dr, dc in adj:
                new_row = row + dr
                new_col = col + dc
                if inbound(new_row, new_col) and (new_row, new_col) not in visited and maze[new_row][new_col] != "+":
                    if new_row == len(maze) - 1 or new_row == 0 or new_col == len(maze[0]) - 1 or new_col == 0:
                        return steps
                    visited.add((new_row, new_col))
                    queue.append((new_row, new_col, steps))
        return -1
                    
                    
                