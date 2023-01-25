from typing import List

def letter_combination(n: int) -> List[str]:
    res = []
    def dfs(path, start_index):
        if start_index >= n:
            res.append(''.join(path))
            return
        for edge in ['a','b']:
            path.append(edge)
            dfs(path, start_index + 1)
            path.pop()
    dfs([],0)
    return res

if __name__ == '__main__':
    n = int(input())
    res = letter_combination(n)
    for line in sorted(res):
        print(line)