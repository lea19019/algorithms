from typing import List
from math import inf

# Solution 1, fails wwit large input, ain't using memoization
def coin_change_sol1(coins: List[int], amount: int) -> int:
    memo = {}
    coins.sort(reverse=True)

    def dfs(idx, count):
        if count == amount:
            return idx
        ans = inf
        for coin in coins:
            if count + coin > amount:
                continue
            ans = min(ans,dfs(idx+1, count+coin))
        return ans
    
    val = dfs(0,0)
    return val if val != inf else -1