def dfs(node):
    if not node:
        return
    dfs(node.left)
    dfs(node.right)
    return # Something