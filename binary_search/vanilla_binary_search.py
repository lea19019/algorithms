def binary_search(arr: list, target):
    s,e = 0, len(arr)-1
    while s<=e:
        mid = (e+s)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            e = mid -1
        else:
            s = mid + 1
    return -1

def binary_search_algo(arr, target: int) -> int:
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
    return -1 # if we get here we didn't hit above return so we didn't find target

if __name__ == "__main__":
    assert binary_search([1,2,3,4,5,6,7],0) == -1 
    assert binary_search([1,3,5,7,8],5) == 2 
    assert binary_search([2,8,89,120,1000],120) == 3
    print('succesful')


