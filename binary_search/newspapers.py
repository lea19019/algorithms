def feasible(newspapers, workers, time):
    time_w=0
    workers_t=0
    for pile in newspapers:
        if time_w + pile > time:
            workers_t += 1
            time_w=0
        time_w += pile
    if time_w: 
        workers_t += 1
    return workers_t <= workers
        

def newspapers_split(newspapers_read_times, num_coworkers: int) -> int:
    s,e=max(newspapers_read_times),sum(newspapers_read_times)
    min_time=0
    while s<=e:
        mid=(e+s)//2
        if feasible(newspapers_read_times, num_coworkers, mid):
            min_time=mid
            e=mid-1
        else:
            s=mid+1
    return min_time