from typing import List
from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Attempt reversing list
def zig_zag_traversal(root: Node) -> List[List[int]]:
    queue = deque([root])
    res = []
    zig = False
    while len(queue) > 0:
        n = len(queue)
        lvl = []
        for _ in range(n):
            node = queue.popleft()
            lvl.append(node.val)
            for child in [node.left, node.right]:
                if child:
                    queue.append(child)
        if zig:
            zig = False
            lvl.reverse()
        else:
            zig = True
        res.append(lvl)
    return res


# Leetcode solution aooending values in zig zag to lvl
def zigzagLevelOrder(root: Node) -> List[List[int]]:
    if not root:
        return []
    queue = deque([root])
    res = []
    zig = True
    while len(queue) > 0:
        n = len(queue)
        lvl = deque()
        for _ in range(n):
            node = queue.popleft()
            if zig:
                lvl.append(node.val)
            else:
                lvl.appendleft(node.val)
            for child in [node.left, node.right]:
                if child:
                    queue.append(child)
        res.append(lvl)
        zig = not zig
    return res