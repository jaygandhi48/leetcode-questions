from collections import deque
from typing import List

class Solution:
    def bfs(self, row: int, col: int, grid: List[List[str]], visited: List[List[int]]) -> None:
        queue = deque()
        queue.append((row, col))
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  
        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                ur, uc = row + dr, col + dc
                if 0 <= ur < len(grid) and 0 <= uc < len(grid[0]) and grid[ur][uc] == "1" and visited[ur][uc] == 0:
                    visited[ur][uc] = 1
                    queue.append((ur, uc))
    
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        visited = [[0] * cols for _ in range(rows)]
        count = 0
        for i in range(rows):
            for j in range(cols):
                if visited[i][j] == 0 and grid[i][j] == "1":
                    visited[i][j] = 1
                    self.bfs(i, j, grid, visited)  
                    count += 1
        return count