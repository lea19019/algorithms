from collections import deque

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def binary_tree_min_depth(root: Node) -> int:
    queue = deque([root]) # at least one element in the queue to kick start bfs
    depth = -1 # we start from -1 because popping root will add 1 depth
    while len(queue) > 0: # as long as there is element in the queue
        depth += 1
        n = len(queue) # number of nodes in current level
        for _ in range(n): # dequeue each node in the current level
            node = queue.popleft()
            if node.left is None and node.right is None: # found leaf node, early return
                return depth
            for child in [node.left, node.right]:
                if child is not None:
                    queue.append(child)
    return depth


# My implementation of the solution, just modified the starting index of depth to 0
def binary_tree_min_depth(root: Node) -> int:
    queue = deque([root])
    depth = 0
    while len(queue) > 0:
        n = len(queue)
        for _ in range(n):
            node = queue.popleft()
            if not node.left and not node.right:
                return depth
            for child in [node.left, node.right]:
                if child:
                    queue.append(child)
        depth += 1
    return depth