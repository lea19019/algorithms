def feasible(arr, w, n):
    th, tw = 0, 0
    for num in arr:
        if th + num > n:
            tw += 1
            th=0
        th += num
    if th != 0:
        tw+=1
    return tw <= w

def newspapers_split(newspapers_read_times: List[int], num_coworkers: int) -> int:
    left, right = max(newspapers_read_times),sum(newspapers_read_times)
    first_true_index = -1
    while left <= right:
        mid = (left + right) // 2
        if feasible(newspapers_read_times, num_coworkers, mid):
            first_true_index = mid
            right = mid - 1
        else:
            left = mid + 1

    return first_true_index
    