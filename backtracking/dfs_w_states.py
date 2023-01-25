from typing import List

class Node:
    def __init__(self, val, children=None):
        if children is None:
            children = []
        self.val = val
        self.children = children

def ternary_tree_paths(root: Node) -> List[str]:
    roots = []
    def dfs(node, path):
        if not node.children:
            roots.append('->'.join(path) + '->' + str(node.val))

        for child in node.children:
            path.append(str(node.val))
            dfs(child, path)
            path.pop()
            
    dfs(root, [])
    return roots

def build_tree(nodes, f):
    val = next(nodes)
    num = int(next(nodes))
    children = [build_tree(nodes, f) for _ in range(num)]
    return Node(f(val), children)

if __name__ == '__main__':
    root = build_tree(iter(input().split()), int)
    res = ternary_tree_paths(root)
    for line in res:
        print(line)