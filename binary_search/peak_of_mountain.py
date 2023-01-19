def peak_of_mountain_array(arr) -> int:
    s,e=0,len(arr)-1
    peak=0
    while s<=e:
        m=(e+s)//2
        if arr[m] > arr[m+1]:
            peak=m
            e=m-1
        else:
            s=m+1
    return peak
