class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_balanced(tree: Node) -> bool:
    def dfs(node):
        if not node:
            return 0
        l=dfs(node.left)
        r=dfs(node.right)
        if l==-1 or r==-1:
            return -1
        elif abs(l-r) > 1:
            return -1
        else:
            return max(l,r)+1
    return dfs(tree) != -1

def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

if __name__ == '__main__':
    tree = build_tree(iter(input().split()), int)
    res = is_balanced(tree)
    print('true' if res else 'false')