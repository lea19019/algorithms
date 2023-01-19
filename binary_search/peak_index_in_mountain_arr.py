def peakIndexInMountainArray(arr) -> int:
        s,e=0,len(arr)-1
        peak=0
        while s<=e:
            mid=(e+s)//2
            if mid+1 <= len(arr)-1 and arr[mid]>arr[mid+1]:
                peak=mid
                e=mid-1
            else:
                s=mid+1
        return peak