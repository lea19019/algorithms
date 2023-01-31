from typing import List

# THis solution was made not using memoization and constructing the target based on the array of words
def word_break_sol_1_no_memo(s: str, words: List[str]) -> bool:
    def dfs(idx, path):
        if idx == len(s):
            return s == path
        
        ans = False
        for word in words:
            if len(word) + len(path) > len(s):
                continue
            if dfs(len(word)+idx, path+word):
                ans = True
        return ans
    
    return dfs(0, '')


# This solution also does not have memoization and was made validating the prefix of the target with the words list
def word_break_sol2_no_memo(s: str, words: List[str]) -> bool:
    def dfs(idx):
        if idx == len(s):
            return True
        ans = False
        for word in words:
            if s[idx:].startswith(word):
                if dfs(idx+len(word)):
                    ans = True
        return ans
    
    return dfs(0)

# Solution with memoization, its using prefixes as in solution 2
def word_break(s: str, words: List[str]) -> bool:
    memo = {}
    def dfs(idx):
        if idx == len(s):
            return True
        if idx in memo: 
            return memo[idx]
        ans = False
        for word in words:
            if s[idx:].startswith(word):
                if dfs(idx+len(word)):
                    ans = True
        memo[idx] = ans
        return ans
    return dfs(0)