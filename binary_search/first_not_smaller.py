def first_not_smaller(arr, target: int) -> int:
    s,e=0,len(arr)-1
    first=-1
    while s <= e:
        mid=(e+s)//2
        if arr[mid] >= target:
            first=mid
            e=mid-1
        else:
            s=mid+1
    return first
