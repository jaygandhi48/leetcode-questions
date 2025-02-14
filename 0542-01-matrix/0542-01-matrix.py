from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        result = [[float('inf')] * cols for _ in range(rows)]
        
        queue = deque()
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    result[i][j] = 0
                    queue.append((i, j))
        
        while queue:
            cr, cc = queue.popleft()
            for dr, dc in directions:
                nr, nc = cr + dr, cc + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if result[nr][nc] > result[cr][cc] + 1:
                        result[nr][nc] = result[cr][cc] + 1
                        queue.append((nr, nc))
        
        return result