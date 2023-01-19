def find_boundary(arr: list[bool]) -> int:
    res = -1
    s,e=0,len(arr)-1
    while s<=e:
        mid=(e+s)//2
        if arr[mid]:
            res = mid
            e=mid-1
        else:
            s=mid+1

    return res


if __name__ == "__main__":
    assert find_boundary([False,False,True,True,True]) == 2
    assert find_boundary([True]) == 0
    assert find_boundary([False,False,False]) == -1
    print('succesful')


