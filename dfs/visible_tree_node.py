class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def visible_tree_node(root: Node) -> int:
    def dfs(node, maxV):
        if not node:
            return 0
        l = dfs(node.left, max(node.val, maxV))
        r = dfs(node.right,max(node.val, maxV))
        return l+r+1 if node.val >= maxV else l+r
    return dfs(root, root.val)

def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

if __name__ == '__main__':
    root = build_tree(iter(input().split()), int)
    res = visible_tree_node(root)
    print(res)