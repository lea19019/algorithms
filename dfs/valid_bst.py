from math import inf

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def valid_bst(root: Node) -> bool:
    def bst(node, minV, maxV):
        if not node:
            return True
        l=bst(node.left, minV, node.val)
        r=bst(node.right, node.val, maxV)
        if node.val > minV and node.val < maxV and l and r:
            return True
        else:
            return False
    return bst(root, -inf, inf)

def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

if __name__ == '__main__':
    root = build_tree(iter(input().split()), int)
    res = valid_bst(root)
    print('true' if res else 'false')