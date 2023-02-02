from typing import List
from math import inf

# Solution 1, fails wwit large input, ain't using memoization
def coin_change_sol1(coins: List[int], amount: int) -> int:
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

# This solution incorporates memoization
# I incorporated the idea of dfs max depth, but in this case it was a min depth.
# 
def coin_change_sol2(coins: List[int], amount: int) -> int:
    memo = {}
    def dfs(count):
        if count == amount:
            return 0
        if count in memo:
            return memo[count]+1 # Adding one because we are going 1 level up
        ans = inf # Unless we find a solution we return 'inf'
        for coin in coins:
            if count+coin > amount: continue # if we ocntinue it means there is no solution with that coin
            ans = min(ans,dfs(count+coin)) # Save in ans the value of the min levels it takes to reach a solution

        memo[count] = ans # Save how many levels it takes from count to reach if a solution if there is any
        return ans+1 # Adding one because we are going 1 level up
    val = dfs(0)
    return val if val != inf else -1