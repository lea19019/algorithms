from typing import List
from collections import deque

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order_traversal(root: Node) -> List[List[int]]:
    queue = deque([root])
    ans = []
    while len(queue) > 0:
        n = len(queue)
        lvl = []
        for _ in range(n):
            node = queue.popleft()
            lvl.append(node.val)
            for child in [node.left, node.right]:
                if child:
                    queue.append(child)
        ans.append(lvl)
    return ans
