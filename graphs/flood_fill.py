from typing import List
from collections import deque

def flood_fill(r: int, c: int, replacement: int, image: List[List[int]]) -> List[List[int]]:
    num_rows, num_cols = len(image), len(image[0])
    def get_neighbors(coord, color):
        row, col = coord
        delta_row = [-1, 0, 1, 0]
        delta_col = [0, 1, 0, -1]
        res = []
        for i in range(len(delta_row)):
            neighbor_row = row + delta_row[i]
            neighbor_col = col + delta_col[i]
            if 0 <= neighbor_row < num_rows and 0 <= neighbor_col < num_cols:
                if image[neighbor_row][neighbor_col] == color:
                    res.append((neighbor_row, neighbor_col))
        return res

        
    def bfs(root):
        queue = deque([root])
        row, col = root
        color = image[row][col]
        visited = set([root])
        while len(queue) > 0:
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                row, col = node
                image[row][col] = replacement
                for neighbor in get_neighbors(node, color):
                    if neighbor in visited: continue
                    queue.append(neighbor)
                    visited.add(neighbor)
                
    bfs((r,c))
    return image