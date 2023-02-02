from typing import List

# Solution searching the entire tree
def subsets_sol1(nums: List[int]) -> List[List[int]]:
    res = []
    def dfs(path, idx):
        if idx == len(nums):
            res.append(path[:])
            return
        dfs(path+[nums[idx]], idx+1)
        dfs(path, idx+1)
            
    dfs([], 0)
    return res


# solution by saving the path every time you enter to a node, since it will contain the combinations
def subsets_sol2(nums: List[int]) -> List[List[int]]:
    res = []
    def dfs(path, idx):
        res.append(path[:])
        for i in range(idx, len(nums)):
            path.append(nums[i])
            dfs(path, i+1)
            path.pop()
    dfs([], 0)
    return res