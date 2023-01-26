from typing import List

def letter_combinations_of_phone_number(digits: str) -> List[str]:
    res = []
    edges = {
        2: 'abc', 3: 'def', 4: 'ghi',
        5: 'jkl', 6: 'mno', 7: 'pqrs',
        8: 'tuv', 9: 'wxyz'
    }
    def dfs(path, idx):
        if idx == len(digits):
            res.append(''.join(path))
            return
        for edge in edges[int(digits[idx])]:
            path.append(edge)
            dfs(path, idx+1)
            path.pop()
    dfs([],0)
    return res

if __name__ == '__main__':
    digits = input()
    res = letter_combinations_of_phone_number(digits)
    print(' '.join(res))