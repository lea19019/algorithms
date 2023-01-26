from typing import List

# My solution
def permutations(letters: str) -> List[str]:
    ans = []
    def dfs(path, idx, ltrs):
        if idx == len(letters):
            ans.append(''.join(path[:]))
            return
        for char in ltrs:
            path.append(char)
            letter = ltrs[:]
            dfs(path, idx+1, letter.replace(char, ""))
            path.pop()
    dfs([], 0, letters)
    return ans

# Example solution
def permutationsExample(letters):
    def dfs(start_index, path, used, res):
        if start_index == len(letters):
            res.append(''.join(path))
            return

        for i, letter in enumerate(letters):
            # skip used letters
            if used[i]:
                continue
            # add letter to permutation, mark letter as used
            path.append(letter)
            used[i] = True
            dfs(start_index + 1, path, used, res)
            # remove letter from permutation, mark letter as unused
            path.pop()
            used[i] = False

    res = []
    dfs(0, [], [False] * len(letters), res)
    return res

if __name__ == '__main__':
    letters = input()
    res = permutations(letters)
    for line in sorted(res):
        print(line)


'''
For this problem I came up with a solution different to the one given by the example.
The main difference between these 2 solutions is that one uses a list to keep the state
and passes it by reference, whereas my solution creates a copy of the letters removing
the character that was used and then used those letters to keep doing the permutations.
Definitely, the example solution uses less space and is more performant since it doesn't
have to built a new copy of the letters everytime.
'''
# My solution with state
def permutationsState(letters: str) -> List[str]:
    ans = []
    def dfs(path, idx, used):
        if idx == len(letters):
            ans.append(''.join(path[:]))
            return
        for i, char in enumerate(letters):
            if used[i]:
                continue
            path.append(char)
            used[i] = True
            dfs(path, idx+1, used)
            used[i] = False
            path.pop()
    dfs([], 0, [False]*len(letters))
    return ans