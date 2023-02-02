from typing import List

def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    res = []
    candidates.sort()
    def dfs(path, count, idx):
        if count == target:
            res.append(path[:])
            return
        for i in range(idx,len(candidates)):
            candidate = candidates[i]
            if candidate+count > target:
                continue
            path.append(candidate)
            dfs(path, count+candidate, i)
            path.pop()
    dfs([],0,0)
    return res