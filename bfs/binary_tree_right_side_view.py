from typing import List
from collections import deque

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# My solution
def binary_tree_right_side_view(root: Node) -> List[int]:
    queue = deque([root])
    res = []
    while len(queue) > 0:
        n = len(queue)
        for _ in range(n):
            node = queue.popleft()
            if _ == n-1:
                res.append(node.val)
            for child in [node.left, node.right]:
                if child:
                    queue.append(child)
    return res


# ALgo solution
def binary_tree_right_side_view2(root):
    res = []
    queue = deque([root]) # at least one element in the queue to kick start bfs
    while len(queue) > 0: # as long as there is element in the queue
        n = len(queue) # number of nodes in current level
        res.append(queue[0].val) # only append the first node we encounter since it's the rightmost
        for _ in range(n): # dequeue each node in the current level
            node = queue.popleft()
            for child in [node.right, node.left]: # add right child first so it'll pop out of the queue first
                if child is not None:
                    queue.append(child)
    return res

# Seems like you can treat it as an array