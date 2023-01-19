def square_root(n: int) -> int:
    s,e=0,n
    sr=-1
    while s<=e:
        mid=(e+s)//2
        if mid**2 <= n:
            sr=mid
            s=mid+1
        else:
            e=mid-1
    return sr