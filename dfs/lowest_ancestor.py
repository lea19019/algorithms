class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lca(root, node1, node2):
    if not root:
        return None
    if root.val == node1.val or root.val == node2.val:
        return root
    l=lca(root.left, node1, node2)
    r=lca(root.right, node1, node2)
    if l and r:
        return root
    elif l:
        return l
    elif r:
        return r

    return None

if __name__ == '__main__':
    def build_tree(nodes):
        val = next(nodes)
        if not val or val == 'x': return
        cur = Node(val)
        cur.left = build_tree(nodes)
        cur.right = build_tree(nodes)
        return cur
    def find_node(root, target):
        if not root: return
        if root.val == target: return root
        return find_node(root.left, target) or find_node(root.right, target)
    s = input().split()
    root = build_tree(iter(s))
    node1 = find_node(root, input())
    node2 = find_node(root, input())
    ans = lca(root, node1, node2)
    if not ans: print('null')
    else: print(ans.val)