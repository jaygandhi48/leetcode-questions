from collections import deque
from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        original_color = image[sr][sc]

        if original_color == color:
            return image  
        
        queue = deque([(sr, sc)])

        while queue:
            r, c = queue.popleft()
            image[r][c] = color

            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:  
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == original_color:
                    queue.append((nr, nc))

        return image
