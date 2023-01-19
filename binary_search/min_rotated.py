def find_min_rotated(arr) -> int:
    s,e=0,len(arr)-1
    min_idx = -1
    while s<=e:
        mid=(e+s)//2
        if arr[mid] <= arr[e]:
            min_idx=mid
            e=mid-1
        else:
            s=mid+1
    return min_idx