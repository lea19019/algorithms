def feasible(val): return val

def binary_search(arr, target: int) -> int:
    left, right = 0, len(arr) - 1
    first_true_index = -1
    while left <= right:
        mid = (left + right) // 2
        if feasible(mid):
            # Probably do something with target
            first_true_index = mid
            right = mid - 1
        else:
            left = mid + 1

    return first_true_index



def vanilla_binary_search(arr, target: int) -> int:
    left, right = 0, len(arr) - 1
    while left <= right:  # <= because left and right could point to the same element, < would miss it
        mid = (left + right) // 2 # double slash for integer division in python 3, we don't have to worry about integer `left + right` overflow since python integers can be arbitrarily large
        # found target, return its index
        if arr[mid] == target:
            return mid
        # middle less than target, discard left half by making left search boundary `mid + 1`
        if arr[mid] < target:
            left = mid + 1
        # middle greater than target, discard right half by making right search boundary `mid - 1`
        else:
            right = mid - 1
    return -1


def dfs(node):
    if not node:
        return
    dfs(node.left)
    dfs(node.right)
    return # Something