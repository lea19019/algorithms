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


if __name__ == "__main__":
    assert binary_search([1,2,3,4,5,6,7],0) == -1 
    assert binary_search([1,3,5,7,8],5) == 2 
    assert binary_search([2,8,89,120,1000],120) == 3
    print('succesful')


