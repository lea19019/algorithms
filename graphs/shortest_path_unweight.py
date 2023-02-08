from collections import deque
from typing import List
from math import inf

# Solution with bfs
def shortest_path_bfs(graph: List[List[int]], a: int, b: int) -> int:
    
    def bfs(root, target):
        queue = deque([root])
        visited = set([root])
        lvl = 0
        while len(queue) > 0:
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                if node == target:
                    return lvl
                for neighbor in graph[node]:
                    if neighbor in visited: continue
                    queue.append(neighbor)
                    visited.add(neighbor)
            lvl += 1

    return bfs(a,b)




# Partial solution using DFS, it fails with one test from examples
def shortest_path(graph: List[List[int]], a: int, b: int) -> int:
    
    def dfs(root, target, visited):
        if root == target:
            return 0
        lvl = inf
        for neighbor in graph[root]:
            if neighbor in visited: continue
            visited.add(neighbor)
            lvl = min(lvl, dfs(neighbor, target, visited))
            
        return lvl+1

    return dfs(a,b, set([a]))
