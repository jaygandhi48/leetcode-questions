from collections import deque
from typing import List

class Solution:
    def detect(self, i, j, grid, visited):
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        queue.append(((i, j), (-1, -1))) 
        visited[i][j] = 1
        target_char = grid[i][j]  
        
        while queue:
            (r, c), (pr, pc) = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == target_char:
                    if visited[nr][nc] == 0:  
                        visited[nr][nc] = 1
                        queue.append(((nr, nc), (r, c)))
                    elif visited[nr][nc] == 1 and (nr, nc) != (pr, pc):  
                        return True  

        return False
                
    def containsCycle(self, grid: List[List[str]]) -> bool:
        rows, cols = len(grid), len(grid[0])
        visited = [[0] * cols for _ in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                if visited[i][j] == 0 and self.detect(i, j, grid, visited):
                    return True
        
        return False
