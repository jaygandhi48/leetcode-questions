from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_oranges = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c)) #Get all rotten oranges in the queue first
                elif grid[r][c] == 1:
                    fresh_oranges += 1

       
        if fresh_oranges == 0:
            return 0 #Check if initially there are no freash oranges and are all rotten

        
        minutes = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while queue:
            level_size = len(queue)
            has_rottened_another_orange = False
            
            for _ in range(level_size):
                row, col = queue.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2 
                        queue.append((nr, nc))
                        fresh_oranges -= 1
                        has_rottened_another_orange = True
            
            if has_rottened_another_orange:
                minutes += 1

        
        return minutes if fresh_oranges == 0 else -1
