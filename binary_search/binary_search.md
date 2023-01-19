# Binary Search

Analize the problem and figure out how can you loop through the problem, if there is some portion of the problem that is sorted and you need
to find something within that range of sorted values binary search might be the tool. 

For example the newspaper problem was not obvious that you could use binary search, by noticing that the max value and the sum value of the values in the array would be the range and that you need to find a value in the middle that let you fulfill the task was visible that you could use binary search.

Figure out what would be the min and max values, what is exactly that you want to find, and do the binary operation.
Here is a template for binary search.

```py
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
```